import os
from threading import Thread

from document_classification.ml.utils import load_config, training_setup, training_operations


def train(config_filepath):
    """Asynchronously train a model.
    """

    # Load config and set up
    config = load_config(config_filepath=config_filepath)
    config = training_setup(config=config)

    # Asynchronous call
    thread = Thread(target=training_operations, args=(config,))
    thread.start()

    return config


def infer(config_filepath):
    """Predict using a model.
    """
    pass

