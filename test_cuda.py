import torch
import os 
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

print(torch.cuda.is_available())