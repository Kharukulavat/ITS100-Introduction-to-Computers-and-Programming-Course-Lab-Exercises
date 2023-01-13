#ITS100 Lecture3 Libraries Lab3.1
import numpy as np
import matplotlib.pyplot as plt
from math import*
plt.xlim(-3*pi,3*pi)
x = np.arange(-3*pi,3*pi,0.1)
y1 = np.sin(x)
y2 = np.sin(x+0.5)
y3 = np.sin(x+1)
y4 = np.sin(x+1.5)

plt.plot(x, y1, color="pink", linestyle="solid")
plt.plot(x, y2, color ="orange", linestyle="dashdot")
plt.plot(x, y3, color="green", linestyle="dashed")
plt.plot(x, y4, color="blue", linestyle="dotted")
print(x)
print(y1)
print(y2)
print(y3)
print(y4)
plt.show()