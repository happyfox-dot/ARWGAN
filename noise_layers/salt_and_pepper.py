import torch
import torch.nn as nn
import numpy as np

class Salt_and_Pepper(nn.Module):
    def __init__(self,ratio):
        super(Salt_and_Pepper, self).__init__()
        self.ratio=float(ratio)
        self.device=torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')


    def forward(self, noise_and_cover):
        encoded_image=noise_and_cover[0]
        B,C,H,W=encoded_image.size()
        mask = np.random.choice((0, 1, 2), size=(B,1,H,W), p=[self.ratio, self.ratio, 1 - 2 * self.ratio])
        mask=torch.tensor(np.repeat(mask,C, axis=1),device=self.device)
        encoded_image[mask==0]=-1
        encoded_image[mask==1]=1
        noise_and_cover[0]=encoded_image
        return noise_and_cover



# import numpy as np
# import torch
# import torch.nn as nn


# class Salt_and_Pepper(nn.Module):
#     def __init__(self, ratio: float):
#         super().__init__()
#         self.ratio = ratio

#     def forward(self, image: torch.Tensor):
#         batch_size, channels, height, width = image.shape
#         mask = np.random.choice([0, 1, 2], size=(batch_size, 1, height, width),
#                                 p=[self.ratio, self.ratio, (1-2*self.ratio)])
#         mask = torch.from_numpy(mask).to(image.device).repeat(1, channels, 1, 1)
#         image[mask == 0] = 0.
#         image[mask == 1] = 1.
#         return image