"""
File Metadata searcher/filter

- Search for all files according to a specific metadata category, keyword, filter value or condition
"""
import os
import sys
from json import load, loads, dump, dumps
from pyutils.libraries.treelib import tree_traversal, path_separator
from pyutils.libraries.utils import sizeof_fmt, convert_size_to_num, split_size_suffix

def search_metadata(filter_keyword, filter_operator, filter_condition, top_level_root_dir="."):
    """
    Traverse through all branches and subbranches starting from the top-level root directory and find files based on specific conditions

    :: Params
    - filter_keyword : Specify the metadata search keyword you wish to obtain
        + Type: String
        - Metadata categories
            + size : Obtain all files based on a size range
    - filter_operator : Specify the comparison operator to apply to the metadata search range
        + Type: String
        - Operators
            + 'gt' | '>'  : Greater than
            + 'ge' | '>=' : Greater than or Equals to
            + 'lt' | '>'  : Less than
            + 'le' | '>=' : Less than or Equals to
            + 'ne' | '!=' : Not Equals to
            + 'eq' | '==' : Equals to
    - filter_condition : Specify the condition value to search for
        + Type: String
        - Filter Conditions:
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
    """
    # Initialize Variables
    standard_stream = {
        "stdout" : [],
        "stderr" : []
    }
    ## Initialize metasearch results dictionary entry for this file
    metasearch_results = {
        ## Contains Search results
        ## Key = directory path
        ## Values = { keyword : { operator : { condition : [elements, that, matched, this, condition] } }
        # filter_keyword : {filter_operator : {filter_condition : []}}
        "filter" : {
            "keyword" : filter_keyword,
            "operator" : filter_operator,
            "condition" : filter_condition,
        },
        "results" : [],
    }

    # Dive through the tree starting from the top-level root directory
    tree_mappings = tree_traversal(top_level_root_dir)

    standard_stream["stdout"].append("[i] Filter Keyword: {}".format(filter_keyword))
    standard_stream["stdout"].append("[i] Filter Operator: {}".format(filter_operator))

    # Iterate through the tree mappings and search the metadata of the files
    for dir_name, dir_values in tree_mappings.items():
        # Get directory contents
        dir_subdirectories = dir_values["directories"]
        dir_files = dir_values["files"]

        # Initialize a new results entry if it doesnt exist
        metasearch_results["results"].append({"directory" : dir_name, "files" : []})

        # Get current index of the search results list
        curr_idx = len(metasearch_results["results"])-1

        ## Iterate through all files and check the metadata of the file based on filter
        for file in dir_files:
            # Format full file path
            full_filepath = os.path.join(dir_name, file)

            # Filter and search current file's metadata and check if it matches the criteria/filter
            match filter_keyword:
                case "size":
                    # Get the metadata of the current file
                    curr_file_metadata = os.path.getsize(full_filepath)

                    # Convert the size string of the filter condition to bytes
                    condition_size, condition_suffix = split_size_suffix(filter_condition)
                    condition_size_bytes = convert_size_to_num(int(condition_size), condition_suffix)

                    ## Filter by size checking
                    match filter_operator:
                        case ">" | "gt":
                            ## Size is greater than a certain value
                            if curr_file_metadata > int(condition_size_bytes):
                                # Append the standard output message
                                standard_stream["stdout"].append("[i] Current File [{}] = {}".format(full_filepath, "Greater than"))
                                # Append the files to the list
                                metasearch_results["results"][curr_idx]["files"].append(file)
                        case ">=" | "ge":
                            ## Size is greater than or equals to a certain value
                            if curr_file_metadata >= int(condition_size_bytes):
                                # Append the standard output message
                                standard_stream["stdout"].append("[i] Current File [{}] = {}".format(full_filepath, "Greater than or Equals to"))
                                # Append the files to the list
                                metasearch_results["results"][curr_idx]["files"].append(file)
                        case "<" | "lt":
                            ## Size is less than a certain value
                            if curr_file_metadata < int(condition_size_bytes):
                                # Append the standard output message
                                standard_stream["stdout"].append("[i] Current File [{}] = {}".format(full_filepath, "Less than"))
                                # Append the files to the list
                                metasearch_results["results"][curr_idx]["files"].append(file)
                        case "<=" | "le":
                            ## Size is less than or equals to a certain value
                            if curr_file_metadata <= int(condition_size_bytes):
                                # Append the standard output message
                                standard_stream["stdout"].append("[i] Current File [{}] = {}".format(full_filepath, "Less than or Equals to"))
                                # Append the files to the list
                                metasearch_results["results"][curr_idx]["files"].append(file)
                        case "!=" | "ne":
                            ## Size is equals to a certain value
                            if curr_file_metadata != int(condition_size_bytes):
                                # Append the standard output message
                                standard_stream["stdout"].append("[i] Current File [{}] = {}".format(full_filepath, "Equals to"))
                                # Append the files to the list
                                metasearch_results["results"][curr_idx]["files"].append(file)
                        case "==" | "eq":
                            ## Size is equals to a certain value
                            if curr_file_metadata == int(condition_size_bytes):
                                # Append the standard output message
                                standard_stream["stdout"].append("[i] Current File [{}] = {}".format(full_filepath, "Equals to"))
                                # Append the files to the list
                                metasearch_results["results"][curr_idx]["files"].append(file)
                        case _:
                            ## Invalid operator
                            standard_stream["stderr"].append("[-] {} : Invalid Operator".format(filter_operator))
                case _:
                    ## Invalid keyword  
                    standard_stream["stderr"].append("[-] {} : Invalid Keyword".format(filter_keyword))

    # Output/Return
    return [metasearch_results, standard_stream]

def main():
    # Initialize Variables
    top_level_root_dir = "."
    stdout_msg = [] # List of messages to print to standard output
    filter = ""
    output_format = ["text", "json"][1] # Specify the standard output export format. Options: text (Default), json

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

        """
        ## Initialize metasearch results dictionary entry for this file
        metasearch_results = {
            ## Contains Search results
            ## Key = directory path
            ## Values = { keyword : { operator : { condition : [elements, that, matched, this, condition] } }
            # filter_keyword : {filter_operator : {filter_condition : []}}
            "filter" : {
                "keyword" : filter_keyword,
                "operator" : filter_operator,
                "condition" : filter_condition,
            },
            "results" : [],
        }

        # Dive through the tree starting from the top-level root directory
        tree_mappings = tree_traversal(top_level_root_dir)

        stdout_msg.append("[i] Filter Keyword: {}".format(filter_keyword))
        stdout_msg.append("[i] Filter Operator: {}".format(filter_operator))

        # Iterate through the tree mappings and search the metadata of the files
        for dir_name, dir_values in tree_mappings.items():
            # Get directory contents
            dir_subdirectories = dir_values["directories"]
            dir_files = dir_values["files"]

            # Initialize a new results entry if it doesnt exist
            metasearch_results["results"].append({"directory" : dir_name, "files" : []})

            # Get current index of the search results list
            curr_idx = len(metasearch_results["results"])-1

            ## Iterate through all files and check the metadata of the file based on filter
            for file in dir_files:
                # Format full file path
                full_filepath = os.path.join(dir_name, file)

                # Filter and search current file's metadata and check if it matches the criteria/filter
                match filter_keyword:
                    case "size":
                        # Get the metadata of the current file
                        curr_file_metadata = os.path.getsize(full_filepath)

                        # Convert the size string of the filter condition to bytes
                        condition_size, condition_suffix = split_size_suffix(filter_condition)
                        condition_size_bytes = convert_size_to_num(int(condition_size), condition_suffix)

                        ## Filter by size checking
                        match filter_operator:
                            case ">" | "gt":
                                ## Size is greater than a certain value
                                if curr_file_metadata > int(condition_size_bytes):
                                    # Append the standard output message
                                    stdout_msg.append("[i] Current File [{}] = {}".format(full_filepath, "Greater than"))
                                    # Append the files to the list
                                    metasearch_results["results"][curr_idx]["files"].append(file)
                            case ">=" | "ge":
                                ## Size is greater than or equals to a certain value
                                if curr_file_metadata >= int(condition_size_bytes):
                                    # Append the standard output message
                                    stdout_msg.append("[i] Current File [{}] = {}".format(full_filepath, "Greater than or Equals to"))
                                    # Append the files to the list
                                    metasearch_results["results"][curr_idx]["files"].append(file)
                            case "<" | "lt":
                                ## Size is less than a certain value
                                if curr_file_metadata < int(condition_size_bytes):
                                    # Append the standard output message
                                    stdout_msg.append("[i] Current File [{}] = {}".format(full_filepath, "Less than"))
                                    # Append the files to the list
                                    metasearch_results["results"][curr_idx]["files"].append(file)
                            case "<=" | "le":
                                ## Size is less than or equals to a certain value
                                if curr_file_metadata <= int(condition_size_bytes):
                                    # Append the standard output message
                                    stdout_msg.append("[i] Current File [{}] = {}".format(full_filepath, "Less than or Equals to"))
                                    # Append the files to the list
                                    metasearch_results["results"][curr_idx]["files"].append(file)
                            case "==" | "eq":
                                ## Size is equals to a certain value
                                if curr_file_metadata == int(condition_size_bytes):
                                    # Append the standard output message
                                    stdout_msg.append("[i] Current File [{}] = {}".format(full_filepath, "Equals to"))
                                    # Append the files to the list
                                    metasearch_results["results"][curr_idx]["files"].append(file)
                            case _:
                                ## Invalid operator
                                print("[-] {} : Invalid Operator".format(filter_operator))
                    case _:
                        ## Invalid keyword  
                        print("[-] {} : Invalid Keyword".format(filter_keyword))
        """
        metasearch_results, standard_stream = search_metadata(filter_keyword, filter_operator, filter_condition)

        # Obtain stream
        stdout_msg = standard_stream["stdout"]
        stderr_msg = standard_stream["stderr"]

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

