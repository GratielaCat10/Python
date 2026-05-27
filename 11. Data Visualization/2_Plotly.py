""" Simulate rolling two dice and visualize the results using a bar chart.
Requirements:
  - Create a Die class with a configurable number of sides (default 6)
  - Simulate rolling two dice 1000 times
  - Store the sum of each roll in a list
  - Count the frequency of each possible result
  - Visualize the results using a bar chart (Plotly or similar library)
  - Label the chart and axes appropriately
  - Display the final visualization in a browser.   """

#Creating the Die class
from random import randint

class Die:
    """ A class representing a single die """

    def __init__(self,num_sides=6):
        """ Assume a six sided die """
        self.num_sides = num_sides

    def roll(self):
        """ Return a random value between 1 and number of sides """
        return randint(1,self.num_sides)



#Rolling Dice
import plotly.express as px

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# results = [die_1.roll() + die_2.roll() for roll_num in range(1000)] -> varianta cu list comprehesion

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
# frequencies = [results.count(value) for value in poss_results] -> varianta cu list comprehesion

# Visualize the results.
title = "Results of rolling two D6 dice 1000 times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customized chart.
fig.update_layout(xaxis_dtick=1)

fig.show(renderer="browser")

