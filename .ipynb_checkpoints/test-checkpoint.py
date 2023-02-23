from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import *

def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))

points = genfromtxt("data.csv", delimiter=",")
point_test = genfromtxt("data.csv", delimiter=",")

x = []
for j in point_test :
    x.append(j[0])

m_test = np.arange(-10,10,1)
b_test = np.arange(-100,100,1)

w0, w1 = np.meshgrid(m_test, b_test)

w0 = w0.flatten()
w1 = w1.flatten()

error2d = []
for i in range(np.shape(w0.flatten())[0]) :
        error2d.append(compute_error_for_line_given_points(w1[i], w0[i], points))

print(np.shape(error2d))


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_trisurf(w0, w1, np.array(error2d), cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.show()
