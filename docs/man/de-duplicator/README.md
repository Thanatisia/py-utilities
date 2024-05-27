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
    de-duplicator {optionals} <arguments> [source-target-file] [dataset-source]
    ```

### Parameters
- Positionals
    1. source-target-file : Specify the file name of the target source file containing all your texts which you want to 'unique-fy' by removing the duplicates
        - Type: String
    2. dataset-source : Specify the source/type of URLs that is in the dataset, this is used to split and remove unnessary queries from links. Type 'none' to just remove duplicates and not truncate
        - Sources
            + yt | youtube : For URLs that uses youtube's domain (i.e. youtube.com/...?=search-queries)
            + none : Ignore; just remove duplicates and dont truncate/split

- Optionals
    - With Arguments

    - Flags

### Usage
- Remove duplicates
    ```bash
    de-duplicator source.txt none
    ```

- Sanitize and truncate all URLs belonging to the domain 'youtube.com' by removing the query subdomain strings ('?=query')
    ```bash
    de-duplicator source.txt yt|youtube
    ```

## TODO
+ Optional argument customizations in the form of flags

## Resources

## References

## Remarks

