#!/bin/bash

# Create a Python script for the Matplotlib plot
cat <<EOL > matplot.py
import matplotlib.pyplot as plt

# Data for the two sets
x1 = [7, 8, 9, 10, 11, 12]
y1 = [17.1, 18.4, 20.2, 23.0, 25.6, 30.4]

x2 = [7, 8, 9, 10, 11, 12]
y2 = [17.1, 18.1, 20.1, 22.8, 25.6, 29.9]

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x1, y1, label='Approximate Tour', marker='o', linestyle='-')
plt.plot(x2, y2, label='Exact Tour', marker='s', linestyle='--')

# Add labels and title
plt.title('Two Sets of Data')
plt.xlabel('Number of vertices')
plt.ylabel('Cost of Tour')

# Add legend
plt.legend()

# Save and display the plot
plt.savefig('accuracy_plot.png')
plt.show()
EOL

# Make the Python script executable
chmod +x matplot.py

# Run the Python script
python3 matplot.py
