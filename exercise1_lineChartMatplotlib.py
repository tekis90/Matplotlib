
"""
Creating a simple line plot with matplotlib

"""

import numpy as np
import matplotlib.pyplot as plt


#Creating a NumPy array containing numbers 1 through 10
x = np.arange(1, 10)

# Create the array y, using the formula y = (x*3.14) + 4
y = (x * 3.14) + 4



# I create a line chart using x and y values

plt.plot(x, y, color="red", label="y=(x*3.14)+4")
# I specify the line color with the 'color' parameter
# I specify a label for the line with the 'label' parameter


# I use the 'legend' function to add a description for the drawing
plt.legend()

# x axis label
plt.xlabel("X Ekseni")

# Y axis label
plt.ylabel("Y Ekseni")

# Chart title
plt.title("y=(x*3.14)+4")

# Show the created chart
plt.show()
