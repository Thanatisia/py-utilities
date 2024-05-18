"""
Blob/File object handling library
"""
import os
import sys
from json import load, loads, dump, dumps
from pyutils.libraries.treelib import tree_traversal, path_separator
from pyutils.libraries.utils import sizeof_fmt, convert_size_to_num, split_size_suffix

def search_files_by_metadata(filter_operator, filter_condition, filter_keyword="size", top_level_root_dir="."):
    """
    Traverse through all branches and subbranches starting from the top-level root directory and find files based on specific conditions

    :: Params
    - filter_keyword : Specify the metadata search keyword you wish to obtain
        + Type: String
        + Default: size
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

                    # Split the condition into its numerical size and the suffix
                    condition_size, condition_suffix = split_size_suffix(filter_condition)

                    # Check if suffix exists
                    if condition_suffix != "":
                        # Convert the size string of the filter condition to bytes
                        condition_size_bytes = convert_size_to_num(int(condition_size), condition_suffix)
                    else:
                        ## The size is in bytes
                        condition_size_bytes = condition_size

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

