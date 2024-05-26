# sysenvhndlr : System Environment Variable Buffer Handler/manager

## Information
### Description
- Standing for 'system environment handler', sysenvhndlr is a System Environment Variable Buffer Handler/manager CLI utility
    + designed to make the Input-Processing-Output (I/O Processing) and modification of environment variables easier to work with

### Notes
- Currently sysenvhndlr only supports static parameter specifications (positional-only),
    + however, Optional argument customizations in the form of flags are in the TODO pipeline
- Currently sysenvhndlr is set to return the results as a JSON string and printed to standard output
    + Standard text string is supported as well, will be added to an '--json/-x | --export' optional argument value in a future update

## Setup
### Dependencies

### Pre-Requisites

## Documentations

### Synopsis/Syntax
- Standard
    ```bash
    sysenvhndlr {optionals} <arguments> [action]
    ```

### Parameters
- Positionals
    - action : Specify the action to apply to the environment variables
        + Type: String
        - Actions
            + print : Print the environment variable(s)
            - `split [delimiter/separator]` : Split the environment variable according to a provided deliiter/separator and print the result
                - Parameters
                    - delimiter : Specify the delimiter/separator to split the environment variable values with
                        + Type: String

- Optionals
    - With Arguments
        + '-d | --delimiter <delimiter/separator>' : Parse in the delimiter to split
        + '-e | --environment-variable <variable>' : Append the environment variable you wish to print; Repeat this for every environment variable you wish to work with
        - '-x | --export-format : Export and print the standard output in the specified format
            - Formats:
                + text : (Default) Display standard output as string
                + json : Display results as JSON
    - Flags
        + --hide-header : Hide all environment variable header/title outputs
        + -h | --help : Display help message
        + --show-targets : Print all target environment variables
        + --show-positional-arguments : Show all positional arguments passed
        + --show-optional-arguments : Show all optional arguments passed
        + -v | --version : Display system version information
        + -V | --verbose : Enable verbose output

### Usage
- Print environment variable to Standard Output (stdout)
    ```bash
    sysenvhndlr -e ENV_VAR print
    ```

- Split an environment variable by a delimiter/separator and print to stdout
    - Using positionals
        ```bash
        sysenvhndlr -e ENV_VAR split ';'
        ```
    - Using optionals
        ```bash
        sysenvhndlr -e ENV_VAR split -d ';'
        ```

- Print the environment variable results as a JSON
    ```bash
    sysenvhndlr -e ENV_VAR -x json --hide-header print
    ```

- Print the environment variable results as a JSON and format using jq
    - List the key and values
        ```bash
        sysenvhndlr -e ENV_VAR -x json --hide-header print | jq '.[] | .key, .value'
        ```

- Split the environment variable using a delimiter and print the results as a JSON
    ```bash
    sysenvhndlr -e ENV_VAR -x json --hide-header split -d ';'
    ```

- Split the environment variable using a delimiter, print the results as a JSON and format using jq
    - List the key and values
        ```bash
        sysenvhndlr -e ENV_VAR -x json --hide-header split -d ';' | jq '.[] | .key, .value'
        ```

## Wiki

### Snippets

## TODO

## Resources

## References

## Remarks

