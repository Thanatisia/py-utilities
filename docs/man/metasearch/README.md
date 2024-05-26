# metasearch : File Metadata searcher/filter

## Information
### Description
+ File finder/searcher that  Search for all files according to a specific metadata category, keyword, filter value or condition

### Notes
- Currently metasearch only supports static parameter specifications (positional-only),
    + however, Optional argument customizations in the form of flags are in the TODO pipeline
- Currently metasearch is set to return the results as a JSON string and printed to standard output
    + Standard text string is supported as well, will be added to an '--json/-x | --export' optional argument value in a future update

## Setup
### Dependencies

### Pre-Requisites

## Documentations

### Synopsis/Syntax
- Standard
    ```bash
    metasearch {optionals} <arguments> [filter]
    ```

### Parameters
- Positionals
    - filter : Specify the filter condition string used to filter the files found. The filter condition is in the format of `"[keyword] [operator] [condition]"`
        - Parameters
            - keyword : Specify the metadata category you wish to filter while searching for a file
                - Filter Keywords:
                    + size: Filter by size
            - operator : Specify the comparison operator you wish to use to filter the conditional value corresponding to the metadata category of choice
                - Operators
                    + 
            - condition : Specify the filter condition corresponding to the metadata category of choice
                - Filter Conditions
                    - size
                        + xB   : Bytes
                        + xK   : Kilobytes
                        + xKiB : Kibibytes
                        + xM   : Megabytes
                        + xMiB : Mibibytes
                        + xG   : Gigabytes
                        + xGiB : Gibibytes
                        + xT   : Terabytes
                        + xTiB : Tibibytes

- Optionals
    - With Arguments

    - Flags

### Usage
- Search for files more than a specific size
    ```bash
    metasearch "size > x{B,K,KiB,M,MiB,G,GiB,T,TiB}"
    ```

- Using jq to filter the results in JSON string output
    - files
        ```bash
        metasearch "size > x{B,K,KiB,M,MiB,G,GiB,T,TiB}" | jq '.results | .[].files[]'
        ```

## TODO
+ Optional argument customizations in the form of flags

## Resources

## References

## Remarks

