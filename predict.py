import pandas as pd
import random as r


def predict(df_test, m, c):
    student = r.randint(0, len(df_test))
    ofx_var = df_test['NU_NOTA_MT'].values
    ofy_var = df_test['NU_NOTA_CN'].values
    true_x = ofx_var[student]
    true_y = ofy_var[student]
    prediction = m * true_x + c

    print(f'NOTA MATEÁTICA REAL: {true_x}')
    print(f'NOTA CIÊNCIAS DA NATUREZA REAL: {true_y}')
    print(f'PREVISÃO DO ALGORÍTIMO: {prediction}')