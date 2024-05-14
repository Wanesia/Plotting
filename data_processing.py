import pandas as pd

data = pd.read_csv('data/speed_data_data.csv')

# Display the count of null values in the 'age' column
print("Null count in the 'age' column before dropping rows:")
print(data['age'].isnull().sum())

# Drops rows with null values in the 'age' column
data_cleaned = data.dropna(subset=['age'])

# Display the count of null values in the 'age' column after dropping rows
print("Null count in the 'age' column after dropping rows:")
print(data_cleaned['age'].isnull().sum())

# Selecting needed data (dec column represents match)
selected_data = data_cleaned[['gender', 'age', 'dec']]
print(selected_data.info())
print(selected_data.isnull().sum())
