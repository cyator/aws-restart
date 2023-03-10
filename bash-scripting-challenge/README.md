# Bash Script for Creating Empty Files

This bash script creates 25 empty files in the current directory, with names that start with your name followed by a number. Each time you run the script, it generates a new batch of 25 files with increasing numbers starting with the last or maximum number that already exists.

## How to Use

1. Open a terminal and navigate to the directory where you want to create the files.
2. Copy the script into the terminal or create a new file with a .sh extension and copy the script into the file.
3. Make the script executable by running the following command: ``` chmod +x ```
4. Run the script using the command ./script.sh.
5. When prompted, enter a name for the files you want to create.
6. The script will search for all files in the current directory containing the entered name and extract the highest number from the file names.
7. It will then create 25 empty files with names starting from the highest number found + 1, incrementing by 1.

## Notes

1. The script uses the **touch** command to create empty files.
2. It uses a **for loop** to create 25 files with incremental names.
3. The script does not hard code the numbers; it generates them based on the highest number found in the existing file names.
4. You can run the script multiple times, and it will continue to generate files with incremental names based on the highest number found in existing file names.
5. To validate that the script created the expected files, you can use the ``` ls -l ```  command to display a long list of the directory and its contents.
