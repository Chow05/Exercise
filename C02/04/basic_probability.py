import numpy as np


if __name__ == "__main__":
    x = np.asarray([-2, -5, -11, 6, 4, 15, 9])
    y = np.asarray([4, 25, 121, 36, 16, 225, 81])

    print("Mean : ", np.mean(x))
    print("Median : ", np.median(x))
    print("Std : ", np.std(x))
    print("Variance : ", np.var(x))
    print("Correlation: ", np.corrcoef(x, y)[0][1])
