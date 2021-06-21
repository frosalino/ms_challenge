from data_input import data_input
from normalize import normalize
# from check_correlation import check_correlation
# from scatter_diagram import generate_scatter_diagram
import split_data as sd
import linear_regression as lr
import calc_error as error
from predict import predict


if __name__ == '__main__':
    df = data_input('data/raw/microdados_enem_2019.csv')
    df_norm = normalize(df)
    # check_correlation(df_norm)
    # generate_scatter_diagram(df_norm)
    msk = sd.create_mask(df_norm)
    df_train = sd.return_df_train(df_norm, msk)
    df_test = sd.return_df_test(df_norm, msk)
    m = lr.calc_angular_coefficient(df_train)
    c = lr.calc_linear_coefficient(df_train, m)
    # line = lr.line_equation(df_train, m, c)
    # generate_scatter_diagram_train(df_train)
    # mean_absolute_erro = error.mean_absolute_error(df_train, line)
    # print(f'MAE = {mean_absolute_erro}')
    # mean_squared_error = error.mean_squared_error(df_train, line)
    # print(f'RMSE = {mean_squared_error}')
    predict(df_test, m, c)
