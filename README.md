TASK 1.
Explanation

1.Argument Parsing:
parse_arguments() function sets up argument parsing for the script. It requires the source directory and optionally takes the destination directory (defaulting to dist).

2.Recursive File Copying:
copy_and_sort_files(source_dir, destination_dir) function recursively traverses the source directory.
For each item, if it is a directory, the function calls itself recursively.
If it is a file, it determines the file extension and creates a corresponding subdirectory in the destination directory.
The file is then copied to the appropriate subdirectory.

3.Exception Handling:
The code includes a try-except block around the file copying operation to handle potential errors, such as permission issues or missing files.

4.Main Execution:
The main() function initializes the process by parsing arguments and invoking the copy_and_sort_files function with the provided directories.
Usage
To use this script, save it to a file (e.g., recursive_copy_sort.py) and run it from the command line with the source and destination directories as arguments:

```python recursive_copy_sort.py /path/to/source /path/to/destination```

If the destination directory is omitted, it defaults to dist:

```python recursive_copy_sort.py /path/to/source```

This script will copy all files from the source directory to the destination directory, organizing them into subdirectories based on their file extensions.

