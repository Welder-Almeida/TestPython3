import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Function to be rotated
def f(x):
    return np.sin(x) + 2  # Example function

# Limits of integration
a, b = 0, np.pi  # From x = 0 to x = π

# Compute volume using integral calculus
volume, _ = quad(lambda x: np.pi * (f(x) ** 2), a, b)

# Generate data for visualization
x = np.linspace(a, b, 1000)
y = f(x)

# Plot the function and the solid of revolution
fig, ax = plt.subplots(figsize=(6, 6))

ax.plot(x, y, color='blue', label=r'$f(x) = \sin(x) + 2$')
ax.fill_between(x, y, color='lightblue', alpha=0.6)

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
ax.set_title("Solid of Revolution using Integral Calculus")
ax.legend()
ax.grid(True)

# Show the calculated volume
print(f"Computed Volume: {volume:.4f} cubic units")

plt.show()
