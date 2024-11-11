import numpy as np


def create_data():
    data = np.loadtxt("play_tennis_data.txt", delimiter=",", dtype=str)
    return data


def train_naive_bayes(data):
    labels, counts = np.unique(data[:, -1], return_counts=True)
    prior_prob = counts / sum(counts)
    con_prob_list = [None for _ in range(data.shape[1]-1)]
    features_list = con_prob_list.copy()

    for f in range(data.shape[1]-1):
        features_list[f] = np.unique(data[:, f])
        con_prob_fea_arr = np.zeros((len(labels), len(features_list[f])))

        for row in range(len(con_prob_fea_arr)):
            for col in range(len(con_prob_fea_arr[0])):
                con_prob_fea_arr[row, col] = len(np.nonzero((data[:, f] == features_list[f][col]) & (
                    data[:, -1] == labels[row]))[0])/counts[row]
        con_prob_list[f] = con_prob_fea_arr

    return labels, prior_prob, con_prob_list, features_list


def get_index(x, features_list):
    index = [None for _ in range(len(x))]

    for _ in range(len(x)):
        index[_] = np.nonzero(x[_] == features_list[_])[0]

    return index


def predict_play_tennis(x, features_list, labels, prior_prob, con_prob_list):
    index = get_index(x, features_list)

    p = [None for _ in range(len(prior_prob))]
    for l in range(len(p)):
        p[l] = prior_prob[l]
        for f in range(len(index)):
            p[l] *= con_prob_list[f][l, index[f]]
        print(f"{labels[l]}: {p[l]}")

    print("\nResult: ", labels[np.argmax(p)])


def main():
    data = create_data()
    x = ['Sunny', 'Cool', 'High', 'Strong']

    labels, prior_prob, con_prob_list, features_list = train_naive_bayes(data)
    predict_play_tennis(x, features_list, labels, prior_prob, con_prob_list)

    # print(con_prob_list)


if __name__ == "__main__":
    main()
