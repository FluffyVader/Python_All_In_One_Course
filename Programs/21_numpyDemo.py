#pip install matplotlib. this installs numpy
import numpy as np

#create array from list
# a = np.array([])
#     the basic stuff
# a = np.zeros(3)
# print(a)

# a = np.zeros(5, dtype=int)
# print(a)

# creates 20 evenly spaced numbers from -3 to 3
# numOfPoints = 3
# xArray = np.linspace(-3, 3, numOfPoints)
# print(xArray)

# def func(x):
#     return x**3

# yArray = np.zeros(numOfPoints)
# for i in range(numOfPoints):
#     yArray[i] = func(xArray[i])

# print(yArray)

#solve
# 3x + 2y = 5
# 2x + 4y = 6

# A = np.array([[3, 2], [2, 4]])
# H = np.array([5, 6])
# X = np.linalg.solve(A, H)

# print(X)