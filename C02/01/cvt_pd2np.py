import pandas as pd
import numpy as np


if __name__ == "__main__":
    df = pd.read_csv('Module_02_Exercise_M02EX01/advertising.csv')
    data = df.to_numpy()
    tv = data[:, 0]
    ratio = data[:, 1]
    news = data[:, 2]
    sales = data[:, 3]

    print(f"Max: {max(sales)} - Index: {np.argmax(sales)}")
    print(f"Average of TV: {tv.mean()}")
    print(f"Sales >= 20: {(sales >= 20).sum()}")
    print(f"Average of Radio (Sales >= 15): {ratio[sales >= 15].mean()}")
    print(
        f"Sum of Sales (News >= News.mean()): {sales[news >= news.mean()].sum()}")

    A = sales.mean()
    scores = np.where(sales == A, "Average", sales)
    scores = np.where(sales > A, "Good", scores)
    scores = np.where(sales < A, "Bad", scores)
    print(scores[7:10])

    B = sales[np.argmin(np.abs(sales - A))]
    score = np.where(sales == B, "Average", sales)
    score = np.where(sales > B, "Good", score)
    score = np.where(sales < B, "Bad", score)
    print(score[7:10])
