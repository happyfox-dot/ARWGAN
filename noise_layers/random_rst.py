import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from kornia.augmentation import RandomAffine
from torchvision.ops import masks_to_boxes
import typing

# TE
# 1098

# scale or rotate and translate

# random rotate , scale, translate

# make sure object do not get out of range

# input b,c, w, h 


class RandomRST(nn.Module):
    # Random Roate, Scale, Translate a image while make sure the warped image is not out of the boundary
    # Here, We first randomly rotate and scale the image, then randomly translate the image.
    # However, the random rotate and scale process may cause the warped image out of the boundary.
    def __init__(self, degree: float = 45., scale: tuple = (0.75, 1.5)):
        super(RandomRST, self).__init__()
        
        self.random_rs = RandomAffine(degrees = degree, scale = scale, same_on_batch=False, p=1.)

    def forward(self, noised_and_cover):
        noised_image = noised_and_cover[0]
        batch_size, _, height, width = noised_image.shape
        # Random rotate and scale
        noised_image = self.random_rs(noised_image)
        # mask = torch.ones((batch_size, 1, height, width), dtype=torch.float32, device=noised_image.device)
        # warped_mask = self.random_rs(mask, params=self.random_rs._params)

        # # Random translate
        # for idx in range(noised_image.shape[0]):
        #     # torch.where would return the index of the condition
        #     ind_h, ind_w = torch.where(warped_mask[idx][0].ge(0.5).int() != 0)
        #     margin_u, margin_d = ind_h.min(), height - 1 - ind_h.max()
        #     margin_l, margin_r = ind_w.min(), width - 1 - ind_w.max()
        #     if margin_u + margin_d > 0:
        #         shift_h = np.random.randint(-margin_u, margin_d)
        #     else:
        #         shift_h = 0
        #     if margin_l + margin_r > 0:
        #         shift_w = np.random.randint(-margin_l, margin_r)
        #     else:
        #         shift_w = 0
        #     noised_image[idx] = torch.roll(noised_image[idx], shifts=(shift_h, shift_w), dims=(-2, -1))
        noised_and_cover[0] = noised_image
        return noised_and_cover


def run():
    # Please take a test here.
    # a  = torch.rand(size = (1,3, 256, 256))
    # print(a.shape)
    # rst = RandomRST()
    # a = rst([a])
    # print(a[0].shape)
    pass


if __name__ == '__main__':
    run()
