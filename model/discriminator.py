import torch
import torch.nn as nn
from options import HiDDenConfiguration
from model.Dense_block import Bottleneck


class Discriminator(nn.Module):
    def conv1(self, in_channel, out_channel):
        return nn.Conv2d(in_channels=in_channel,
                         out_channels=out_channel,
                         stride=1,
                         kernel_size=7,
                         padding=3)

    def conv2(self, in_channel, out_chanenl):
        return nn.Conv2d(in_channels=in_channel,
                         out_channels=out_chanenl,
                         stride=1,
                         kernel_size=3,
                         padding=1)

    def __init__(self, config: HiDDenConfiguration):
        super(Discriminator, self).__init__()
        self.channels = config.discriminator_channels

        self.first_layer = nn.Sequential(self.conv2(3, self.channels),
                                         nn.BatchNorm2d(self.channels),
                                         nn.LeakyReLU(inplace=True))

        self.second_layer = nn.Sequential(self.conv2(self.channels, self.channels),
                                          nn.BatchNorm2d(self.channels),
                                          nn.LeakyReLU(inplace=True))

        self.third_layer = nn.Sequential(self.conv2(self.channels * 2, self.channels),
                                         nn.BatchNorm2d(self.channels),
                                         nn.LeakyReLU(inplace=True))

        self.fourth_layer = nn.Sequential(self.conv2(self.channels * 3, self.channels),
                                          nn.BatchNorm2d(self.channels),
                                          nn.LeakyReLU(inplace=True))

        self.Dense_block1 = Bottleneck(self.channels, self.channels)
        self.Dense_block2 = Bottleneck(self.channels * 2, self.channels)
        self.Dense_block3 = Bottleneck(self.channels * 3, self.channels)
        self.fivth_layer = nn.Sequential(self.conv2(self.channels, config.message_length),
                                         nn.BatchNorm2d(config.message_length),
                                         nn.LeakyReLU(inplace=True))

        self.average = nn.AdaptiveAvgPool2d(output_size=(1, 1))
        self.linear = nn.Linear(config.message_length, 1)

    def forward(self, image):
        feature0 = self.first_layer(image)
        feature1 = self.second_layer(feature0)
        feature2 = self.third_layer(torch.cat([feature0, feature1], dim=1))
        feature3 = self.fourth_layer(torch.cat([feature0, feature1, feature2], dim=1))
        x = self.fivth_layer(feature3)

        X = self.average(x)
        X.squeeze_(3).squeeze_(2)
        X = self.linear(X)
        return X
# import torch.nn as nn
# from options import HiDDenConfiguration
# from model.conv_bn_relu import ConvBNRelu

# class Discriminator(nn.Module):
#     """
#     Discriminator network. Receives an image and has to figure out whether it has a watermark inserted into it, or not.
#     """
#     def __init__(self, config: HiDDenConfiguration):
#         super(Discriminator, self).__init__()

#         layers = [ConvBNRelu(3, config.discriminator_channels)]
#         for _ in range(config.discriminator_blocks-1):
#             layers.append(ConvBNRelu(config.discriminator_channels, config.discriminator_channels))

#         layers.append(nn.AdaptiveAvgPool2d(output_size=(1, 1)))
#         self.before_linear = nn.Sequential(*layers)
#         self.linear = nn.Linear(config.discriminator_channels, 1)

#     def forward(self, image):
#         X = self.before_linear(image)
#         # the output is of shape b x c x 1 x 1, and we want to squeeze out the last two dummy dimensions and make
#         # the tensor of shape b x c. If we just call squeeze_() it will also squeeze the batch dimension when b=1.
#         X.squeeze_(3).squeeze_(2)
#         X = self.linear(X)
#         # X = torch.sigmoid(X)
#         return X