import pandas as pd


def normalize(df):
    df_norm = df[(df.NU_NOTA_MT > 0) & (df.NU_NOTA_CN > 0) & (df.NU_NOTA_CH > 0) & (df.NU_NOTA_LC > 0)]
    return df_norm
