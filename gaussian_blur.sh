#!/bin/bash

#  python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Median_filter(5.0)'
#    python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Median_filter()'
#    python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Median_filter(5.0)'


#jepeg
echo "jpege, factor = 10" > output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Jpeg(10.0)' >> output.txt

echo "jpege, factor = 30" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Jpeg(30.0)' >> output.txt

echo "jpege, factor = 50" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Jpeg(50.0)' >> output.txt

echo "jpege, factor = 70" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Jpeg(70.0)' >> output.txt
echo "jpege, factor = 90" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Jpeg(90.0)' >> output.txt



# gaussain blur
echo  "gaussain blur , kernel = 7" >> output.txt
echo "sigma = 0.1" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'gaussian(7,0.1)' >> output.txt
echo "ssigma = 0.5" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'gaussian(7,0.5)' >> output.txt
echo "sigma= 1.0" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'gaussian(7,1.0)' >> output.txt
echo "sigma= 1.5" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'gaussian(7,1.5)' >> output.txt
echo "sigma = 2.0" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'gaussian(7,2.0)' >> output.txt
echo "sigma = 2.5" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'gaussian(7,2.5)' >> output.txt
echo "sigma = 3.0" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'gaussian(7,3.0)' >> output.txt

#gaussain noisy 
echo  "gaussain noisy , sigma = [0.01,0.02 , 0.03, 0.04,0.05]"  >> output.txt
echo "sigma = 0.01" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Gaussian_noise(0,0.01)' >> output.txt
echo "ssigma = 0.02" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Gaussian_noise(0,0.02)' >> output.txt
echo "sigma= 0.03" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Gaussian_noise(0,0.03)' >> output.txt
echo "sigma= 0.04" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Gaussian_noise(0,0.04)' >> output.txt
echo "sigma = 0.05" >> output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Gaussian_noise(0,0.05)' >> output.txt

# rescale 
# echo "rescale ,factor =[0.5, 0.75,1., 1.25, 1.5, 2.0]" >> output.txt

# echo "factor = 0.5" >> output.txt
# python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'resize(0.5,0.5)' >> output.txt
# echo "factor = 0.75" >> output.txt
# python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'resize(0.75,0.75)' >> output.txt
# echo "factor = 1." >> output.txt
# python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'resize(1.0,1.0)' >> output.txt
# echo "factor = 1.25" >> output.txt
# python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'resize(1.25,1.25)' >> output.txt
# echo "factor= 1.5 " >> output.txt
# python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'resize(1.5,1.5)' >> output.txt
# echo "factor= 2.0" >> output.txt
# python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'resize(2.0,2.0)' >> output.txt

# rst ,
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'rst' >> output.txt
