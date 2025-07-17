import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data using NumPy
x = np.arange(1, 6)              # x-axis values: [1, 2, 3, 4, 5]
y = x * 2                        # y-axis values: [2, 4, 6, 8, 10]

# Create a DataFrame using Pandas
data = pd.DataFrame({'X values': x, 'Y values': y})

# Print the DataFrame (optional)
print(data)

# Plot the graph using Matplotlib
plt.plot(data['X values'], data['Y values'], marker='o', color='blue')
plt.title("Simple Line Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()
