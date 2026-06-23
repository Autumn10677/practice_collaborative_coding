import numpy as np
import matplotlib.pyplot as plt

# Plots the x^2 from -1 to 1
x_values = np.arange(-1, 1, 0.5)
y_values = x_values**2

# Autumn made a change
plt.plot(x_values, y_values)
plt.show()
