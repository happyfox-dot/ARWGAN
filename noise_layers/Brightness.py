import torchvision
import torch
import torch.nn as nn

from kornia.augmentation import RandomBrightness



class random_br(nn.Module):
    def __init__(self, a, b ):
        super(random_br, self).__init__()
        self.a = float(a) 
        self.b = float(b)
        print(type(a), type(b))
        self.aug = RandomBrightness(brightness=(self.a, self.b ), p = 1.)
    
    def forward(self, noised_and_cover):
        
        encoder = noised_and_cover[0]
        encoder = self.aug(encoder)
        noised_and_cover[0] = encoder
        return noised_and_cover



