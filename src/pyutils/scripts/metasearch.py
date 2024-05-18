"""
File Metadata searcher/filter

- Search for all files according to a specific metadata category, keyword, filter value or condition
"""
import os
import sys
from json import load, loads, dump, dumps
from pyutils.libraries.blob import search_files_by_metadata

def remove_empty_entries(metasearch_results:dict):
    """
    Remove empty entries from the provided metasearch results dictionary

    :: Params
    - metasearch_results : Specify the metasearch dictionary containing the results list you wish to remove empty entries from
        + Type: Dictionary
    """
    i = 0

    # Obtain the results list from the metasearch dictionary
    metasearch_results_values = metasearch_results["results"]

    # Iterate through all elements of metasearch_results_values until the last element
    while (i <= len(metasearch_results_values)-1):
        # Get current element
        curr_val = metasearch_results_values[i]

        # Get directory name and files
        curr_val_dir_name = curr_val["directory"]
        curr_val_files = curr_val["files"]

        # Check if the files list has items
        if len(curr_val_files) == 0:
            # Remove entry from list
            metasearch_results["results"].pop(i)
            # Decrement index counter by 1
            i -= 1
            # Reset values list
            metasearch_results_values:list = metasearch_results["results"]

        # Increment index counter
        i += 1

def main():
    # Initialize Variables
    top_level_root_dir = "."
    stdout_msg = [] # List of messages to print to standard output
    filter = ""
    output_format = ["text", "json"][1] # Specify the standard output export format. Options: text (Default), json
    remove_empty = True

    # Get CLI arguments
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

    # Check if arguments are provided
    if argc > 0:
        # Get filter
        if argc >= 1:
            filter = argv[0]

        # Prepare filters
        filter = filter.split()

        # Data/Null Validation Check
        if (filter == "") or (len(filter) < 3):
            while len(filter) < 3:
                print("Filter Options: size")
                print("Filter Operators: [<, lt], [<=, le], [>, gt], [>=, ge], [!=, ne], [==, eq]")
                print("""
Filter Condition:
    - size:
        xB   : Bytes
        xK   : Kilobytes
        xKiB : Kibibytes
        xM   : Megabytes
        xMiB : Mibibytes
        xG   : Gigabytes
        xGiB : Gibibytes
        xT   : Terabytes
        xTiB : Tibibytes
                      """)
                filter = input("Filter [format: <filter-option> <operator> <condition>]: ")

                # Prepare filters
                filter = filter.split()

        # Obtain filter components
        filter_keyword = filter[0]
        filter_operator = filter[1]
        filter_condition = filter[2]

        # Search for files that fits/matches the provided condition and return in a dictionary/key-value mapping
        metasearch_results, standard_stream = search_files_by_metadata(filter_keyword=filter_keyword, filter_operator=filter_operator, filter_condition=filter_condition)

        # Obtain stream
        stdout_msg = standard_stream["stdout"]
        stderr_msg = standard_stream["stderr"]

        # Data Sanitization
        ## Check if flag 'remove_empty' is Enabled
        if remove_empty:
            ## Enabled: : Store only populated keys
            """
            metasearch_results_values:list = metasearch_results["results"]
            i = 0
            while (i <= len(metasearch_results_values)-1):
                # Get current element
                curr_val = metasearch_results_values[i]

                # Get directory name and files
                curr_val_dir_name = curr_val["directory"]
                curr_val_files = curr_val["files"]

                # Check if the files list has items
                print("Number of Files: {}".format(len(curr_val_files)))
                if len(curr_val_files) == 0:
                    # Remove entry from list
                    metasearch_results["results"].pop(i)
                    # Decrement index counter by 1
                    i -= 1
                    # Reset values list
                    metasearch_results_values:list = metasearch_results["results"]

                # Increment index counter
                i += 1
            """
            remove_empty_entries(metasearch_results)

        if len(stderr_msg) == 0:
            # Switch-case the standard output export format
            match output_format:
                case "text":
                    for msg in stdout_msg: print(msg)
                case "json":
                    # Import dictionary object and parse into a JSON object string
                    json_str = dumps(metasearch_results, indent=4)
                    print(json_str)
                case _:
                    print("[-] Invalid output format: {}".format(output_format))
        else:
            print("Standard Error:")
            for stderr in stderr_msg:
                print(stderr)
    else:
        print("No arguments provided.")

if __name__ == "__main__":
    main()

