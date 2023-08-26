import pickle
import os

file_path = r'pretrain/options-and-config.pickle'

def load_options(options_file_name):
    """ Loads the training, model, and noise configurations from the given folder """
    with open(os.path.join(options_file_name), 'rb') as f:
        train_options = pickle.load(f)
        noise_config = pickle.load(f)
        
        net_config = pickle.load(f)
        # for backward-capability. Some models were trained and saved before .enable_fp16 was added
        if not hasattr(net_config, 'enable_fp16'):
            setattr(net_config, 'enable_fp16', False)

    return train_options, net_config, noise_config

_, net_config , _ = load_options(file_path)

# 打印这个对象中的value

print(net_config.__dict__)