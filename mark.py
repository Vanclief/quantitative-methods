import numpy as np # I want to check my solution with numpy

def transition(matrix, steps):
    return matrix * matrix




matrix = (np.matrix('0.8 0.2; 0.6 0.4'))

matrix = transition(matrix, 2)

print(matrix)




# mx = np.matrix(x)
# my = np.matrix(y)
