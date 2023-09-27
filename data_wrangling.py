import pandas as pd

# Load your existing CSV file into a DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/RealSakifAbdullah/FIT3179_Assignment2/main/data/missing_migrants.csv')

# Remove ' (P)' from the column
df['Region of Origin'] = df['Region of Origin'].str.replace(" (P)", "")

# Save the modified DataFrame to a new CSV file
df.to_csv('test.csv', index=False)
