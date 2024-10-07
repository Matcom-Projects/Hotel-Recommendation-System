import subprocess
import sys
import pandas as pd
import argparse
import os


def redirect(foldername, filename):
    return os.path.normpath(os.path.join(os.getcwd(), '..', foldername, filename))

def install_requirements():
    try:
        # Call pip to install the requirements from the requirements.txt file
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")

def process_dataset(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    # Group the DataFrame by the specified columns and calculate the average of 'final_score'
    grouped_df = df.groupby(['address', 'categories', 'city', 'country', 'name', 'province']).agg(
        average_final_score=('final_score', 'mean')
    ).reset_index()

    # Sort the grouped DataFrame in descending order by 'average_final_score'
    grouped_df = grouped_df.sort_values(by='average_final_score', ascending=False)
    

    # Save the sorted DataFrame to a CSV file named 'Hotel_Recomendation_Result.csv'
    grouped_df.to_csv(redirect('Datasets', 'Hotel_Recomendation_Result.csv'), index=False)

    # Display the top 50 rows of the grouped DataFrame
    grouped_df.head(50)
    return grouped_df

# Example usage
if __name__ == "__main__":
    install_requirements()
    
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Process a CSV dataset to calculate average final scores.')
    parser.add_argument('file_path', type=str, help='The path to the CSV file to be processed.')

    # Parse arguments
    args = parser.parse_args()

    # Call the process_dataset function with the provided file path
    result_df = process_dataset(args.file_path)
    print(result_df)
    # Wait for the user to press "Enter" before exiting
    input("Press Enter to exit...")
