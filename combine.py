import pandas as pd

# Read the two CSV files into dataframes
df1 = pd.read_csv('song_attributes_like.csv')
df2 = pd.read_csv('song_attributes_dont_like.csv')

# Add a new column 'Liked' and set the value to 1 for df1 and 0 for df2
df1['Liked'] = 1
df2['Liked'] = 0

# Concatenate the two dataframes into a single dataframe
df = pd.concat([df1, df2], ignore_index=True, sort=False)

# Save the resulting dataframe to a new CSV file
df.to_csv('combined.csv', index=False)

# Print a message indicating that the file was saved
print('Dataframe saved to combined.csv')

# song_attributes_like.csv
# song_attributes_dont_like.csv
