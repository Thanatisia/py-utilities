# blob : Blob/File object handling library

## Information

### Module
+ Type: Library/module

### Description
+ Library containing various Blob/File object handling-related functions and objects

## Documentations

### Packages
- pyutils.libraries

### Modules
- pyutils.libraries
    - `.blob`

### Classes
- pyutils.libraries.blob

### Data Types/Objects

### Functions
- pyutils.libraries.blob
    - `.search_files_by_metadata(filter_operator, filter_condition, filter_keyword="size", top_level_root_dir=".")`: Traverse through all branches and subbranches starting from the top-level root directory and find files based on specific conditions
        - Parameter Signature/Header
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

        - Return
            - results : List containing the search results and the standard streams (stdout and stderr)
                + Type: List

### Attributes/Variables


### Usage
- Search files according to a metadata filter
    ```python
    import os
    import sys
    from json import load, loads, dump, dumps
    from pyutils.libraries.blob import search_files_by_metadata

    def main():
        # Initialize Variables
        output_format = ["text", "json"][1]

        # Obtain filter components
        filter_keyword = "size"
        filter_operator = ">"
        filter_condition = "x{B,K,KiB,M,MiB,G,GiB,T,TiB}

        # Search for files that fits/matches the provided condition and return in a dictionary/key-value mapping
        metasearch_results, standard_stream = search_files_by_metadata(filter_keyword=filter_keyword, filter_operator=filter_operator, filter_condition=filter_condition)

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

    if __name__ == "__main__":
        main()
    ```

## Wiki

## Resources

## References

## Remarks

