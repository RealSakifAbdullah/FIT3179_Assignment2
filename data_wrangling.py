import pandas as pd

# Load your existing CSV file into a DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/RealSakifAbdullah/FIT3179_Assignment2/main/data/missing_migrants.csv')

# Remove ' (P)' from the column
df['Cause of Death'] = df['Cause of Death'].str.replace('Drowning,Harsh environmental conditions / lack of adequate shelter, food, water', 'Drowning')
df['Cause of Death'] = df['Cause of Death'].str.replace('Drowning,Vehicle accident / death linked to hazardous transport', 'Hazardous Transport')
df['Cause of Death'] = df['Cause of Death'].str.replace('Harsh environmental conditions / lack of adequate shelter, food, water,Sickness / lack of access to adequate healthcare', 'Lack of healthcare')
df['Cause of Death'] = df['Cause of Death'].str.replace('Harsh environmental conditions / lack of adequate shelter, food, water,Mixed or unknown', "Lack of shelter, food, water")
df['Cause of Death'] = df['Cause of Death'].str.replace('Drowning,Violence', "Violence")
df['Cause of Death'] = df['Cause of Death'].str.replace('Mixed or unknown,Vehicle accident / death linked to hazardous transport,Violence', "Hazardous Transport")
df['Cause of Death'] = df['Cause of Death'].str.replace('Drowning,Sickness / lack of access to adequate healthcare', "Lack of healthcare")
df['Cause of Death'] = df['Cause of Death'].str.replace('Vehicle accident / death linked to hazardous transport', 'Hazardous Transport')
df['Cause of Death'] = df['Cause of Death'].str.replace('Harsh environmental conditions / lack of adequate shelter, food, water', "Lack of shelter, food, water")
df['Cause of Death'] = df['Cause of Death'].str.replace('Sickness / lack of access to adequate healthcare', 'Lack of healthcare')
df['Cause of Death'] = df['Cause of Death'].str.replace('Drowning,Mixed', 'Drowning')
df['Cause of Death'] = df['Cause of Death'].str.replace('Drowning or unknown', 'Drowning')


# Save the modified DataFrame to a new CSV file
df.to_csv('test.csv', index=False)
