import argparse



def main():
    parser = argparse.ArgumentParser(description= 'test trained terminal')


    parser.add_argument('--options_file','-o', default='options-and-config.pickles',type  =str,
                        help = 'The file where tht simulation options are sorted')
    parser.add_argument('--checkpoint_file', '-c',required= True,type = str, help ='Model checkpoint file')

    parser.add_argument('--batch_size','-b', default= 12, type= int, help='The batch size')
    # parser.add_argument('--noise','-n',nargs = '*',action = N)


    args = parser.parse_args()


    print(f'optinos_file:{args.options_file},checkpoint-file:{args.checkpoint_file}, batch_size:{args.batch_size}')

# run main function
main()