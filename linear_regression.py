import pandas as pd
import numpy as np


def calc_angular_coefficient(df_train):
    x_var = df_train['NU_NOTA_MT'].values
    y_var = df_train['NU_NOTA_CN'].values
    x_mean = np.mean(x_var)
    y_mean = np.mean(y_var)
    x_error = x_var - x_mean
    y_error = y_var - y_mean
    xy_error_sum = np.sum(x_error * y_error)
    x_quadratic_error = (x_var - x_mean) ** 2
    x_quadratic_error_sum = np.sum(x_quadratic_error)
    m = xy_error_sum / x_quadratic_error_sum
    return m


def calc_linear_coefficient(df_train, m):
    x_var = df_train['NU_NOTA_MT'].values
    y_var = df_train['NU_NOTA_CN'].values
    x_mean = np.mean(x_var)
    y_mean = np.mean(y_var)
    c = y_mean - m * x_mean
    return c


def line_equation(df_train, m, c):
    x_var = df_train['NU_NOTA_MT'].values
    line = m * x_var + c
    return line
