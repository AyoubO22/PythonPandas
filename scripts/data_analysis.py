import pandas as pd
import time

# Function to measure execution time
def measure_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {function.__name__}: {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@measure_time
def import_data(file_path):
    return pd.read_csv(file_path)

@measure_time
def sort_data(df, column):
    return df.sort_values(by=column)

@measure_time
def filter_data(df, condition):
    return df.query(condition)

@measure_time
def calculate_statistics(df, columns):
    return df[columns].mean(), df[columns].sum()

# Main function to run the tests
def run_tests(file_path):
    df = import_data(file_path)

    # Sorting the data
    sorted_df = sort_data(df, 'column_to_sort')

    # Filtering the data
    filtered_df = filter_data(sorted_df, 'column_condition > 500')

    # Calculating statistics
    means, sums = calculate_statistics(filtered_df, ['column1', 'column2'])
    print("Means:", means)
    print("Sums:", sums)

# Example usage
if __name__ == "__main__":
    for size in ['donnees/synthétiques_10000.csv',
                 'donnees/synthétiques_100000.csv',
                 'donnees/synthétiques_500000.csv',
                 'donnees/synthétiques_1000000.csv']:
        print(f"\nTests on {size}:")
        run_tests(size)
