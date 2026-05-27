""" Create a scatter plot using Matplotlib that visualizes square numbers from 1 to 1000.
Requirements:
  - Generate x values from 1 to 1000
  - Compute y values as the square of x
  - Plot the data using a scatter plot
  - Color points based on their values using a blue colormap
  - Apply a Matplotlib style
  - Add title and axis labels
  - Adjust axis limits and disable scientific notation
  - Display the plot.   """

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style = "plain")

plt.show()

