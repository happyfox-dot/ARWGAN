import torch.nn
import argparse
import os
import math
import utils
from model.ARWGAN import *
from noise_argparser import NoiseArgParser
from noise_layers.noiser import Noiser
from PIL import Image
import torchvision.transforms.functional as TF
from torchmetrics.classification import MultilabelAccuracy, BinaryAccuracy
import numpy as np
from tqdm import trange
from torch.utils.tensorboard import SummaryWriter
from torchmetrics.image import StructuralSimilarityIndexMeasure
from torchmetrics.image import PeakSignalNoiseRatio


# log file 
write = SummaryWriter(os.path.join('logs/','Jpeg(10.0)'))



#  

def randomCrop(img, height, width):
    # bugfix
    assert img.shape[0] > height
    assert img.shape[1] > width
    x = np.random.randint(0, img.shape[1] - width)
    y = np.random.randint(0, img.shape[0] - height)
    img = img[y:y + height, x:x + width]
    return img


def PSNR(img1, img2):
    img1 , img2 = img1.to('cpu'), img2.to('cpu')
    psnr = PeakSignalNoiseRatio(range = 1.0)
    return psnr(img1.float(), img2.float())
    # mse = np.mean((img1 / 255. - img2 / 255.) ** 2)
    # if mse < 1.0e-10:
    #     return 100
    # PIXEL_MAX = 1
    # return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def SSIM(img1,img2):
    img1 , img2 = img1.to('cpu'), img2.to('cpu')
    ssim = StructuralSimilarityIndexMeasure(range = 255.0)
    return ssim(img1.float(), img2.float())

def bar(message, decode_message):
    metric  = BinaryAccuracy()
    a  = torch.Tensor(message)
    b = torch.Tensor(decode_message)
    b = b.round().clip(0, 1)
    return metric(a, b)
    
    # pass 

def yuv_psnr(img):
    imgy = 0.299 * img[:, 0, :, :] + 0.587 * img[:, 1, :, :] + 0.114 * img[:, 2:, :, :]
    imgu = -0.14713 * img[:, 0, :, :] + (-0.28886) * img[:, 1, :, :] + 0.436 * img[:, 2:, :, :]
    imgv = 0.615 * img[:, 0, :, :] + -0.51499 * img[:, 1, :, :] + (-0.10001) * img[:, 2:, :, :]
    return imgy, imgu, imgv


def main():
    # set cuda:0 is visiable 
    os.environ["CUDA_VISIBLE_DEVICES"] = "1"
    if torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')

    parser = argparse.ArgumentParser(description='Test trained models')
    parser.add_argument('--options-file', '-o', default='options-and-config.pickle', type=str,
                        help='The file where the simulation options are stored.')
    parser.add_argument('--checkpoint-file', '-c', required=True, type=str, help='Model checkpoint file')
    parser.add_argument('--batch-size', '-b', default=12, type=int, help='The batch size.')
    parser.add_argument('--source_images', '-s', required=True, type=str,
                        help='The image to watermark')
    parser.add_argument("--noise", '-n', nargs="*", action=NoiseArgParser)
    # parser.add_argument('--times', '-t', default=10, type=int,
    #                     help='Number iterations (insert watermark->extract).')

    args = parser.parse_args()
    train_options, net_config, noise_config = utils.load_options(args.options_file)
    print(args.noise)
    
    noise_config = args.noise
    
    # 初始化
    noiser = Noiser(noise_config, device)

    checkpoint = torch.load(args.checkpoint_file)
    # info
    hidden_net = ARWGAN(net_config, device, noiser, None)
    utils.model_from_checkpoint(hidden_net, checkpoint)
    # get using file 
    source_images = os.listdir(args.source_images)
    source_images  = sorted(source_images)
    source_images = source_images[len(source_images)//2:]
    psnr_mean = []
    ssim_mean = []
    bar_mean = []
    with trange(len(source_images)) as t:
        for i, source_image in zip(t,source_images):
            # hidden_net = ARWGAN(net_config, device, noiser, None)
            # utils.model_from_checkpoint(hidden_net, checkpoint)
            image_pil = Image.open(args.source_images + source_image)
            # reisze 
            # set the image size is 128 * 128 , could see the info on .pickle
            image_pil = image_pil.resize((net_config.H, net_config.W))
            image_tensor = TF.to_tensor(image_pil).to(device)
            image_tensor = image_tensor * 2 - 1
            image_tensor.unsqueeze_(0)  # add dimmentions
            # np.random.seed(42)
            message = torch.Tensor(np.random.choice([0, 1], (image_tensor.shape[0],
                                                            net_config.message_length))).to(device)

            losses, (encoded_images, noised_images, decoded_messages) = hidden_net.validate_on_batch(
                [image_tensor, message])
            
            # print(encoded_images.shape)
            # print(image_tensor.shape)

            # break
            # calcule metrics 
            psnr_value = PSNR(encoded_images, image_tensor)
            ssim_value = SSIM(encoded_images, image_tensor)
            
            write.add_scalars('Losses/losses',losses,i)

            write.add_scalar('losses/psnr',losses['PSNR'],i)
            write.add_scalar('losses/ssim',losses['ssim'],i)
            write.add_scalar('losses/bitwise-error',losses['bitwise-error'],i)
            psnr_mean.append(psnr_value)
            ssim_mean.append(ssim_value)
            
            # bar_mean.append(losses['bitwise-error'])
            
                                     
            # print('message: {}'.format(message))
            # print('decoded_mesage : {}'.format(decoded_messages))
            
            decoded_rounded = decoded_messages.detach().cpu().numpy().round().clip(0, 1)
            message_detached = message.detach().cpu().numpy()
            bar_mean.append(np.mean(np.abs(decoded_rounded - message_detached)))
            # print('original: {}'.format(message_detached)) 
            # print('decoded : {}'.format(decoded_rounded))
            # break
            
            # print('error : {:.3f}'.format(np.mean(np.abs(decoded_rounded - message_detached))))
            write.add_scalar('metrics/bar', np.mean(np.abs(decoded_rounded - message_detached)),i)
            # write.add_scalar('metrics/error', bar(message, decoded_messages),i)
        # utils.save_images(image_tensor.cpu(), encoded_images.cpu(), 'test', '.', resize_to=(128, 128))
        # print(psnr_mean)
        print(f'psnr mean :{np.mean(psnr_mean)}')
        print(f'ssim mean :{np.mean(ssim_mean)}')
        print(f'bar mean :{(1- np.mean(bar_mean)):.4f}')
if __name__ == '__main__':
    main()
