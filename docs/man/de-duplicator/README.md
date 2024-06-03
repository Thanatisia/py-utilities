# de-duplicator

## Information
### Description
+ de-duplicator is as the name suggests, a simple CLI utility that will take in the contents of the provided file, remove all duplicates, and output to a new text file.
+ If a dataset source is specified, it will sanitize/truncate the URLs within accordingly (to be removed)

### Notes
- Currently de-duplicator only supports static parameter specifications (positional-only),
    + however, Optional argument customizations in the form of flags are in the TODO pipeline

## Setup
### Dependencies

### Pre-Requisites

## Documentations

### Synopsis/Syntax
- Standard
    ```bash
    de-duplicator {optionals} <arguments> [actions]
    ```

### Parameters
- Positionals
    - actions : Specify the action to run
        - Accepted Values
            - prune : To 'uniquify'/remove duplicates from a list of contents
- Optionals
    - With Arguments
        - `-i | --input-file [input-file-name]` : Specify the name of a file to import into the application buffer memory
            - Options
                - input-file-name : The name of the target file to import into the application buffer memory
                    + Type: String
                    + Default Value: source.txt
        - `-t | --truncate <delimiter|pattern>` : Truncate a given text based on a specified pattern (i.e. family/type/category) of texts (i.e. 'url-links' : remove all search query syntaxes ('?='))
            - Notes
                + If a pattern is not specified/invalid, this option will be ignored
            - Values
                - delimiter : If the text you wish to truncate contains a specific delimiter and you want to keep only the sections before the specified delimiter
                    - Special Delimiter Keywords
                        - url-search-query : Truncate the URL by removing the search query pattern from the web URL (aka links), if available
                            + Delimiter/Pattern: ?=
                            - Notes
                                + Useful for cleaning up links (such as youtube shortened links where there is a search query appended to the back of the URLs) and keeping web URLs of the same format synchronized
                - pattern : (WIP) If the list contains contents related to an application/"family" of texts (i.e. General URL links, Youtube Links)
    - Flags
        + --debug : Set program to 'debug mode'; All commands will be printed out instead
        + -h | --help : Display help message
        + -v | --version : Display system version
        + --print-opts-all : Print all optionals (with arguments and flags)
        + --print-opts-with-arguments : Print all optionals with arguments
        + --print-opts-flags : Print all flags (optionals without arguments)

### Usage
- Remove duplicate contents from the default file (source.txt)
    ```bash
    de-duplicator prune
    ```

- Remove duplicate contents from a custom file
    ```bash
    de-duplicator -i [input-file-name] prune
    ```

- Truncate the file contents by removing the provided delimiter/patterns, then remove duplicates from the list of contents
    - Example Use Cases
        - youtube URL
            + Truncating/Sanitizing a list of YouTube URLs (containing search queries) by removing the search query strings (?=)
    ```bash
    de-duplicator [-t|--truncate] <url-search-query|'?='|delimiter> prune
    ```

## TODO
+ Optional argument customizations in the form of flags

## Resources

## References

## Remarks

