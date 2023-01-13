#ITS100 Lecture3 Libraries Lab3.2
import numpy as np
import matplotlib.pyplot as plt
from math import *
x = np.arange(0.1,10.1,0.1)
y = (1+x)/np.sqrt(x)
plt.plot(x, y, color="purple", linewidth=2, linestyle="dotted")
print(x)
print(y)
plt.show()