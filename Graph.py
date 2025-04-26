import math
import matplotlib.pyplot as plt
import numpy as np  # For generating smooth angle values

# Create 1000 points evenly spaced between 0 and 2π (360 degrees)
theta = np.linspace(0, 2 * math.pi, 1000)

# Basic circle (radius = 1)
x_basic = [math.cos(t) for t in theta]
y_basic = [math.sin(t) for t in theta]

plt.figure(figsize=(6, 6))
plt.plot(x_basic, y_basic, 'b-', linewidth=1)
plt.title("Basic Circle")
plt.grid(True)
plt.axis('equal') 
plt.show()

# Add harmonics to make the circle "flower-like"
x_circle = [math.cos(t) + 0.3 * math.cos(5 * t) for t in theta]
y_circle = [math.sin(t) + 0.3 * math.sin(7 * t) for t in theta]