import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generator function for random walk
def random_walk():
    position = 0
    while True:
        step = np.random.choice([-1, 1])
        position += step
        yield position

# Set up the plot
fig, ax = plt.subplots()
xdata, ydata = [0], [0]
ln, = plt.plot(xdata, ydata, lw=2)
ax.set_xlim(0, 100)
ax.set_ylim(-50, 50)
ax.set_title('Animated Random Walk')
ax.set_xlabel('Step')
ax.set_ylabel('Position')

# Initialize the generator
walk_generator = random_walk()

# Update function for animation
def update(frame):
    xdata.append(xdata[-1] + 1)
    ydata.append(frame)
    ln.set_data(xdata, ydata)
    ax.set_xlim(0, len(xdata))
    ax.set_ylim(min(ydata) - 1, max(ydata) + 1)
    return ln,

# Create animation
ani = FuncAnimation(fig, update, frames=walk_generator, blit=True, interval=100)

# Show the plot
plt.show()