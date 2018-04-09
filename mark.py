import numpy as np


def transition(matrix, steps):
    for x in range(1, steps):
        matrix = matrix * matrix

    return matrix


def main():
    f = open("matrix.txt", "r")
    steps = int(input("Ingrese el numero de pasos: "))

    content = f.read()

    matrix = (np.matrix(content))

    matrix = transition(matrix, steps)

    print(matrix)


if __name__ == "__main__":
    main()
