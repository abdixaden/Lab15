import math
import matplotlib.pyplot as plt
import numpy as np  # For generating smooth angle values

# Create 1000 points evenly spaced between 0 and 2π (360 degrees)
theta = np.linspace(0, 2 * math.pi, 1000)

# Basic circle (radius = 1)
x_basic = [math.cos(t) for t in theta]
y_basic = [math.sin(t) for t in theta]

