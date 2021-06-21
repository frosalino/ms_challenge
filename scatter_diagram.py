import pandas as pd
import matplotlib.pyplot as plt


def generate_scatter_diagram(df):
    dep_var = df['NU_NOTA_MT'].values
    ind_var = df['NU_NOTA_CN'].values
    plt.scatter(dep_var, ind_var, label='NOTA_CN(NOTA_MT)')
    plt.xlabel('NOTAS MATEMÁTICA')
    plt.ylabel('NOTAS CIÊNCIAS DA NATUREZA')
    plt.legend()


def generate_scatter_diagram_train(df_train):
    x_var = df_train['NU_NOTA_MT'].values
    y_var = df_train['NU_NOTA_CN'].values
    plt.scatter(x_var, y_var, label='NOTAS')
    plt.plot(x_var, line, label='AJUSTE LINEAR', color='red')
    plt.xlabel('NOTA MATEMÁTICA')
    plt.ylabel('NOTA CIÊNCIAS DA NATUREZA')
    plt.legend()
