import pandas as pd

# # Load your existing CSV file into a DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/RealSakifAbdullah/FIT3179_Assignment2/main/data/missing_migrants.csv')

# Define a function to map region to continent
def map_region_to_continent(region):
    if 'Asia' in region:
        return 'Asia'
    
    elif region == 'Europe':
        return 'Europe'
    
    elif region == 'South America':
        return 'South America'

    elif region in ['North America','Caribbean','Central America']:
        return 'North America'
    
    elif 'Africa' in region:
        return 'Africa'
    
    elif region == 'Mediterranean':
        return 'Seven seas (open ocean)'
    
    else:
        return None  # Handle other cases if needed

# Apply the mapping function to create the new column
df['Continent of Incident'] = df['Region of Incident'].apply(map_region_to_continent)

# Save the modified DataFrame to a new CSV file
df.to_csv('test.csv', index=False)