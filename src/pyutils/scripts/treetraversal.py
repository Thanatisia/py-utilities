"""
Walking through all files and subdirectories in the top level root directory down the separate branches
"""
import os
import sys
from pyutils.libraries.treelib import tree_traversal, path_separator

def print_tree_branches(tree_branch_mappings, filters="all"):
    """
    Print the tree branch mappings
    """
    match filters:
        case "all":
            ## Print all keys
            for k,v in tree_branch_mappings.items():
                print("{} = {}".format(k,v))
        case "files":
            # Print files only
            for k,v in tree_branch_mappings.items():
                curr_branch_files = v["files"]
                print("{} = {}".format(k,curr_branch_files))
        case "directories":
            # Print directories only
            for k,v in tree_branch_mappings.items():
                curr_branch_directories = v["directories"]
                print("{} = {}".format(k,curr_branch_directories))
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

def print_git_repositories(top_level_root_dir=".", delimiter="="):
    """
    Get and print all git repositories at the top level directory down
    """
    all_git_dirs = get_git_repositories(root_dir=top_level_root_dir)

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

def main():
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

    # Initialize Variables
    top_level_root_dir = "."
    filters = "all"
    print_topic = "tree"

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

    match print_topic:
        case "tree":
            tree_branch_mappings = tree_traversal(top_level_root_dir)
            print_tree_branches(tree_branch_mappings, filters=filters)
        case "git":
            print_git_repositories(top_level_root_dir)

if __name__ == "__main__":
    main()

