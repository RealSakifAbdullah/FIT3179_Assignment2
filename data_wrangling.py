import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('https://raw.githubusercontent.com/RealSakifAbdullah/FIT3179_Assignment2/main/data/missing_migrants.csv')

region_counts = df['Region of Incident'].value_counts()

# Create a DataFrame from the Series
df_counts = region_counts.reset_index()
df_counts.columns = ['Region of Incident', 'Count']

# Specify the file path where you want to save the CSV file
csv_file_path = 'region_counts.csv'

# Save the DataFrame to a CSV file
df_counts.to_csv(csv_file_path, index=False)

# Now you have a CSV file named 'region_counts.csv' with the counts
