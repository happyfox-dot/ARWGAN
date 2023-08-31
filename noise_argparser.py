import argparse
import re
from noise_layers.cropout import Cropout
from noise_layers.crop import Crop
from noise_layers.identity import Identity
from noise_layers.dropout import Dropout
from noise_layers.resize import Resize
from noise_layers.quantization import Quantization
from noise_layers.jpeg_compression import JpegCompression
from noise_layers.gaussian import Gaussian_blur
from noise_layers.jpeg import Jpeg
from noise_layers.salt_and_pepper import Salt_and_Pepper
from noise_layers.Gaussian_noise import Gaussian_Noise
from noise_layers.Median_filter import Median_filter
# adjust hue
from noise_layers.Adjust_hue import random_hue
from noise_layers.Adjust_contrast import random_constrast
from noise_layers.Brightness import random_br
from noise_layers.Saturation import random_sat
from noise_layers.grid_crop import grid_crop


def parse_pair(match_groups):
    heights = match_groups[0].split(',')
    hmin = float(heights[0])
    hmax = float(heights[1])
    widths = match_groups[1].split(',')
    wmin = float(widths[0])
    wmax = float(widths[1])
    return (hmin, hmax), (wmin, wmax)


def parse_crop(crop_command):
    matches = re.match(r'crop\(\((\d+\.*\d*,\d+\.*\d*)\),\((\d+\.*\d*,\d+\.*\d*)\)\)', crop_command)
    (hmin, hmax), (wmin, wmax) = parse_pair(matches.groups())
    return Crop((hmin, hmax), (wmin, wmax))

def parse_cropout(cropout_command):
    matches = re.match(r'cropout\(\((\d+\.*\d*,\d+\.*\d*)\),\((\d+\.*\d*,\d+\.*\d*)\)\)', cropout_command)
    (hmin, hmax), (wmin, wmax) = parse_pair(matches.groups())
    return Cropout((hmin, hmax), (wmin, wmax))


def parse_dropout(dropout_command):
    matches = re.match(r'dropout\((\d+\.*\d*,\d+\.*\d*)\)', dropout_command)
    ratios = matches.groups()[0].split(',')
    keep_min = float(ratios[0])
    keep_max = float(ratios[1])
    return Dropout((keep_min, keep_max))

def parse_resize(resize_command):
    matches = re.match(r'resize\((\d+\.*\d*,\d+\.*\d*)\)', resize_command)
    ratios = matches.groups()[0].split(',')
    min_ratio = float(ratios[0])
    max_ratio = float(ratios[1])
    return Resize(resize_ratio_range = (min_ratio, max_ratio))
# gussian blur
def parse_gaussian(gaussian_commond):
    matches=re.match(r'gaussian\((\d+\.*\d*,\d+\.*\d*)\)',gaussian_commond)
    values=matches.groups()[0].split(',')
    kernel=values[0]
    sigma=values[1]
    return Gaussian_blur(kernel,sigma)
# 
# using jpge
def parse_jpeg(jpeg_commond):
    matches=re.match(r'Jpeg\((\d+\.*\d*)\)',jpeg_commond)
    factor = matches.groups()[0]
    print(f'factor is {factor}')
    return Jpeg(factor)

def parse_s_and_p(S_and_P_commond):
    matches=re.match(r'sp\((\d+\.*\d*)\)',S_and_P_commond)
    ratio=matches.groups()[0]
    return Salt_and_Pepper(ratio)
# gussia noise
def parse_gaussian_nosie(Gaussian_noise_commond):
    matches=re.match(r'Gaussian_noise\((\d+\.*\d*,\d+\.*\d*)\)',Gaussian_noise_commond)
    values = matches.groups()[0].split(',')
    mean = values[0]
    sigma = values[1]
    return Gaussian_Noise(mean,sigma)

def parse_Median_filter(Median_filter_commond):
    matches=re.match(r'Median_filter\((\d+\.*\d*)\)',Median_filter_commond)
    values=matches.groups()[0]
    return Median_filter(values)

# ##############################
####### add experiment 
def parse_Adjust_hue(Adjust_hue_commond):
    matches=re.match(r'random_hue\((\-\d+\.*\d*,\d+\.*\d*)\)',Adjust_hue_commond)
    values = matches.groups()[0].split(',')
    a =values[0]
    b  = values[1]
    return random_hue(a,b)
#  调整对比度
def parse_Adjust_contrast(Adjust_contrast_commond):
    matches=re.match(r'random_constr\((\d+\.*\d*,\d+\.*\d*)\)',Adjust_contrast_commond)
    values = matches.groups()[0].split(',')
    a =values[0]
    b  = values[1]
    return random_constrast(a,b)

def parse_random_brightness(Adjust_contrast_commond):
   
    matches=re.match(r'random_bri\((\d+\.*\d*,\d+\.*\d*)\)',Adjust_contrast_commond)
    values = matches.groups()[0].split(',')
    a =values[0]
    b  = values[1]
   
    return random_br(a,b)

def parse_random_saturation(Adjust_contrast_commond):
    matches=re.match(r'random_sat\((\d+\.*\d*,\d+\.*\d*)\)',Adjust_contrast_commond)
    values = matches.groups()[0].split(',')
    a =values[0]
    b  = values[1]
    return random_sat(a,b)

#########################################
def parse_grid_crop(grid_crop_commond):
    matches=re.match(r'grid_crop\((\d+\.*\d*)\)',grid_crop_commond)
    values=matches.groups()[0]
    return grid_crop(values)

class NoiseArgParser(argparse.Action):
    def __init__(self,
                 option_strings,
                 dest,
                 nargs=None,
                 const=None,
                 default=None,
                 type=None,
                 choices=None,
                 required=False,
                 help=None,
                 metavar=None):
        argparse.Action.__init__(self,
                                 option_strings=option_strings,
                                 dest=dest,
                                 nargs=nargs,
                                 const=const,
                                 default=default,
                                 type=type,
                                 choices=choices,
                                 required=required,
                                 help=help,
                                 metavar=metavar,
                                 )

    @staticmethod
    def parse_cropout_args(cropout_args):
        pass

    @staticmethod
    def parse_dropout_args(dropout_args):
        pass

    def __call__(self, parser, namespace, values,
                 option_string=None):

        layers = []
        split_commands = values[0].split('+')

        for command in split_commands:
            # remove all whitespace
            command = command.replace(' ', '')
            # 比较前 n 个字符
            # 匹配的形式是 cropout(value1, value2)
            # valeu = 1.0
            if command[:len('cropout')] == 'cropout':
                layers.append(parse_cropout(command))
            elif command[:len('crop')] == 'crop':
                layers.append(parse_crop(command))
            elif command[:len('dropout')] == 'dropout':
                layers.append(parse_dropout(command))
            elif command[:len('resize')] == 'resize':
                layers.append(parse_resize(command))
            elif command[:len('jpeg')] == 'jpeg':
                layers.append('JpegPlaceholder')
            elif command[:len('quant')] == 'quant':
                layers.append('QuantizationPlaceholder')
            elif command[:len('gaussian')] =='gaussian':
                layers.append(parse_gaussian(command))
            elif command[:len('Jpeg')]=='Jpeg':
                layers.append(parse_jpeg(command))
            elif command[:len('sp')]=='sp':
                layers.append(parse_s_and_p(command))
            elif command[:len('Gaussian_noise')]=='Gaussian_noise':
                layers.append(parse_gaussian_nosie(command))
            elif command[:len('Median_filter')]=='Median_filter':
                layers.append(parse_Median_filter(command))
            elif command[:len('random_hue')]=='random_hue':
                layers.append(parse_Adjust_hue(command))
            elif command[:len('random_constr')]=='random_constr':
                layers.append(parse_Adjust_contrast(command))
            elif command[:len('random_bri')] == 'random_bri':
                layers.append(parse_random_brightness(command))
            elif command[:len('random_sat')] =='random_sat':
                layers.append(parse_random_saturation(command))
            elif command[:len('grid_crop')]=='grid_crop':
                layers.append(parse_grid_crop(command))
            elif command[:len('identity')] == 'identity':
                # We are adding one Identity() layer in Noiser anyway
                pass
            else:
                # if string is wrong , print this message 
                raise ValueError('Command not recognized: \n{}'.format(command))
        setattr(namespace, self.dest, layers)
