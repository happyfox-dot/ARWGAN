import torch 
import torch.nn as  nn
from kornia.augmentation import RandomSaturation



class random_sat(nn.Module):
    def __init__(self, a ,b ):
        super().__init__()
        self.a = float(a)
        self.b = float(b)
        self.aug = RandomSaturation(saturation=(self.a, self.b),p = 1.)

    def forward(self, noised_and_cover):
        encoder = noised_and_cover[0]
        encoder = self.aug(encoder)
        noised_and_cover[0] = encoder
        return noised_and_cover
