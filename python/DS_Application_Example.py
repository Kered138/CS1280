
# Performs descriptive analysis on data from a CSV file using pandas.
import pandas as pd

def read_csv_file(filename):
    data = pd.read_csv(filename)
    print(f"\nSuccessfully loaded '{filename}'")
    return data

def display_basic_info(data):
    print("\n--- Basic Information ---")
    print(f"Number of rows: {data.shape[0]}")
    print(f"Number of columns: {data.shape[1]}")
    print("\nColumn Names:")
    print(list(data.columns))

def display_descriptive_stats(data):
    print("\n--- Descriptive Statistics ---")
    print(data.describe())

def display_categorical_summary(data):
    print("\n--- Categorical Columns Summary ---")
    categorical_cols = data.select_dtypes(include=['object'])
    for col in categorical_cols.columns:
        print(f"\nColumn: {col}")
        print(categorical_cols[col].value_counts().head(10))

def main():
    print("=== Descriptive Analysis Program ===")
    filename = input("Enter the path to your CSV file (e.g., data.csv): ")

    data = read_csv_file(filename)
    display_basic_info(data)
    display_descriptive_stats(data)
    display_categorical_summary(data)

    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
