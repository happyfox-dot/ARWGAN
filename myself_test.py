import argparse
from argparse import FileType
from collections.abc import Callable, Iterable, Sequence
import re
def parse_guassian_nosie(commond):
    matches = re.match(r'guassian\((\d+\.*\d*,\d+\.*\d*)\)',commond)
    # groups and group is not the same valus
    values = matches.groups()[0].split(',')
    mean = values[0]
    sigma = values[1]
    print(f'value is {values}')
    print(f'mean is {mean}')
    print(f'sigman is {sigma}')

class NoiseArg(argparse.Action):
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
    def __call__(self, parser, namespace, values,option_string = None):
        layers = []
        spilt_commands = values[0].split('+')
        for commands in spilt_commands:
            print(f'commands is {commands}')
            if commands[:len('guassian')]== 'guassian':
                layers.append(parse_guassian_nosie(commands))
            pass 
        # pass
        print('running __call__ function')
        # print(type(values))
        # print(f'value is :{values}')
        print(f'layers is{layers}')
        pass


def main():
    parser = argparse.ArgumentParser(description= 'test trained terminal')


    parser.add_argument('--options_file','-o', default='options-and-config.pickles',type  =str,
                        help = 'The file where tht simulation options are sorted')
    parser.add_argument('--checkpoint_file', '-c',required= True,type = str, help ='Model checkpoint file')

    parser.add_argument('--batch_size','-b', default= 12, type= int, help='The batch size')
    parser.add_argument('--noise','-n',nargs = '*',action = NoiseArg)


    args = parser.parse_args()


    print(f'optinos_file:{args.options_file},checkpoint-file:{args.checkpoint_file}, batch_size:{args.batch_size}')

# run main function
main()