import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

# Function to simulate simple random walk
def simple_random_walk(n_steps):
    steps = np.random.choice([-1, 1], size=n_steps)
    return np.cumsum(steps)

# Function to simulate Gaussian random walk
def gaussian_random_walk(n_steps):
    steps = np.random.normal(loc=0, scale=1, size=n_steps)
    return np.cumsum(steps)

# Function to simulate Levy flight
def levy_flight(n_steps):
    steps = np.random.standard_cauchy(size=n_steps)
    return np.cumsum(steps)

# Function to simulate Brownian motion
def brownian_motion(n_steps):
    steps = np.random.normal(loc=0, scale=1, size=n_steps)
    return np.cumsum(steps)

# Function to simulate Self-Avoiding Random Walk
def self_avoiding_random_walk(n_steps):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    path = [(0, 0)]
    for _ in range(n_steps - 1):
        x, y = path[-1]
        np.random.shuffle(directions)
        for dx, dy in directions:
            new_pos = (x + dx, y + dy)
            if new_pos not in path:
                path.append(new_pos)
                break
        else:
            break  # No valid move found, end the walk
    return np.array(path).T

# Function to update the plot
def update(val):
    n_steps = int(slider.val)
    algorithm = radio.value_selected
    if algorithm == 'Simple':
        walk = simple_random_walk(n_steps)
        line.set_xdata(np.arange(n_steps))
        line.set_ydata(walk)
    elif algorithm == 'Gaussian':
        walk = gaussian_random_walk(n_steps)
        line.set_xdata(np.arange(n_steps))
        line.set_ydata(walk)
    elif algorithm == 'Levy':
        walk = levy_flight(n_steps)
        line.set_xdata(np.arange(n_steps))
        line.set_ydata(walk)
    elif algorithm == 'Brownian':
        walk = brownian_motion(n_steps)
        line.set_xdata(np.arange(n_steps))
        line.set_ydata(walk)
    elif algorithm == 'Self-Avoiding':
        walk = self_avoiding_random_walk(n_steps)
        line.set_xdata(walk[0])
        line.set_ydata(walk[1])
    ax.relim()
    ax.autoscale_view()
    plt.draw()

# Initial parameters
initial_steps = 100

# Create initial random walk
walk = simple_random_walk(initial_steps)

# Create a figure and axis with a larger size
fig, ax = plt.subplots(figsize=(15, 12))
plt.subplots_adjust(left=0.1, bottom=0.35)
line, = ax.plot(np.arange(initial_steps), walk, lw=2)

# Add a slider for the number of steps
ax_steps = plt.axes([0.1, 0.2, 0.8, 0.03])
slider = Slider(ax_steps, 'Steps', 10, 1000, valinit=initial_steps, valstep=10)
slider.on_changed(update)

# Add radio buttons for selecting the algorithm
ax_radio = plt.axes([0.1, 0.05, 0.8, 0.1])
radio = RadioButtons(ax_radio, ('Simple', 'Gaussian', 'Levy', 'Brownian', 'Self-Avoiding'))
radio.on_clicked(update)

# Show the plot
plt.show()