import os
from collections import Counter
import numpy as np
import pandas as pd
import torch

from document_classification.ml.vocabulary import Vocabulary, SequenceVocabulary

class Vectorizer(object):
    def __init__(self, X_vocab, y_vocab):
        self.X_vocab = X_vocab
        self.y_vocab = y_vocab

    def vectorize(self, X):
        indices = [self.X_vocab.lookup_token(token) for token in X.split(" ")]
        indices = [self.X_vocab.begin_seq_index] + indices + \
            [self.X_vocab.end_seq_index]

        # Create vector
        X_length = len(indices)
        vector = np.zeros(X_length, dtype=np.int64)
        vector[:len(indices)] = indices

        return vector

    def unvectorize(self, vector):
        tokens = [self.X_vocab.lookup_index(index) for index in vector]
        X = " ".join(token for token in tokens)
        return X

    @classmethod
    def from_dataframe(cls, df, cutoff=0):

        # Create class vocab
        y_vocab = Vocabulary()
        for y in sorted(set(df.y)):
            y_vocab.add_token(y)

        # Get word counts
        word_counts = Counter()
        for X in df.X:
            for token in X.split(" "):
                word_counts[token] += 1

        # Create X vocab
        X_vocab = SequenceVocabulary()
        for word, word_count in word_counts.items():
            if word_count >= cutoff:
                X_vocab.add_token(word)

        return cls(X_vocab, y_vocab)

    @classmethod
    def from_serializable(cls, contents):
        X_vocab = SequenceVocabulary.from_serializable(contents['X_vocab'])
        y_vocab = Vocabulary.from_serializable(contents['y_vocab'])
        return cls(X_vocab=X_vocab, y_vocab=y_vocab)

    def to_serializable(self):
        return {'X_vocab': self.X_vocab.to_serializable(),
                'y_vocab': self.y_vocab.to_serializable()}