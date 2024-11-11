import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


if __name__ == "__main__":
    data = pd.read_csv("Module_02_Exercise_M02EX04/advertising.csv")

    data_corr_coef = data.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(data_corr_coef, annot=True, fmt=".2f", linewidth=.5)
    plt.show()
