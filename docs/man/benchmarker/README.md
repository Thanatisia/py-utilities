# benchmarker

## Information
### Description
- Benchmarker CLI utility powered by subproces, the in-package module 'pyutils.libraries.subprocess' and the in-package decorator 'pyutils.decorators.benchmark'
    + That will take in the target command, execute it using subprocess and measure the time, then print the output to standard output

### Notes

## Setup
### Dependencies

### Pre-Requisites

## Documentations

### Synopsis/Syntax
- Standard
    ```bash
    benchmarker {optionals} <arguments>
    ```

### Parameters
- Positionals
    + start : Begin executing the command benchmark with the arguments and stdin stream data

- Optionals
    - With Arguments
        - `--input-file [input-file]` : Import the file into the buffer containing a list of commands you wish to execute, with each command in each line
            - Parameters
                - input-file : Specify the name of the file you wish to import
                    + Type: String
        - `--set-command "[command] <arguments>"` : Set the target command that you wish to execute/benchmark here
            - Parameters
                - command : Specify the command executable you wish to execute/benchmark
                    + Type: String
                - arguments : Specify all the arguments and values you wish to pass to the command to be executed during the benchmark
                    + Type: List
        - `--set-stdin-data "stdin data here"` : Set the standard input stream data you wish to pass into the target command here
            - Parameters
                - stdin-data : Set the standard input stream data you wish to pass into the target command as a user input
                    + Type: String

    - Flags
        + -h | --help : Display help message
        + -v | --version : Display system version

### Usage
- Execute a command
    ```bash
    benchmarker --set-command "ip a s" start
    ```

- Execute a command with stdin stream data
    ```bash
    benchmarker --set-command "ip a s" --set-stdin-data "stdin data here" start
    ```

- Pipe a standard output containing a list of commands you wish to execute and benchmark into benchmarker as a standard input stream
    ```bash
    [command-output] | benchmarker start --
    ```

## TODO
+ Optional argument customizations in the form of flags

## Resources

## References

## Remarks

