import numpy as np
import torch.nn as nn
from noise_layers.identity import Identity
from noise_layers.jpeg_compression import JpegCompression
from noise_layers.quantization import Quantization


class Noiser(nn.Module):
    """
    This module allows to combine different noise layers into a sequential noise module. The
    configuration and the sequence of the noise layers is controlled by the noise_config parameter.
    """
    def __init__(self, noise_layers: list, device):
        super(Noiser, self).__init__()
        # self.noise_layers = [Identity()]
        self.noise_layers = []
        print(f'noise_layers : {noise_layers}')
        print(f'self.noise_layers :{self.noise_layers}')


        for layer in noise_layers:
            if type(layer) is str:
                if layer == 'JpegPlaceholder':
                    self.noise_layers.append(JpegCompression(device))
                elif layer == 'QuantizationPlaceholder':
                    self.noise_layers.append(Quantization(device))
                else:
                    raise ValueError(f'Wrong layer placeholder string in Noiser.__init__().'
                                     f' Expected "JpegPlaceholder" or "QuantizationPlaceholder" but got {layer} instead')
            else:
                self.noise_layers.append(layer)
        # self.noise_layers = nn.Sequential(*noise_layers)
        print(type(Identity()))
        print(f'after for cicyle , self.noise_layer{self.noise_layers}')

    def forward(self, encoded_and_cover):
        # random choose 
        # random_noise_layer = np.random.choice(self.noise_layers, 1)[0]
        "If you want to use specific noise, you can set it like this. " 
        "self.noise_layers[i](encoded_and_cover)"
        # print(random_noise_layer)
        ## TODO:
        # for single noisy 
        # return the last operation , it's customer
        return self.noise_layers[-1](encoded_and_cover)
    
        # return random_noise_layer(encoded_and_cover)
        # TODO:
        # combine nosiy ,random chose one noisy
        
        # random_noise_layer= np.random.choice(self.noise_layers, 1)[0]
        # print(f'random_noise_layer:{random_noise_layer}')
        # return random_noise_layer(encoded_and_cover)



