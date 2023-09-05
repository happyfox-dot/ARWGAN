#jepeg
echo "jpege, factor = 10" > output.txt
python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Jpeg(10.0)' >> output.txt

echo "jpege, factor = 30" >> output.txt
python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Jpeg(30.0)' >> output.txt

echo "jpege, factor = 50" >> output.txt
python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Jpeg(50.0)' >> output.txt

echo "jpege, factor = 70" >> output.txt
python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Jpeg(70.0)' >> output.txt
echo "jpege, factor = 90" >> output.txt
python test.py -o ./pretrain/options-and-config.pickle -c ./pretrain/checkpoints/ARWGAN.pyt -s /mnt/chengxin/Datasets/DUTS/DUTS-TE/Std-Image-30/ -n 'Jpeg(90.0)' >> output.txt


