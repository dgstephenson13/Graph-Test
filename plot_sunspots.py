# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:37:11 2024

@author: steph
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv(r'C:\Users\steph\Graphs Test\Graph-Test\sunspots.csv')

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(df['Sunspots'])  # Replace 'Column1' and 'Column2' with actual column names
plt.title('Sunspots over Time')
plt.xlabel('Time')  # Adjust label as per your data
plt.ylabel('Number of Sunspots')  # Adjust label as per your data
plt.grid(True)

plt.savefig(r'C:\Users\steph\Graphs Test\Graph-Test\sunspots_plot.png')
plt.show()