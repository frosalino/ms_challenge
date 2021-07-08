import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error


def mae(df_train, line):
    y_var = df_train['NU_NOTA_CN'].values
    MAE = mean_absolute_error(y_var, line)
    return MAE


def rmse(df_train, line):
    y_var = df_train['NU_NOTA_CN'].values
    RMSE = np.sqrt(mean_squared_error(y_var, line))
    return RMSE
