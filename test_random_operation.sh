echo "Median_blur, kernel" > rst_output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Median_filter(5)' >> rst_output.txt

echo "salt_and_pepper" >> rst_output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'sp(0.1)' >> rst_output.txt

echo "brightness" >> rst_output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'random_bri(0.8,1.2)' >> rst_output.txt

echo "contrast" >> rst_output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'random_constr(0.8,1.2)' >> rst_output.txt
echo "saturation" >> rst_output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'random_sat(0.8,1.2)' >> rst_output.txt
echo "hue" >> rst_output.txt
python test.py -o runs/train_arwgan_2023.09.04--23-18-18/options-and-config.pickle -c runs/train_arwgan_2023.09.04--23-18-18/checkpoints/train_arwgan--epoch-285.pyt  -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'random_hue(-0.1,0.1)' >> rst_output.txt
