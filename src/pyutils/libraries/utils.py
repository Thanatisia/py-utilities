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


