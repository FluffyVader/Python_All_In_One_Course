#pip install matplotlib. this installs numpy
import numpy as np
import matplotlib.pyplot as plt
#create array from list
# a = np.array([])
#     the basic stuff
# a = np.zeros(3)
# print(a)

# a = np.zeros(5, dtype=int)
# print(a)

# creates 50 evenly spaced numbers from -2 to 2
numOfPoints = 50
xArray = np.linspace(-2, 2, numOfPoints)

def func(x):
    return 3 * x ** 2

def func2(x):
    return 3 * x ** 3

def func3(x):
    return 3 * x ** 4

yArray = np.zeros(numOfPoints)
yArray2 = np.zeros(numOfPoints)
yArray3 = np.zeros(numOfPoints)

for i in range(numOfPoints):
    yArray[i] = func(xArray[i])
    yArray2[i] = func2(xArray[i])
    yArray3[i] = func3(xArray[i])


plt.title("polynomials")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.plot(xArray, yArray)
plt.plot(xArray, yArray2)
plt.plot(xArray, yArray3)
plt.legend(['3x^2', '3x^3', '3x^4'])
plt.show()

# print(yArray)

#solve
# 3x + 2y = 5
# 2x + 4y = 6

# A = np.array([[3, 2], [2, 4]])
# H = np.array([5, 6])
# X = np.linalg.solve(A, H)

# print(X)