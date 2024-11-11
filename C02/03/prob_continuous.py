import numpy as np


def create_data():
    data = np.loadtxt("iris_data.txt", delimiter=",", dtype=str)
    return data


def train_gaussian_naive_bayes(data):
    labels, counts = np.unique(data[:, -1], return_counts=True)
    prior_prob = counts / sum(counts)
    con_prob_list = [None for _ in range(data.shape[1]-1)]

    for f in range(data.shape[1]-1):
        mean_sigma2_arr = np.zeros((len(labels), 2))

        for label in range(len(labels)):
            mean = data[:, f][np.nonzero(
                data[:, -1] == labels[label])].astype(float).mean()
            sigma2 = data[:, f][np.nonzero(
                data[:, -1] == labels[label])].astype(float).var()
            mean_sigma2_arr[label] = [mean, sigma2]

        con_prob_list[f] = mean_sigma2_arr

    return labels, prior_prob, con_prob_list


def gauss(x, mean, sigma):
    result = (1.0 / (np.sqrt(2*np.pi*sigma))) \
        * (np.exp(-(float(x) - mean) ** 2 / (2 * sigma)))
    return result


def predict_iris(x, labels, prior_prob, con_prob_list):
    p = [None for _ in range(len(prior_prob))]

    for l in range(len(p)):
        p[l] = prior_prob[l]
        for f in range(len(con_prob_list)):
            p[l] *= gauss(x[f], con_prob_list[f][l][0], con_prob_list[f][l][1])
        print(f"{labels[l]}: {p[l]}")

    print("\nResult: ", labels[np.argmax(p)])


def main():
    x = [4.9, 3.1, 1.5, 0.1]
    data = create_data()

    labels, prior_prob, con_prob_list = train_gaussian_naive_bayes(data)
    predict_iris(x, labels, prior_prob, con_prob_list)
    # print(con_prob_list)


if __name__ == "__main__":
    main()
