import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('your_file.csv')

region_sum = df.groupby('Region of Incidents')['Column_to_sum'].sum()

print(region_sum)
