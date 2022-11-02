from detoxify import Detoxify
import pandas as pd


def classify_sentence(text):
    return Detoxify('original').predict(text)
