import PIL
import torch
import torch.nn as nn
from kornia.augmentation import RandomMedianBlur
import kornia.filters as filters


# class Median_filter(nn.Module):
#     def __init__(self,kernel_size):
#         super(Median_filter, self).__init__()
#         self.kernel_size=int(kernel_size)
#         self.device=torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

#     def forward(self, noise_and_cover):
#         encoded=noise_and_cover[0].clone()
#         noise_and_cover[0]=filters.MedianBlur(kernel_size=(self.kernel_size,self.kernel_size))(encoded)
#         # noise_and_cover[0]=filters.motion.MotionBlur(ksize=7,angle=35.,direction=-0.5,border_type='reflect')(encoded)
#         return noise_and_cover


class Median_filter(nn.Module):
    def __init__(self, kernel_size):
        super().__init__()
        self.kernel_size = int(kernel_size)
        self.aug = RandomMedianBlur(kernel_size=(self.kernel_size, self.kernel_size))
    
    def forward(self, noised_and_cover):
        encoded = noised_and_cover[0]
        encoded = self.aug(encoded)
        noised_and_cover[0] = encoded
        return noised_and_cover
