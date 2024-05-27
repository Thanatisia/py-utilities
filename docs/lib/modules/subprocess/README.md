# subprocess : Custom subprocess helper library

## Information

### Module
+ Type: Library/module

### Description
+ Library containing various subprocess helper/support wrapper functions and objects for improving the efficacy of implementing SQLite3 in python projects

## Documentations

### Packages
- pyutils.libraries

### Modules
- pyutils.libraries
    - `.subprocess`

### Classes
- pyutils.libraries.subprocess

### Data Types/Objects

### Functions
- pyutils.libraries.subprocess
    - `.sync_exec(cmd_list:list, **kwargs)`: Synchronously execute command with state communication
        - Parameter Signature/Headers
            - cmd_list : Specify a list of commands to execute
                + Type: List
            - **kwargs : Specify all variable-length keyword arguments you wish to pass into subprocess.Popen()
                + Type: Variable-Length kwargs; Dictionary
        - Notes
            + This is similar to 'execute_command_communicate' except this has kwargs
        - Return
            - res : A List containing the resulting standard streams (stdout, stderr) and the result/return status code
                + Type: List
                - Values
                    - 0 : res_stdout
                        + Type: String
                    - 1 : res_stderr
                        + Type: String
                    - 2 : rc
                        + Type: Integer

    - `.execute_command_communicate(cmd_list, stream_input=None)`: Execute the provided command, as well as the standard input stream data required.
        - Notes
            + The commands are executed in the background by `subprocess.Popen` and only after the program has been successfully completed will it release the standard output, error and return code to the caller
        - Parameter Signature/Headers
            - cmd_list : Specify a list of commands to execute
                + Type: List
            - stream_input : Specify a list of data to be passed into the command's stdin stream
                + Type: List
                + Default: None
        - Return
            - res : A Tuple containing the resulting standard streams (stdout, stderr) and the result/return status code
                + Type: Tuple 
                - Values:
                    + 0 : stdout
                    + 1 : stderr
                    + 2 : retcode

    - `.execute_command_real_time(cmd_list, stream_input=None, ttl_threshold=4)`: Execute the provided command, as well as the standard input stream data required. The commands are printed in real time, line by line
        - Parameter Signature/Headers
            - cmd_list : Specify a list of commands to execute
                + Type: List
            - stream_input : Specify a list of data to be passed into the command's stdin stream
                + Type: List
                + Default: None
            - ttl_threshold : Specify the Time-to-Live max counter before the system closes the process
                + Type: Integer
                + Default: 4
        - Return
            - res : A Tuple containing the resulting standard streams (stdout, stderr) and the result/return status code
                + Type: Tuple 
                - Values:
                    + 0 : stdout
                    + 1 : stderr
                    + 2 : retcode

### Attributes/Variables


### Usage
- Search files according to a metadata filter
    ```python
    import os
    import sys
    from pyutils.libraries.subprocess import sync_exec, PIPE, DEVNULL

    def main():
        # Initialize Variables
        output_format = ["text", "json"][1]
        cmd_to_exec = ["command", "arguments"]

        # Open subprocess to execute the command
        stdout, stderr, rc = sync_exec(cmd_to_exec, stdout=PIPE, stderr=PIPE)

        # Split all of the results into a list
        stdout_spl = stdout.split("\n")

        # Find selected git branch
        for i in range(len(stdout_spl)):
            # Get current element
            curr_stdout = stdout_spl[i]

            print(curr_stdout)

    if __name__ == "__main__":
        main()
    ```

## Wiki

## Resources

## References

## Remarks

