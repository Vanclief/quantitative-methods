import numpy as np


def calc_c(matrix, vector):
    print(matrix)
    print(vector)
    E = np.array(matrix) * np.array(vector)
    return E.sum()


def main():

    # Load files

    f = open("matrix.txt", "r")
    P = (np.matrix(f.read()))

    f = open("politic.txt", "r")
    R = (np.matrix(f.read()))

    # Init required variables

    size = P.shape[0]

    c = []

    for i in range(0, size):
        c.append(calc_c(P[i:i+1], R[i:i+1]))

    print(c)


if __name__ == "__main__":
    main()
