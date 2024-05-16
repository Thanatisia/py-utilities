"""
Walking through all files and subdirectories in the top level root directory down the separate branches
"""
import os
import sys
from json import load, loads, dump, dumps
from pyutils.libraries.treelib import tree_traversal, path_separator

def print_tree_branches(tree_branch_mappings, filters="all", delimiter="=", stdout_type="json", json_dump_opts={"indent" : 4}):
    """
    Print the tree branch mappings

    :: Params
    - top_level_root_dir : Specify the top level root directory to begin searching from
        + Type: String
        + Default: '.'

    - filters : Specify the filter topic you wish to view from the standard output
        + Type: String
        + Default: all
        - Filters
            + all : Display all key-values
            + directories : Display directories only
            + files : Display files only

    - delimiter : Specify the delimiter to map the directory name to the parent directory path
        + Type: String
        + Default: '='

    - stdout_type : Specify the type of standard output to print the results with
        + Type: String
        + Default: 'text'
        - Standard output formats
            + text
            + dictionary (aka JSON)

    - json_dump_opts : Specify a dictionary containing the options you wish to pass into 'json.dumps()'
        + Type: Dictionary
        - Default
            {
                "indent" : 4
            }
    """
    match filters:
        case "all":
            # Switch case the standard output format
            match stdout_type:
                case "text":
                    ## Print all keys
                    for k,v in tree_branch_mappings.items():
                        print("{} {} {}".format(k, delimiter, v))
                case "json":
                    # Initialize variables
                    json_contents = {}

                    for k,v in tree_branch_mappings.items():
                        # Map the directory name to the paths
                        json_contents[k] = v

                    # Format the dictionary object into a JSON string
                    json_str = dumps(json_contents, **json_dump_opts)

                    # Print the JSON string
                    print(json_str)
        case "files":
            # Switch case the standard output format
            match stdout_type:
                case "text":
                    # Print files only
                    for k,v in tree_branch_mappings.items():
                        curr_branch_files = v["files"]
                        print("{} {} {}".format(k, delimiter, curr_branch_files))
                case "json":
                    # Initialize variables
                    json_contents = {}

                    for k,v in tree_branch_mappings.items():
                        # Obtain file vlaues
                        curr_branch_files = v["files"]
                        # Map the directory name to the paths
                        json_contents[k] = curr_branch_files

                    # Format the dictionary object into a JSON string
                    json_str = dumps(json_contents)

                    # Print the JSON string
                    print(json_str)
        case "directories":
            # Switch case the standard output format
            match stdout_type:
                case "text":
                    # Print directories only
                    for k,v in tree_branch_mappings.items():
                        curr_branch_directories = v["directories"]
                        print("{} {} {}".format(k, delimiter, curr_branch_directories))
                case "json":
                    # Initialize variables
                    json_contents = {}

                    for k,v in tree_branch_mappings.items():
                        # Obtain file vlaues
                        curr_branch_directories = v["directories"]
                        # Map the directory name to the paths
                        json_contents[k] = curr_branch_directories

                    # Format the dictionary object into a JSON string
                    json_str = dumps(json_contents)

                    # Print the JSON string
                    print(json_str)
        case _:
            print("Invalid format: {}".format(format))

def get_git_repositories(root_dir="."):
    """
    Get git repositories based on the .git identifier
    """
    # Initialize Variables
    all_git_dirs = []

    # Get all directories in each tree branch
    tree_branch_mappings = tree_traversal(root_dir)
    for k,v in tree_branch_mappings.items():
        curr_dir_dirs = v["directories"]

        # Check if curr_obj is a directory called .git
        if ".git" in curr_dir_dirs:
            # Is a .git
            all_git_dirs.append(k)

    return all_git_dirs

def print_git_repositories(top_level_root_dir=".", delimiter="=", stdout_type="text", json_dump_opts={"indent" : 4}):
    """
    Get and print all git repositories at the top level directory down

    :: Params
    - top_level_root_dir : Specify the top level root directory to begin searching from
        + Type: String
        + Default: '.'

    - delimiter : Specify the delimiter to map the directory name to the parent directory path
        + Type: String
        + Default: '='

    - stdout_type : Specify the type of standard output to print the results with
        + Type: String
        + Default: 'text'
        - Standard output formats
            + text
            + dictionary (aka JSON)

    - json_dump_opts : Specify a dictionary containing the options you wish to pass into 'json.dumps()'
        + Type: Dictionary
        - Default
            {
                "indent" : 4
            }
    """
    all_git_dirs = get_git_repositories(root_dir=top_level_root_dir)

    # Switch case the standard output format
    match stdout_type:
        case "text":
            # print("All git repositories: {}".format(all_git_dirs))
            print("Name {} Parent".format(delimiter))
            for dir in all_git_dirs:
                # Split directory into parts
                dir_parts = dir.split(path_separator)
                # Get every element in the list until the second last element, and merge them together with the "/" delimiter
                dir_parents = path_separator.join(dir_parts[:-1])
                # Get the last element in the list
                dir_name = dir_parts[::-1][0]
                print("{} {} {}".format(dir_name, delimiter, dir_parents))
        case "json":
            # Initialize variable
            json_contents = {}
            for dir in all_git_dirs:
                # Split directory into parts
                dir_parts = dir.split(path_separator)
                # Get every element in the list until the second last element, and merge them together with the "/" delimiter
                dir_parents = path_separator.join(dir_parts[:-1])
                # Get the last element in the list
                dir_name = dir_parts[::-1][0]
                # Map the directory name to the paths
                json_contents[dir_name] = dir_parents

            # Format the dictionary object into a JSON string
            json_str = dumps(json_contents, **json_dump_opts)

            # Print the JSON string
            print(json_str)
        case _:
            # Invalid type
            print("[-] Invalid type provided: {}".format(stdout_type))

def main():
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

    # Initialize Variables
    top_level_root_dir = "."
    filters = "all"
    print_topic = "tree"
    stdout_type = "text"

    match argc:
        case 1:
            top_level_root_dir = argv[0]
        case 2:
            top_level_root_dir = argv[0]
            filters = argv[1]
        case 3:
            top_level_root_dir = argv[0]
            filters = argv[1]
            print_topic = argv[2]
        case 4:
            top_level_root_dir = argv[0]
            filters = argv[1]
            print_topic = argv[2]
            stdout_type = argv[3]

    match print_topic:
        case "tree":
            tree_branch_mappings = tree_traversal(top_level_root_dir)
            print_tree_branches(tree_branch_mappings, filters=filters, stdout_type=stdout_type)
        case "git":
            print_git_repositories(top_level_root_dir, stdout_type=stdout_type)

if __name__ == "__main__":
    main()

