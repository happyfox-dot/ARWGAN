import torch.nn as nn
import torch
# from kornia.color.adjust import AdjustHue,AdjustSaturation,AdjustContrast,AdjustBrightness,AdjustGamma
from kornia.augmentation import RandomContrast
import math
from torchvision.transforms import ToPILImage
# class Adjust_contrast(nn.Module):
#     def __init__(self,factor):
#         super(Adjust_contrast, self).__init__()
#         self.factor=factor

#     def forward(self, noised_and_cover):
#         encoded=((noised_and_cover[0]).clone())
#         encoded=AdjustContrast(contrast_factor=self.factor)(encoded)
#         noised_and_cover[0]=(encoded)
#         return noised_and_cover


class random_constrast(nn.Module):
    def __init__(self, a, b):
        super(random_constrast, self).__init__()
        self.a = float(a) 
        self.b = float(b)
        self.aug = RandomContrast(contrast=(self.a, self.b), p = 1.)

    def forward(self, encoder_and_cover):
        encoder = encoder_and_cover[0]
        encoder = self.aug(encoder)
        encoder_and_cover[0] = encoder
        return encoder_and_cover


def main():
    # input = torch.rand(size=(1,3,32, 32))
    # rc = random_constrast(0.8, 1.0)
    # print(rc(input))
    pass

if __name__ == '__main__':
    main()