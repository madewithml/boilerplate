import os
import collections
import numpy as np
import pandas as pd
import random
import re
import time
import torch
from tqdm import tqdm
import uuid
import yaml

from document_classification.config import BASE_DIR, ml_logger
from document_classification.utils import create_dirs

def load_config(yaml_filepath):
    """Load the yaml config.
    """
    with open(yaml_filepath, 'r') as fp:
        config = yaml.load(fp)
    return config


def set_seeds(seed, cuda):
    """ Set Numpy and PyTorch seeds.
    """
    np.random.seed(seed)
    torch.manual_seed(seed)
    if cuda:
        torch.cuda.manual_seed_all(seed)


def generate_unique_id():
    """Generate a unique uuid
    preceded by a epochtime.
    """
    timestamp = int(time.time())
    unique_id = "{}_{}".format(timestamp, uuid.uuid1())

    return unique_id


def setup(config):
    # Set seeds
    set_seeds(seed=config["seed"], cuda=config["cuda"])

    # Generate experiment ID
    config["experiment_id"] = generate_unique_id()

    # Expand file paths
    config["save_dir"] = os.path.join(
        BASE_DIR, config["save_dir"], config["experiment_id"])
    create_dirs(config["save_dir"])
    config["vectorizer_file"] = os.path.join(
        config["save_dir"], config["vectorizer_file"])
    config["model_file"] = os.path.join(
        config["save_dir"], config["model_file"])

    # Check CUDA
    if not torch.cuda.is_available():
        config["device"] = False
    config["device"] = torch.device("cuda" if config["cuda"] else "cpu")

    config["learning_rate"] = np.float(config["learning_rate"])

    return config














