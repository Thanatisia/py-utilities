"""
File Handling I/O Processing Library
"""
import os
import sys

def import_file(f_Name):
    """
    Open and read a file into a list and return

    :: Params
    - f_Name : The name of the file
        Type: String
    """
    # Initialize Variables
    res = []
    line = ""

    # Open file for reading
    with open(f_Name, "r+") as read_file:
         # Read first line
         line = read_file.readline()

         # While there are still lines
         while line != "":
             # Append line into list
             res.append(line)

             # Read subsequent lines
             line = read_file.readline()

         # Close file after usage
         read_file.close()

    # Output
    return res

def export_file(f_Name, file_contents):
    """
    Open and write a list of contents into the file

    :: Params
    - f_Name : The name of the file
        Type: String

    - file_contents : List containing all lines of the contents to write
        Type: List
    """
    # Initialize Variables
    res = []
    line = ""

    # Open file for reading
    with open(f_Name, "a+") as export_file:
         # Loop through the list
         for i in range(len(file_contents)):
             # Get current line
             line = file_contents[i]

             # Write current line into the file
             export_file.write(line)

             # Write newline
             export_file.write("\n")

         # Close file after usage
         export_file.close()


