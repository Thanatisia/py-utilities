"""
Operating System tree/branch pathfinder library

- Library containing functions focusing on moving/traversing around directories, nested subdirectories and throughout the entire root filesystem
    + To map file locations
"""
import os
import sys

# OS-specific switching
path_separator = os.path.sep

def tree_traversal(top_level_dir="."):
    """
    Walk through all directories and subdirectories starting from the root/top-level directory down the tree
    os.walk() will return a list of tuples where each tuple is
        [0] = String, Current path
        [1] = Tuple, Nested subdirectories in directory branch
        [2] = Tuple, Files in directory branch
    """
    # Initialize Variables
    tree_branch_mappings = {
        # path : { directories : [subdirectories in current directory], files : [files in current directory], },
    }

    # Begin walking through the tree and navigate through all nested directories and subdirectories and the files within
    tree_iterable = list(os.walk(top_level_dir))

    # Iterate through tree iterable
    for i in range(len(tree_iterable)):
        # Get current branch
        curr_branch = tree_iterable[i]

        # Get branch tuple objects
        curr_path = curr_branch[0]
        curr_dir_dirs = curr_branch[1]
        curr_dir_files = curr_branch[2]

        # Check if path is in mapping
        if curr_path not in tree_branch_mappings:
            tree_branch_mappings[curr_path] = {"directories" : curr_dir_dirs, "files" : curr_dir_files}
 
    # Output
    return tree_branch_mappings

