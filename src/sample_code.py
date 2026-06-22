import numpy as np
import matplotlib.pyplot as plt

# Changed end arguments of 'np.arange'
x_values = np.arange(0, 1, 0.1)
y_values = x_values**2

plt.plot(x_values, y_values)
plt.show()
