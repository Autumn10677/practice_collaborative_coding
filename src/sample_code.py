import numpy as np
import matplotlib.pyplot as plt

# Plots the x^2 from -2 to 2 (Catriona changed the range to -1 to 1)
x_values = np.arange(-2, 2, 0.5)
y_values = x_values**2

# Autumn made a change
plt.plot(x_values, y_values)
plt.show()
