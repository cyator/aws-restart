#!/bin/bash

# Prompt the user to enter a name
echo "please enter name"
read NAME

# Print a message indicating that files are being created for the entered name
echo "creating files for $NAME"

# Get all files in the current directory that contain the entered name
FILES=$(ls | grep $NAME)

# Initialize a variable to keep track of the highest number found in existing file names
MAX=0

# Loop through each file name containing the entered name
for f in $FILES
do
    # Extract the numeric portion of the file name and assign it to the NUM variable
    NUM=${f//[!0-9]}
    
    # Compare NUM to the current MAX value and update MAX if necessary
    MAX=$(( $NUM > $MAX ? $NUM : $MAX ))
done

# Print a message indicating that the script will start creating files from MAX + 1
echo "starting from $MAX"

# Loop through the numbers 1 to 25
for i in {1..25}
do
    # Create a new file with the name "<entered name><i + MAX>"
    touch $NAME$(($i+$MAX))
done

