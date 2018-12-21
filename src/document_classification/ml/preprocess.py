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

def load_data(data_file):
    """Load data from CSV to Pandas DataFrame.
    """
    # Load into DataFrame
    df = pd.read_csv(data_file, header=0)
    ml_logger.info("\n==> 🍣 Raw data:")
    ml_logger.info(df.head())

    return df


def split_data(df, shuffle, train_size, val_size, test_size):
    """Split the data into train/val/test splits.
    """
    # Split by category
    by_category = collections.defaultdict(list)
    for _, row in df.iterrows():
        by_category[row.y].append(row.to_dict())
    ml_logger.info("\n==> 🛍️  Categories:")
    for category in by_category:
        ml_logger.info("{0}: {1}".format(category, len(by_category[category])))

    # Create split data
    final_list = []
    for _, item_list in sorted(by_category.items()):
        if shuffle:
            np.random.shuffle(item_list)
        n = len(item_list)
        n_train = int(train_size*n)
        n_val = int(val_size*n)
        n_test = int(test_size*n)

      # Give data point a split attribute
        for item in item_list[:n_train]:
            item['split'] = 'train'
        for item in item_list[n_train:n_train+n_val]:
            item['split'] = 'val'
        for item in item_list[n_train+n_val:]:
            item['split'] = 'test'

        # Add to final list
        final_list.extend(item_list)

    # df with split datasets
    split_df = pd.DataFrame(final_list)
    ml_logger.info("\n==> 🖖 Splits:")
    ml_logger.info(split_df["split"].value_counts())

    return split_df


def preprocess_text(text):
    """Basic text preprocessing.
    """
    text = ' '.join(word.lower() for word in text.split(" "))
    text = text.replace('\n', ' ')
    text = re.sub(r"[^a-zA-Z.!?_]+", r" ", text)
    text = text.strip()
    return text


def preprocess_data(df):
    df.X = df.X.apply(preprocess_text)
    ml_logger.info("\n==> 🚿 Preprocessing:")
    ml_logger.info(df.head())
    return df

