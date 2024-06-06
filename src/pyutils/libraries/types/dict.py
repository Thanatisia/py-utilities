"""
Dictionary (Key-Value Mapping-based Container)-related helper wrapper functions and utilities

:: Notes
- Key-Value Mapping: Other names includes: Map, HashMap, Associative Array, Tables
"""
import os
import sys

def print_dict(dict_obj):
    """
    Print all dictionaries (key-value/associative array) provided
    """
    # Initialize Variables

    # Iterate through associative array
    for k,v in dict_obj.items():
        # Print
        print("{} : {}\n".format(k, v))

def merge_dictionary(dict_1, dict_2):
    """
    Merge 2 dictionaries together
    """
    # Initialize Variables
    merged_dictionary = {}

    # Merge optionals with arguments and flags together
    for k,v in dict_1.items():
        merged_dictionary[k] = v
    for k,v in dict_2.items():
        merged_dictionary[k] = v

    # Output/Return
    return merged_dictionary

