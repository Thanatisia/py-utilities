"""
Functions and utilities for adding information of various types (debugging, pretty-fying etc)
"""
import os
import sys

"""
FUNCTIONS : Pretty Print
"""
def pprint_error(msg, newline=False, fmt_str="[ERROR]"):
    """
    Pretty Printing: Error Messages

    :: Params
    - msg : Specify the message you want to pretty print
        + Type: String
    - newline : Enable/Disable newline formatting
        + Type: Integer
    - fmt_str : Specify the format string to apply to the message
        + Type: String
        + Default: [ERROR] %s
    """
    # Initialize Variables

    # Design message
    fmt_str += " {}".format(msg)

    # Parse options
    if newline == True:
        ## TRUE
        fmt_str += "\n".format(msg)

    # Print message
    print(fmt_str)

def pprint_info(msg, newline=False, fmt_str="[INFO]"):
    """
    Pretty Printing: Information

    :: Params
    - msg : Specify the message you want to pretty print
        + Type: String
    - newline : Enable/Disable newline formatting
        + Type: Integer
    - fmt_str : Specify the format string to apply to the message
        + Type: String
        + Default: [INFO] %s
    """
    # Initialize Variables

    # Design message
    fmt_str += " {}".format(msg)

    # Parse options
    if newline == True:
        ## TRUE
        fmt_str += "\n".format(msg)

    # Print message
    print(fmt_str)

def pprint_warning(msg, newline=False, fmt_str="[WARNING]"):
    """
    Pretty Printing: Warning

    :: Params
    - msg : Specify the message you want to pretty print
        + Type: String
    - newline : Enable/Disable newline formatting
        + Type: Integer
    - fmt_str : Specify the format string to apply to the message
        + Type: String
        + Default: [WARNING] %s
    """
    # Initialize Variables

    # Design message
    fmt_str += " {}".format(msg)

    # Parse options
    if newline == True:
        ## TRUE
        fmt_str += "\n".format(msg)

    # Print message
    print(fmt_str)

"""
FUNCTIONS: Formatting and String/Text modifications
"""
def sizeof_fmt(num, suffix="B", factor=1024.0, spacing=False):
    """
    Format a given size string with the appropriate unit

    :: Params
    - num : Specify the size of the file
        + Type: Integer
    - suffix : Specify the default suffix of the file
        + Type: String
        + Default: B
        - Accepted values
            + "" : None
            + "B" : Bytes
            + "K" : Kilobytes
            + "Ki" : Kibibytes
            + "M" : "Megabytes
            + "Mi" : Mibibytes
            + "G" : Gigabytes
            + "Gi" : Gibibytes
            + "T" : Terabytes
            + "Ti" : Tibibytes
            + "P" : Petabytes
            + "Pi" : Pibibytes
            + "E"
            + "Ei"
            + "Z"
            + "Zi"
    - factor : Specify the base common denominator/factor between transitioning from one size to another (i.e. 1024.0 is a good factor because 1K = 1024 Bytes, 1M = 1024 Kilobytes, 1G = 1024 Megabytes etc etc)
        + Type: Float/Double
        + Default: 1024.0
    - spacing : Enable/Disable the addition of a space between the size and the prefix
        + Type: Boolean
        + Default: False

    :: Return
    - fmt_str : Returns the formatted string based on the size provided
        + Type: String

    :: Resources
    - StackOverflow - Get a human-readable version of a file size : https://stackoverflow.com/questions/1094841/get-a-human-readable-version-of-a-file-size
    """
    # Initialize variables
    accepted_units = ("", "K", "Ki", "M", "Mi", "G", "Gi", "T", "Ti", "P", "Pi", "E", "Ei", "Z", "Zi")

    # Iterate and format size string
    for unit in accepted_units:
        if abs(num) < factor:
            # Format string
            fmt_str = f"{num:3.1f}"
            # Append string if 'spacing' is enabled 
            if spacing:
                fmt_str += " "
            # Append unit and suffix
            fmt_str += f"{unit}{suffix}"
            return fmt_str
        num /= factor
    if spacing:
        return f"{num:.1f} Yi{suffix}"
    else:
        return f"{num:.1f}Yi{suffix}"

def convert_size_to_num(size, suffix="B", factor=1024):
    """
    Convert a given size to a numerical value based on the provided suffix (i.e. xG, xGiB, xM, xMiB, ...)

    :: Params
    - size : Specify the size you wish to convert into numerical form
        + Type: Integer
    - suffix : Specify the default suffix of the size
        + Type: String
        + Default: B
        - Accepted values
            + "" : None
            + "B" : Bytes
            + "K" : Kilobytes
            + "Ki" : Kibibytes
            + "M" : "Megabytes
            + "Mi" : Mibibytes
            + "G" : Gigabytes
            + "Gi" : Gibibytes
            + "T" : Terabytes
            + "Ti" : Tibibytes
            + "P" : Petabytes
            + "Pi" : Pibibytes
            + "E"
            + "Ei"
            + "Z"
            + "Zi"
        - Conversion
            + 1K = 1024 Bytes
            + 1M = 1024 Kilobytes
            + 1G = 1024 Megabytes
            + 1T = 1024 Gigabytes
            + 1P = 1024 Terabytes
    - factor : Specify the base common denominator/factor between transitioning from one size to another (i.e. 1024.0 is a good factor because 1K = 1024 Bytes, 1M = 1024 Kilobytes, 1G = 1024 Megabytes etc etc)
        + Type: Integer
        + Default: 1024

    :: Return
    - num_bytes : Returns the bytes (integer) corresponding to the provided size and suffix
        + Type: Integer
    """
    # Initialize variables
    accepted_units = ("B", "K", "Ki", "M", "Mi", "G", "Gi", "T", "Ti", "P", "Pi", "E", "Ei", "Z", "Zi")
    conversion_table = {
        1 : ["B", "b", "bytes"],
        2 : ["K", "k", "kb", "kilo", "kilobytes"],
        3 : ["M", "m", "mb", "mega", "megabytes"],
        4 : ["G", "g", "gb", "giga", "gigabytes"],
        5 : ["T", "t", "tb", "tera", "terabytes"],
        6 : ["P", "p", "pb", "peta", "petabytes"],
        7 : ["E", "e", "eb"],
        8 : ["Z", "z", "zb"],
    }
    num_bytes = 0

    # Iterate through each unit; For each unit - multiply by the factor (default: 1024)
    for conv_idx, conv_accepted_values in conversion_table.items():
        # Convert suffix to lower case
        suffix_lowercase = suffix.lower()

        # print("Suffix: {}".format(suffix_lowercase))

        # Check if current index is the first item
        if conv_idx == 1:
            num_bytes = 1
        else:
            # Multiply the number by the factor
            num_bytes *= factor

        # Check if suffix is in the accepted values list
        if suffix_lowercase in conv_accepted_values:
            # Break condition: End
            break

        # print("Bytes [{}]: {}".format(conv_accepted_values[0], num_bytes))

    # Multiply the number by the size
    num_bytes *= size

    # Return
    return num_bytes

def split_size_suffix(size_str):
    """
    Split a given size string into its components [0 = Size numeral, 1 = Size Suffix]
    - i.e.
        + xB => [x, 'B']
        + xK => [x, 'K']
        + xKiB => [x, 'KiB']
        + xG => [x, 'G']
        + xGiB => [x, 'GiB']
        + xM => [x, 'M']
        + xMiB => [x, 'MiB']

    :: Params
    - size : Specify the size you wish to convert into numerical form
        + Type: String
    - suffix : Specify the default suffix of the size
        + Type: String
        + Default: B
        - Accepted values
            + "" : None
            + "B" : Bytes
            + "K" : Kilobytes
            + "Ki" : Kibibytes
            + "M" : "Megabytes
            + "Mi" : Mibibytes
            + "G" : Gigabytes
            + "Gi" : Gibibytes
            + "T" : Terabytes
            + "Ti" : Tibibytes
            + "P" : Petabytes
            + "Pi" : Pibibytes
            + "E"
            + "Ei"
            + "Z"
            + "Zi"
        - Conversion
            + 1K = 1024 Bytes
            + 1M = 1024 Kilobytes
            + 1G = 1024 Megabytes
            + 1T = 1024 Gigabytes
            + 1P = 1024 Terabytes

    :: Returns
    - size_split : A List containing the components of the size string after splitting
        + Type: List
        - Values/Elements
            + 0 : Size Digit/Numeral
            + 1 : Size Suffix
    """
    # Obtain the filter size
    filter_size = ""
    filter_suffix = ""

    # Split the size string
    size_str_spl = size_str.split()

    # Iterate through all characters in the suffix string and try to convert into an integer (test if its a number/digit)
    for i in range(len(size_str)):
        # Get condition characters
        char = size_str[i]

        try:
            condition_num = int(char)
            filter_size += str(condition_num)
        except ValueError as ve:
            # Not number, append all remaining strings (the suffix) to the suffix string
            filter_suffix = size_str[i:len(size_str)]
            # Break the loop
            break

    # Return
    return [filter_size, filter_suffix]

