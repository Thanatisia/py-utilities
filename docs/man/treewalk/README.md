# treewalk : A filesystem tree walker/traversal CLI utility

## Information
### Description
+ A filesystem tree walker/traversal CLI utility that will walk through every branch (directory and subdirectories) from the specified directory as the top-level root

### Notes
+ Currently treewalk only supports static parameter specifications (positional-only), however, Optional argument customizations in the form of flags are in the TODO pipeline

## Setup
### Dependencies

### Pre-Requisites

## Documentations

### Synopsis/Syntax
```bash
treewalk {options} <arguments>
```

### Parameters
- Positional
    - top_level_root_dir : Specify the top level root directory you wish to start the walking from
        + Type: String
        + Default: '.' (Current working directory)
    - filters : Filter which key-value you wish to see from the tree results
        + Type: String
        - Keyword Filters
            + all : (Default) display all key-values
            + files : Display files only
            + directories : Display directories only
    - print_topic : Specify a custom type/topic to search
        + Type: String
        - Topics
            + tree : (Default) Print all files/directories/all attributes from all branches in the tree
            + git : Print git repository directories only

- Optionals
    - With Arguments
    - Flags

### Usage
- Search all view all files and directories in a path
    ```bash
    treewalk [path] "all"
    ```

- Search all view all files in a path
    ```bash
    treewalk [path] "files"
    ```

- Search all view all directories in a path
    ```bash
    treewalk [path] "directories"
    ```

- Search and list all git directories (and subdirectories) in a path
    ```bash
    treewalk [path] "all" "git"
    ```

## TODO
+ Optional argument customizations in the form of flags

## Resources

## References

## Remarks

