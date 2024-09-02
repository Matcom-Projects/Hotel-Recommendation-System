import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('Dataser_with_score.csv')

# Group the DataFrame by the specified columns and calculate the average of 'final_score'
grouped_df = df.groupby(['address', 'categories', 'city', 'country', 'name', 'province']).agg(
    average_final_score=('final_score', 'mean')
).reset_index()

# Sort the grouped DataFrame in descending order by 'average_final_score'
grouped_df = grouped_df.sort_values(by='average_final_score', ascending=False)

# Save the sorted DataFrame to a CSV file named 'Hotel_Recomendation_Result.csv'
grouped_df.to_csv('Hotel_Recomendation_Result.csv', index=False)

# Display the top 50 rows of the grouped DataFrame
grouped_df.head(50)