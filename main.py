import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
import yfinance as yf
from datetime import datetime, timedelta

# Function to fetch historical stock price data
def fetch_historical_data(ticker, start_date):
    stock_data = yf.download(ticker, start=start_date)
    return stock_data['Close']

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

# Function to simulate future stock prices using a random walk
def simulate_future_prices(start, n_steps):
    steps = np.random.normal(0, scale=1, size=n_steps)
    future_prices = start + np.cumsum(steps)
    return future_prices

# Function to update the plot
def update(val):
    n_steps = int(slider.val)
    algorithm = radio.value_selected
    if algorithm == 'Simple':
        walk = simple_random_walk(n_steps)
    elif algorithm == 'Gaussian':
        walk = gaussian_random_walk(n_steps)
    elif algorithm == 'Levy':
        walk = levy_flight(n_steps)
    elif algorithm == 'Brownian':
        walk = brownian_motion(n_steps)
    elif algorithm == 'Self-Avoiding':
        walk = self_avoiding_random_walk(n_steps)
        line.set_xdata(walk[0])
        line.set_ydata(walk[1])
    else:
        line.set_xdata(np.arange(n_steps))
        line.set_ydata(walk)
    ax.relim()
    ax.autoscale_view()
    plt.draw()

    # Fetch historical data and simulate future prices
    ticker = 'AAPL'
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    historical_prices = fetch_historical_data(ticker, start_date)
    future_prices = simulate_future_prices(historical_prices.iloc[-1][ticker], n_steps)
    
    # Combine historical and future prices
    combined_prices = np.concatenate([historical_prices['AAPL'].values, future_prices])
    combined_dates = pd.date_range(start=historical_prices.index[0], periods=len(combined_prices))
    
    # Update the plot
    line.set_xdata(combined_dates)
    line.set_ydata(combined_prices)
    ax.relim()
    ax.autoscale_view()
    plt.draw()

# Initial parameters
initial_steps = 100

# Fetch initial historical data
historical_prices = fetch_historical_data('AAPL', '2024-01-01')

# Create initial random walk
walk = simple_random_walk(initial_steps)

# Create a figure and axis with a larger size
fig, ax = plt.subplots(figsize=(15, 12))
plt.subplots_adjust(left=0.1, bottom=0.35)
line, = ax.plot(historical_prices.index, historical_prices.values, lw=2)

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