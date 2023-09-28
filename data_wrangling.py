import pandas as pd

# Load your existing CSV file into a DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/RealSakifAbdullah/FIT3179_Assignment2/main/data/missing_migrants.csv')

df_clean = df.dropna()

# Save the modified DataFrame to a new CSV file
df_clean.to_csv('test.csv', index=False)
