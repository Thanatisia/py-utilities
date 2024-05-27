# treewalk : A filesystem tree walker/traversal CLI utility

## Information
### Description
+ A filesystem tree walker/traversal CLI utility that will walk through every branch (directory and subdirectories) from the specified directory as the top-level root

### Notes
- As of v0.2.0,
    + Optional argument customizations in the form of flags are now officially supported
    + Positional argument are now removed in favour of moving to obtaining parameters via optional arguments and setting of default values in case of null/empty-value variables

## Setup
### Dependencies

### Pre-Requisites

## Documentations

### Synopsis/Syntax
- Standard
    ```bash
    treewalk {optionals} <arguments>
    ```

### Parameters
- Positionals

- Optionals
    - With Arguments
        - `-f | --filter <filter-keyword>` : Specify the search/archive targets you wish to scan for (i.e. files, directories or all (both)).
            + Type: String
            + Default: all
            - Filter keywords
                + all : Display all files and (sub)directories found in the tree, branches and subbranches starting from the top level root directory
                + directories : Display all directories found in the tree, branches and subbranches starting from the top level root directory
                + files : Display all files found in the tree, branches and subbranches starting from the top level root directory
        - `-s | --search-category <category>`: Explicitly specify the target search category/topic to find (i.e. tree = Regular Files and Directories, git = git repositories)
            + Type: String
            + Default: tree
            - Search Category/Topic
                + git : Search for git directories down the tree, branches and subbranches starting from the top level root directory
                + tree : Search for regular files and directories down the tree, branches and subbranches starting from the top level root directory
        - `-t | --top-level-root-dir <top-level-root-directory-path>` : Specify the top-level root directory path to start the search.
            + Type: String
            + Default: "."
        - `-x | --export-format <formats>` : Explicitly specify the type/format to export/print the standard output as
            + Type: String
            + Default: text
            - Search Category/Topic
                + text : Regular text format
                + json : Export/Output the result as a parsed JSON-formatted string to standard output
    - Flags
        + -h | --help : Display help message
        + -v | --version : Display system version information
        + -V | --verbose : Enable Verbose output

### Usage
- Default run
    ```bash
    treewalk
    ```

- Default run with all flags
    - Notes
        - This is the same as:
            ```bash
            treewalk -t -x -s -f
            ```
    ```bash
    treewalk -t . -f all -s tree -x text
    ```

- Traverse through the default route with default configurations
    ```bash
    treewalk -t
    ```

- Export result as JSON
    - Notes
        - This is the same as:
            ```bash
            treewalk -t -x json -s -f
            ```
    ```bash
    treewalk -t . -f all -s tree -x json
    ```

- Search all view all files and directories in a path
    ```bash
    treewalk -t [path] -f "all"
    ```

- Search all view all files in a path
    ```bash
    treewalk -t [path] -f "files"
    ```

- Search all view all directories in a path
    ```bash
    treewalk -t [path] -f "directories"
    ```

- Search and list all git directories (and subdirectories) in a path
    ```bash
    treewalk -t [path] -f "all" -s "git"
    ```

## TODO
+ Optional argument customizations in the form of flags

## Resources

## References

## Remarks

