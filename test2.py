import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Callback function to be called when the button is clicked
def on_button_click(event):
    ax.set_xlim(0, 1000)
    plt.draw()

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(-50, 50)

# Add a button
button_ax = plt.axes([0.8, 0.01, 0.1, 0.05])  # Position: [left, bottom, width, height]
button = Button(button_ax, 'Zoom Out')

# Connect the button to the callback function
button.on_clicked(on_button_click)

# Show the plot
plt.show()