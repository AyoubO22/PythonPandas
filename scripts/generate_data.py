import os
import pandas as pd
import numpy as np

# Generation parameters
number_of_rows = [10000, 100000, 500000, 1000000]  # dataset sizes
columns = ['id', 'column_to_sort', 'column_condition', 'column1', 'column2', 'target_column']

# Folder path
directory = 'donnees'

# Check if the folder exists, if not, create it
if not os.path.exists(directory):
    os.makedirs(directory)

# Loop to create CSV files of different sizes
for n in number_of_rows:
    # Generate synthetic data
    data = {
        'id': range(1, n + 1),
        'column_to_sort': np.random.rand(n) * 1000,  # Random values between 0 and 1000
        'column_condition': np.random.randint(1, 1000, size=n),  # Values between 1 and 1000
        'column1': np.random.rand(n) * 100,  # Random values
        'column2': np.random.rand(n) * 200,  # Random values
        'target_column': np.random.choice(['A', 'B', 'C', 'D'], size=n)  # Categories
    }
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Save as CSV in the "donnees" folder
    df.to_csv(f'{directory}/synthetic_{n}.csv', index=False)
    print(f'CSV file generated: synthetic_{n}.csv')
