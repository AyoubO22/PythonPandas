import os
import matplotlib.pyplot as plt

# Check if the 'resultats' folder exists, if not, create it
if not os.path.exists('resultats'):
    os.makedirs('resultats')

# Execution data
file_sizes = ['10k', '100k', '500k', '1M']
import_time = [0.01, 0.08, 0.48, 0.97]
sort_time = [0.00, 0.02, 0.16, 0.27]
filter_time = [0.00, 0.00, 0.02, 0.02]
stats_time = [0.00, 0.00, 0.01, 0.01]

# Creating the plots
plt.figure(figsize=(10, 6))

plt.plot(file_sizes, import_time, label='Import Time', marker='o')
plt.plot(file_sizes, sort_time, label='Sort Time', marker='o')
plt.plot(file_sizes, filter_time, label='Filter Time', marker='o')
plt.plot(file_sizes, stats_time, label='Stats Calculation Time', marker='o')

plt.xlabel('CSV File Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time for Different File Sizes')
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('resultats/execution_time.png')
plt.show()
