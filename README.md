# Hotel Recommendation System

## Authors:
- Miguel Alejandro Yáñez Martínez C311
- Darío Rodríguez Llosa C312

## Problem Description:

This project develops a hotel recommendation system that enhances the user experience when searching for accommodation. It utilizes sentiment analysis of customer reviews and evaluates customer satisfaction based on those reviews. A model for emotion recognition specifically trained for this task was applied, allowing for more accurate identification of positive, neutral, and negative emotions. The results obtained help classify hotels based on guest satisfaction, making it easier for users to choose the most suitable hotel according to their perception of quality.

## Requirements:

To ensure the proper functioning of the project, make sure to have the following requirements installed:

- **torch**
- **transformers**
- **scikit-learn**
- **numpy**
- **pandas**
- **matplotlib**
- **seaborn**
- **tqdm**
- **flask**

You can install them by running `pip install -r requirements.txt`

## How to Use the Program

This program provides a simple command-line interface that allows users to execute various tasks related to data processing, recommendations, training, sentiment analysis and . Below are the steps to run the program and utilize its features.

**Step 1:** Prerequisites

Before running the program, ensure you have the following installed on your system:

Python (version 3.x)
Jupyter Notebook
Any necessary libraries or dependencies required by the scripts (these should be specified in a requirements file if applicable).

**Step 2:** Running the Program

Open your terminal or command prompt.

Navigate to the directory where your Python script is located.

Run the script by executing:

.\startup.sh in Linux or .\startup.bat in windows

**Step 3:** Using the Menu

Once you run the program, it will display a menu with several options:

Select an option to execute:
1. Run Create Results
2. Run Recommendations
3. Run Data Processing
4. Run Training
5. Run Web Application
6. Run Sentiment Analysis
0. Exit

Options Explained:

- Option 1: Run Create Results: Executes a script that generates results for recommendations.
- Option 2: Run Recommendations: Runs a Jupyter notebook that processes recommendation algorithms.
- Option 3: Run Data Processing: Executes a Jupyter notebook for data preprocessing tasks.
- Option 4: Run Training: Runs a Jupyter notebook that handles model training.
- Option 5: Run Web Application: Executes a Python script that starts a web application.
- Option 6: Run Sentiment Analysis: Runs a Python script that performs sentiment analysis on given data.
- Option 0: Exit: Exits the program.

**Step 4:** Making a Selection

After reviewing the options, enter the corresponding number for the task you wish to execute and press Enter. For example, if you want to run recommendations, type 2 and hit Enter.

### Handling Invalid Input

If you enter an invalid selection (a number outside of the range of available options), or if you input something that is not a number, you will receive an error message prompting you to try again.

**Step 5:** Exiting the Program

To exit the program at any time, simply select option 0 from the menu.

By following these steps, you can effectively utilize this program to perform various tasks related to data processing and analysis. 



