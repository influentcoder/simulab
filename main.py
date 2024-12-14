import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Function to simulate random walk
def random_walk(n_steps):
    steps = np.random.choice([-1, 1], size=n_steps)
    return np.cumsum(steps)

# Function to update the plot
def update(val):
    n_steps = int(slider.val)
    walk = random_walk(n_steps)
    line.set_xdata(np.arange(n_steps))
    line.set_ydata(walk)
    ax.relim()
    ax.autoscale_view()
    plt.draw()

# Initial parameters
initial_steps = 100

# Create initial random walk
walk = random_walk(initial_steps)

# Create a figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
line, = ax.plot(np.arange(initial_steps), walk, lw=2)

# Add a slider for the number of steps
ax_steps = plt.axes([0.1, 0.1, 0.8, 0.03])
slider = Slider(ax_steps, 'Steps', 10, 1000, valinit=initial_steps, valstep=10)
slider.on_changed(update)

# Show the plot
plt.show()

#x = random_walk(100)
#print(x)