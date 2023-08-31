#!/bin/bash

#  python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Median_filter(5.0)'
#    python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Median_filter()'
#    python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Median_filter(5.0)'
echo  "median_filter kernel_size = 5"
python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Median_filter(5)'
echo "salt_papper ratio = 0.1"
python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'sp(0.1)'
echo "random bri, 0.8 - 1.2"
python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'random_bri(0.8,1.2)'
echo "random contrast, 0.8 - 1.2"
python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'random_constr(0.8,1.2)'
echo "random saturation, 0.8 - 1.2"
python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'random_sat(0.8,1.2)'
echo "random hue, 0.8 - 1.2"
python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'random_hue(-0.1,0.1)'