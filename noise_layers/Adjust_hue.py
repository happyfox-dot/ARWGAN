import torch.nn as nn
import torch
# from kornia import adjust_hue as AdjustSaturation
# from kornia.color.adjust import AdjustHue,AdjustSaturation,AdjustContrast,AdjustBrightness,AdjustGamma
import math
from torchvision.transforms import ToPILImage
# class Adjust_hue(nn.Module):
#     def __init__(self,factor):
#         super(Adjust_hue, self).__init__()
#         self.factor=factor

#     def forward(self, noised_and_cover):
#         encoded=((noised_and_cover[0]).clone())
#         encoded=AdjustSaturation(saturation_factor=self.factor)(encoded)
#         noised_and_cover[0]=(encoded)
#         return noised_and_cover

 
from kornia.augmentation import RandomHue


class random_hue(nn.Module):
    def __init__(self, a, b):
        super(random_hue , self).__init__()
        self.a = float(a) 
        self.b = float(b)
        self.trans = RandomHue(hue = (self.a , self.b), p = 1.0)

    def forward(self, noised_and_cover):
        encoder = ((noised_and_cover[0]).clone())
        encoder = self.trans(encoder)
        noised_and_cover[0] = (encoder)
        return noised_and_cover
        
        # return self.trans(input)
    

def main():
    # input = torch.rand(size= (1,3, 32,32))
    # rh = random_hue(-0.2, 0.2)
    # print(rh(input), rh(input).shape)
    pass

if __name__ == '__main__':
    main()