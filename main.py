import subprocess

def show_menu():
    """
    Displays a fixed menu with options for the user to execute different tasks.
    """
    print("Select an option to execute:")
    print("1. Run Create Results")
    print("2. Run Recommendations")
    print("3. Run Data Processing")
    print("4. Run Training")
    print("5. Run Web Application")
    print("6. Run Sentiment Analysis")
    print("0. Exit")

def execute(option):
    """
    Executes the selected file based on the chosen option.
    
    Args:
        opcion (int): The selected option number corresponding to a specific file to run.
    """
    # Option 1: Run the script to create results
    if option == 1:
        filename = "src/Recommmendation/create_result.py"
        print(f"Running {filename}...")
        subprocess.run(['python', filename])

    # Option 2: Run the Jupyter notebook for recommendations
    elif option == 2:
        filename = "src/Recommmendation/recomendation.ipynb"
        print(f"Running {filename}...")
        subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', filename])

    # Option 3: Run the Jupyter notebook for data preprocessing
    elif option == 3:
        filename = "src/Training/data_preprocessing.ipynb"
        print(f"Running {filename}...")
        subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', filename])

    # Option 4: Run the Jupyter notebook for training
    elif option == 4:
        archivo = "src/Training/training.ipynb"
        print(f"Running {filename}...")
        subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', filename])

    # Option 5: Run the Python script for the web application
    elif option == 5:
        filename = "src/Webapp/main.py"
        print(f"Running {filename}...")
        subprocess.run(['python', filename])

    # Option 6: Run the Python script for sentiment analysis
    elif option == 6:
        filename = "src/Webapp/sentiment_analysis.py"
        print(f"Running {filename}...")
        subprocess.run(['python', filename])

if __name__ == "__main__":
    # Infinite loop to keep showing the menu until the user chooses to exit
    while True:
        show_menu()

        try:
            # Get user input and convert it to an integer
            selection = int(input("Enter your selection number: "))
            
            # Option 0: Exit the program
            if selection == 0:
                print("Exiting...")
                break
            # If the selection is valid, execute the corresponding file
            elif 1 <= selection <= 6:
                execute(selection)
            else:
                print("Invalid selection. Please try again.")

        # Handle the case where the user input is not a valid integer
        except ValueError:
            print("Please enter a valid number.")
