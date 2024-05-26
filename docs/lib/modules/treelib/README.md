# treelib : Operating System tree/branch pathfinder library

## Information

### Module
+ Type: Library/module

### Description
- Library containing functions focusing on moving/traversing around directories, nested subdirectories and throughout the entire root filesystem
    + To map the locations of various files

- Alternative names include:
    + treewalker
    + treegrep

## Documentations

### Packages
- pyutils.libraries

### Modules
- pyutils.libraries
    - `.treelib`

### Classes
- pyutils.libraries.treelib

### Data Types/Objects

### Functions
- pyutils.libraries.treelib
    - `.tree_traversal(top_level_dir=".")`: Walk through all directories and subdirectories starting from the root/top-level directory down the tree
        - Notes
            - os.walk() will return a list of tuples where each tuple is
                """
                [0] = String, Current path
                [1] = Tuple, Nested subdirectories in directory branch
                [2] = Tuple, Files in directory branch
                """
        - Parameter Signature/Headers
            - top_level_dir : Specify the top-level root directory for the traversal to start from
                + Type: String
                + Default: "." (Current working directory)
        - Return
            - tree_branch_mappings : A dictionary containing a Key-Value mapping of all the paths down the tree, branches (aka directories) and sub-branches (aka subdirectories) that the system has traversed to the directories and files found in each path
                + Type: Dictionary
                - Format
                    ```python
                    {
                        path : {
                            directories : [subdirectories in current directory],
                            files : [files in current directory],
                        },
                    }
                    ```

### Attributes/Variables
- pyutils.libraries.treelib
    - OS-specific switching
        - `.path_separator` : Specify the default filepath separator/delimiter
            + Type: String
            + Default Value: `os.path.sep` (Python will detect the operating system and set the path separator/delimiter for the platform automatically)

### Usage
- Search files according to a metadata filter
    ```python
    import os
    import sys
    from pyutils.libraries.treelib import tree_traversal, path_separator

    def main():
        # Initialize Variables
        root_dir:str = "."

        # Get all directories in each tree branch
        tree_branch_mappings = tree_traversal(root_dir)

        # Iterate through all paths and print each files and directories
        for path, contents in tree_branch_mappings.items():
            # Get content key-values
            curr_path_directories = contents["directories"]
            curr_path_files = contents["files"]

            # Print
            print("Path: {}".format(path))
            print("\tDirectories: {}".format(curr_path_directories))
            print("\tFiles: {}".format(curr_path_files))

    if __name__ == "__main__":
        main()
    ```

## Wiki

## Resources

## References

## Remarks

