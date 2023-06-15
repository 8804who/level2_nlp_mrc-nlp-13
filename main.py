import yaml
import os
from utils.Train import *

if __name__ == '__main__':
    with open('config.yaml') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    
    train(cfg)