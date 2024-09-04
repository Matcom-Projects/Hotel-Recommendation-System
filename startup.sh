.startup.sh
#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_csv_file>"
    exit 1
fi

# Assign the first argument to a variable
CSV_FILE_PATH=$1

# Execute the Python program with the provided CSV file path
python create_result.py "$CSV_FILE_PATH"