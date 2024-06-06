# utils : Generic utilities and function library

## Information

### Module
+ Type: Library/module

### Description
+ Library containing Functions and utilities for adding information of various types (debugging, pretty-fying etc)

## Documentations

### Packages
- pyutils.libraries

### Modules
- pyutils.libraries
    - `.utils`

### Classes
- pyutils.libraries.utils

### Data Types/Objects

### Functions
- pyutils.libraries.utils
    - Pretty-Printing
        - `.pprint_error(msg, newline=False, fmt_str="[ERROR]")`: Pretty Printing: Error Messages
            - Parameter Signature/Headers
                - msg : Specify the message you want to pretty print
                    + Type: String
                - newline : Enable/Disable newline formatting
                    + Type: Integer
                - fmt_str : Specify the format string to apply to the message
                    + Type: String
                    + Default: [ERROR] %s

        - `.pprint_info(msg, newline=False, fmt_str="[INFO]")`: Pretty Printing: Information
            - Parameter Signature/Headers
                - msg : Specify the message you want to pretty print
                    + Type: String
                - newline : Enable/Disable newline formatting
                    + Type: Integer
                - fmt_str : Specify the format string to apply to the message
                    + Type: String
                    + Default: [INFO] %s

        - `.pprint_warning(msg, newline=False, fmt_str="[WARNING]")`: Pretty Printing: Warning
            - Parameter Signature/Headers
                - msg : Specify the message you want to pretty print
                    + Type: String
                - newline : Enable/Disable newline formatting
                    + Type: Integer
                - fmt_str : Specify the format string to apply to the message
                    + Type: String
                    + Default: [WARNING] %s

    - Formatting and String/Text modifications
        - `.sizeof_fmt(num, suffix="B", factor=1024.0, spacing=False)`: Format a given size string with the appropriate unit
            - Parameter Signature/Headers
                - num : Specify the size of the file
                    + Type: Integer
                - suffix : Specify the default suffix of the file
                    + Type: String
                    + Default: B
                    - Accepted values
                        + "" : None
                        + "B" : Bytes
                        + "K" : Kilobytes
                        + "Ki" : Kibibytes
                        + "M" : "Megabytes
                        + "Mi" : Mibibytes
                        + "G" : Gigabytes
                        + "Gi" : Gibibytes
                        + "T" : Terabytes
                        + "Ti" : Tibibytes
                        + "P" : Petabytes
                        + "Pi" : Pibibytes
                        + "E"
                        + "Ei"
                        + "Z"
                        + "Zi"
                - factor : Specify the base common denominator/factor between transitioning from one size to another (i.e. 1024.0 is a good factor because 1K = 1024 Bytes, 1M = 1024 Kilobytes, 1G = 1024 Megabytes etc etc)
                    + Type: Float/Double
                    + Default: 1024.0
                - spacing : Enable/Disable the addition of a space between the size and the prefix
                    + Type: Boolean
                    + Default: False

            - Return
                - fmt_str : Returns the formatted string based on the size provided
                    + Type: String

        - `.convert_size_to_num(size, suffix="B", factor=1024)`: Convert a given size to a numerical value based on the provided suffix (i.e. xG, xGiB, xM, xMiB, ...)
            - Parameter Signature/Headers
                - size : Specify the size you wish to convert into numerical form
                    + Type: Integer
                - suffix : Specify the default suffix of the size
                    + Type: String
                    + Default: B
                    - Accepted values
                        + "" : None
                        + "B" : Bytes
                        + "K" : Kilobytes
                        + "Ki" : Kibibytes
                        + "M" : "Megabytes
                        + "Mi" : Mibibytes
                        + "G" : Gigabytes
                        + "Gi" : Gibibytes
                        + "T" : Terabytes
                        + "Ti" : Tibibytes
                        + "P" : Petabytes
                        + "Pi" : Pibibytes
                        + "E"
                        + "Ei"
                        + "Z"
                        + "Zi"
                    - Conversion
                        + 1K = 1024 Bytes
                        + 1M = 1024 Kilobytes
                        + 1G = 1024 Megabytes
                        + 1T = 1024 Gigabytes
                        + 1P = 1024 Terabytes
                - factor : Specify the base common denominator/factor between transitioning from one size to another (i.e. 1024.0 is a good factor because 1K = 1024 Bytes, 1M = 1024 Kilobytes, 1G = 1024 Megabytes etc etc)
                    + Type: Integer
                    + Default: 1024

            - Return
                - num_bytes : Returns the bytes (integer) corresponding to the provided size and suffix
                    + Type: Integer

        - `.split_size_suffix(size_str)`: Split a given size string into its components [0 = Size numeral, 1 = Size Suffix]
            - Parameter Signature/Headers
                - size_str : Specify the human-readable string form of the following format: `x{Suffix}`
                    + Type: String

            - Returns
                - size_split : A List containing the components of the size string after splitting
                    + Type: List
                    - Values/Elements
                        + 0 : Size Digit/Numeral
                        + 1 : Size Suffix
                    - Examples
                        + xB => [x, 'B']
                        + xK => [x, 'K']
                        + xKiB => [x, 'KiB']
                        + xG => [x, 'G']
                        + xGiB => [x, 'GiB']
                        + xM => [x, 'M']
                        + xMiB => [x, 'MiB']
    - Progress Bar
        - `.progressbar(tasks, min=0)`: Progress Bar for tracking the execution of a list of multiple tasks (mapped to the arguments) with printing on the same line
            - Parameter Signature/Header
                - tasks : Specify a list of dictionaries containing the task function object mapped to the arguments
                    + Type: List<Dictionary>
                    - Format
                        ```python
                        [
                            {
                                "function" : function,
                                "arguments" : args,
                            }
                        ]
                        ```
                - min : Specify the lower-bound/minimum value to start the progress bar counting from
                    + Type: Integer
                    + Default: 0

### Attributes/Variables


### Usage
- Pretty printing
    - Information
        ```python
        import os
        import sys
        from pyutils.libraries.utils import pprint_info

        def main():
            pprint_info("This is an information!")

        if __name__ == "__main__":
            main()
        ```
    - Error
        ```python
        import os
        import sys
        from pyutils.libraries.utils import pprint_error

        def main():
            pprint_error("This is an error!")

        if __name__ == "__main__":
            main()
        ```
    - Warning
        ```python
        import os
        import sys
        from pyutils.libraries.utils import pprint_warning

        def main():
            pprint_warning("This is a warning!")

        if __name__ == "__main__":
            main()
        ```

- Size handling
    - Splitting a human-readable size string into its constituent parts
        ```python
        import os
        import sys
        from pyutils.libraries.utils import split_size_suffix

        def main():
            # Initialize Variables
            size_str = "xK"

            # Split size string into parts
            size, size_suffix = split_size_suffix(size_str)

            # Print results
            print("Size: {}".format(int(size)))
            print("Suffix: {}".format(suffix))

        if __name__ == "__main__":
            main()
        ```

- Progress Bar
    ```python
    tasks:list = [
        {
            "function" : os.getenv,
            "arguments" : ["HOME"]
        },
        {
            "function" : print,
            "arguments" : ["Hello World"]
        },
        {
            "function" : print,
            "arguments" : ["Hello World"]
        },
    ]
    res = progressbar_decorator(tasks)
    print("Results: {}".format(res))
    ```

## Wiki

## Resources

## References
+ [StackOverflow - Get a human-readable version of a file size](https://stackoverflow.com/questions/1094841/get-a-human-readable-version-of-a-file-size)

## Remarks

