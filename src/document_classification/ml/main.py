import os
from threading import Thread

from document_classification.config import ml_logger
from document_classification.ml.utils import setup, load_config
from document_classification.ml.preprocess import load_data, split_data, \
    preprocess_data
from document_classification.ml.dataset import Dataset, sample_data
from document_classification.ml.model import initialize_model
from document_classification.ml.trainer import Trainer

def train_operations():
    """ Operations for the training procedure.
    """

    # Load config
    config = load_config("/Users/goku/Documents/productionML/src/document_classification/ml/configs/train.yml")
    config = setup(config)

    # Load data
    df = load_data(data_file=config["data_file"])

    # Split data
    split_df = split_data(
        df=df, shuffle=config["shuffle"],
        train_size=config["train_size"],
        val_size=config["val_size"],
        test_size=config["test_size"])

    # Preprocessing
    preprocessed_df = preprocess_data(split_df)

    # Load dataset and vectorizer
    dataset = Dataset.load_dataset_and_make_vectorizer(preprocessed_df)
    dataset.save_vectorizer(config["vectorizer_file"])
    vectorizer = dataset.vectorizer

    # Sample checks
    sample_data(dataset=dataset)

    # Initializing model
    model = initialize_model(config=config, vectorizer=vectorizer)

    # Training
    trainer = Trainer(
        dataset=dataset, model=model, model_file=config["model_file"],
        save_dir=config["save_dir"], device=config["device"],
        shuffle=config["shuffle"], num_epochs=config["num_epochs"],
        batch_size=config["batch_size"], learning_rate=config["learning_rate"],
        early_stopping_criteria=config["early_stopping_criteria"])
    trainer.run_train_loop()

    # Testing
    y_pred, y_test = trainer.run_test_loop()

    # Save all results
    trainer.save_train_state()

def train_model():

    # Asynchronous call
    thread = Thread(target=train_operations)
    thread.start()

if __name__ == "__main__":
    train_model()


