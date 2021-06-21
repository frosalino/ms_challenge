import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def check_correlation(df_norm):
    df_grades = df_norm[['NU_NOTA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC']]
    df_grades_corr = df_grades.corr()
    labels = ['MATEMÁTICA', 'CIÊNCIAS NATUREZA', 'CIÊNCIÂS HUMANAS', 'LINGUAGENS']
    fig, ax = plt.subplots(dpi=180)
    sns.heatmap(df_grades_corr,
                cmap='Wistia',
                annot=True,
                ax=ax,
                annot_kws={'size': 8},
                xticklabels=labels,
                yticklabels=labels)
    plt.show()
