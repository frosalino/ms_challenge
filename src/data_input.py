import pandas as pd


def data_input(path):
    df = pd.read_csv(path, sep=';', encoding='ISO-8859-1')
    return df
