import pandas as pd

# # Load your existing CSV file into a DataFrame
df = pd.read_csv('data/missing_migrants.csv')
print(df.head())

value_counts = df['RegionWB of Incident'].value_counts().reset_index()

# Rename the columns in the new DataFrame
value_counts.columns = ['RegionWB of Incident', 'Count']

# Display the new DataFrame
print(value_counts)

# # Define a function to map region to continent
# def map_region_to_continent(region):
#     if region == 'Southern Asia' :
#         return 'South Asia'

#     elif region == 'Europe':
#         return 'Europe & Central Asia'
    
#     elif region == 'South America':
#         return 'South America'
    
#     elif region in ['Caribbean','Central America','South America']:
#         return 'Latin America & Caribbean'

#     elif region in ['North America']:
#         return 'North America'
    
#     elif region in ['Eastern Africa','Mediterranean','Western Africa']:
#         return 'Sub-Saharan Africa'


#     elif region in ['Northern Africa','Western Asia','Middle Africa','Southern Africa']:
#         return "Middle East & North Africa"
    
#     else:
#         return None  # Handle other cases if needed

# # Apply the mapping function to create the new column
# df['RegionWB of Incident'] = df['Region of Incident'].apply(map_region_to_continent)

# # Save the modified DataFrame to a new CSV file
value_counts.to_csv('regionwb_counts.csv', index=False)