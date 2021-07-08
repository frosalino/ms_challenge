import pandas as pd
import numpy as np


def create_mask(df_norm, percentage=80):
    msk = np.random.rand(len(df_norm)) < percentage/100
    return msk


def return_df_train(df_norm, msk):
    df_train = df_norm[msk]
    return df_train


def return_df_test(df_norm, msk):
    df_test = df_norm[~msk]
    return df_test
