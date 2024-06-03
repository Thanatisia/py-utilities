"""
De-duplicator CLI utility
"""
import os
import sys
from pyutils.libraries.utils import pprint_info, pprint_error, pprint_warning
from pyutils.libraries.io.files import import_file, export_file
from pyutils.libraries.types.list import sanitizer, find_differences, find_duplicates, order_list, order_lists, remove_duplicates, split_and_replace
from pyutils.libraries.types.dict import merge_dictionary, print_dict

"""
Utilities and application logic functions
"""
def display_help():
    """
    Display help message
    """
    msg="""
Help:

:: Synopsis/Syntax
    {} [options] <arguments> [actions]

:: Parameters
- Positionals
    - actions : Specify the action to run
        - Accepted Values
            - prune : To 'uniquify'/remove duplicates from a list of contents
- Optionals
    - With Arguments
        - `-i | --input-file [input-file-name]` : Specify the name of a file to import into the application buffer memory
        - `-t | --truncate <delimiter|pattern>` : Truncate a given text based on a specified pattern (i.e. family/type/category) of texts (i.e. 'url-links' : remove all search query syntaxes ('?='))
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

- Usage
    - Remove duplicates from the list of contents
        de-duplicate -i [input-file-name] prune

    - Truncate a list of YouTube URLs (containing search queries) by removing the search query strings, then remove duplicates from the list of contents
        de-duplicator -i [input-file-name] [-t|--truncate] <url-search-query|'?='> prune
    """.format(exec_name)
    print(msg)

def display_system_version():
    """
    Display system version
    """
    msg="""
System Version:
    Executable: {}
    Version   : {}
    """.format(exec_name, sys_version)
    print(msg)


"""
System Functions
"""
def init():
    """
    Initialize System Global Information
    """
    global sys_version, exec, exec_path, exec_name, argv, argc, default_filename

    sys_version = "v0.2.1"
    exec = sys.argv[0]
    exec_path = os.path.split(exec)[0]
    exec_name = os.path.split(exec)[1]
    argv = sys.argv[1:]
    argc = len(argv)

    ## Default Values
    default_filename = "source.txt"

def get_cli_arguments():
    """
    Get CLI Arguments
    """
    # Initialize Variables
    i = 0
    line = ""
    opts = {
        "positionals" : [], # Holding positional arguments
        "optionals" : {
            "with-arguments" : {}, # Optionals with arguments
            "flags" : {} # Optional flags (no arguments)
        }
    }

    # Process CLI argument options and flags

    ## Check if arguments are provided
    if argc > 0:
        # Arguments are provided
        # print("Total arguments: {}".format(argc))

        ## Iterate through all arguments as long as its not empty
        while i <= (argc-1):
            # Line still contains input

            # Get next item in the argument
            curr_arg = argv[i]

            # print("{} => {}".format(i, curr_arg))

            # Process current line
            match curr_arg:
                ### Optionals

                #### With Arguments
                case "-i" | "--input-file-name":
                    ## Initialize Variables
                    curr_key = "input-file-name"

                    ## Store the name of the custom file to import
                    ### Check if argument is provided
                    if i+1 < argc:
                        # Get argument value
                        input_filename = argv[i+1]

                        # Check if input file is specified
                        if input_filename != "":
                            # Input file name is specified
                            # Check if current keyword exists, and if not = initialize an entry
                            if not (curr_key in opts["optionals"]["with-arguments"]):
                                opts["optionals"]["with-arguments"][curr_key] = ""

                            # Populate current keyword entry with value
                            opts["optionals"]["with-arguments"][curr_key] = input_filename

                            # Shift 1 position to the left to jump to the next argument
                            i += 1
                        else:
                            # Map the optional to the default value
                            opts["optionals"]["with-arguments"][curr_key] = default_filename
                    else:
                        pprint_warning("Target input file name is not specified.")
                        # Map the optional to the default value
                        opts["optionals"]["with-arguments"][curr_key] = default_filename
                case "-t" | "--truncate":
                    ## Initialize Variables
                    curr_key = "truncate"

                    ## Truncate a given text based on a specified pattern/family of texts (i.e. 'url-links' : remove all search query syntaxes ('?='))
                    ### Check if argument is provided
                    if i+1 < argc:
                        # Get argument value
                        truncate_pattern = argv[i+1]

                        if truncate_pattern != "":
                            # Check if current keyword exists, and if not = initialize an entry
                            if not (curr_key in opts["optionals"]["with-arguments"]):
                                opts["optionals"]["with-arguments"][curr_key] = ""

                            # Populate current keyword entry with value
                            opts["optionals"]["with-arguments"][curr_key] = truncate_pattern

                            # Shift 1 position to the left to jump to the next argument
                            i += 1
                    else:
                        pprint_warning("Target truncate pattern")
                #### Flags
                case "--debug":
                    # Set properties
                    curr_key = "debug"
                    # Check if current keyword exists, and if not = initialize an entry
                    if not (curr_key in opts["optionals"]["flags"]):
                        opts["optionals"]["flags"][curr_key] = 0
                    opts["optionals"]["flags"][curr_key] = 1
                case "-h" | "--help":
                    # Set properties
                    curr_key = "help"
                    # Check if current keyword exists, and if not = initialize an entry
                    if not (curr_key in opts["optionals"]["flags"]):
                        opts["optionals"]["flags"][curr_key] = 0
                    opts["optionals"]["flags"][curr_key] = 1
                case "-v" | "--version":
                    # Set properties
                    curr_key = "version"
                    # Check if current keyword exists, and if not = initialize an entry
                    if not (curr_key in opts["optionals"]["flags"]):
                        opts["optionals"]["flags"][curr_key] = 0
                    opts["optionals"]["flags"][curr_key] = 1
                case "--print-opts-all":
                    # Set properties
                    curr_key = "print-opts-all"
                    # Check if current keyword exists, and if not = initialize an entry
                    if not (curr_key in opts["optionals"]["flags"]):
                        opts["optionals"]["flags"][curr_key] = 0
                    opts["optionals"]["flags"][curr_key] = 1
                case "--print-opts-flags":
                    # Set properties
                    curr_key = "print-opts-flags"
                    # Check if current keyword exists, and if not = initialize an entry
                    if not (curr_key in opts["optionals"]["flags"]):
                        opts["optionals"]["flags"][curr_key] = 0
                    opts["optionals"]["flags"][curr_key] = 1
                case "--print-opts-with-arguments":
                    # Set properties
                    curr_key = "print-opts-with-args"
                    # Check if current keyword exists, and if not = initialize an entry
                    if not (curr_key in opts["optionals"]["flags"]):
                        opts["optionals"]["flags"][curr_key] = 0
                    opts["optionals"]["flags"][curr_key] = 1
                case _:
                    ### Positionals
                    curr_positional_value = argv[i]
                    if curr_positional_value != "":
                        opts["positionals"].append(curr_positional_value)
                    else:
                        # Default action
                        pprint_warning("Invalid option|action provided: {}".format(curr_positional_value))

            # Increment next line
            i += 1
    else:
        pprint_error("No arguments provided")

    # Output and Return
    return opts

def main():
    init()

    # Get CLI arguments
    opts = get_cli_arguments()

    # Process and begin operation

    # Split dictionary into standalone objects
    positionals = opts["positionals"]
    opts_complete = opts["optionals"]
    opt_with_arguments = opts_complete["with-arguments"]
    opt_Flags = opts_complete["flags"]

    ## Iterate through the optional categories
    for opt_category_key, opt_category_values in opts_complete.items():
        for opt_name, opt_value in opt_category_values.items():
            # Switch case and check values
            match opt_name:
                case "help":
                    ## Display help message
                    if opt_value == 1:
                        display_help()
                case "version":
                    ## Display system version information
                    if opt_value == 1:
                        display_system_version()
                case "print-opts-all":
                    ## Print 'opts' associative array containing both flags and options with arguments
                    if opt_value == 1:
                        print_dict(opts)
                case "print-opts-flags":
                    ## Print 'opt_Flags' associative array containing flags
                    if opt_value == 1:
                        print_dict(opt_Flags)
                case "print-opts-with-args":
                    ## Print 'opt_with_arguments' associative array containg options with arguments
                    if opt_value == 1:
                        print_dict(opt_with_arguments)
                case opt_name if not (opt_name in list(opt_category_values.keys())):
                    ## Default: If current option is not in the list
                    print("Invalid optional provided in category [{}]: {}={}".format(opt_category_key, opt_name, opt_value))

    ## Process Positional Arguments
    for i in range(len(positionals)):
        # Get current value
        curr_val = positionals[i]

        # Switch case current key-value
        match curr_val:
            case "prune":
                ## To 'uniquify'/remove duplicates from a list of contents
                ### Obtain the file name
                if "input-file-name" in opt_with_arguments:
                    file_name = opt_with_arguments["input-file-name"]
                else:
                    file_name = default_filename

                # Split file name metadata
                file_name_split = os.path.splitext(file_name)
                file_name_without_extension = file_name_split[0]
                file_ext = file_name_split[1]

                # Check if file exists
                if os.path.isfile(file_name):
                    # File exists

                    # Import file contents using file name
                    file_contents = import_file(file_name)

                    # Sanitize content list
                    original_file_contents = sanitizer(file_contents)

                    pprint_info("Original File Contents: {}".format(original_file_contents))

                    # Check if truncation is specified
                    if "truncate" in opt_with_arguments:
                        # Obtain truncation pattern
                        pattern = opt_with_arguments["truncate"]

                        # Process the truncation patterns to obtain the delimiter
                        match pattern:
                            case "url-search-query":
                                """
                                truncate/split the text by the Web URL search query '?' delimiter
                                """
                                # Initialize variables
                                pattern = "?"

                        pprint_info("Pattern: {}".format(pattern))
                        # Loop through all URLs and remove the elements after the split
                        rem = split_and_replace(file_contents, pattern)

                    # Remove duplicates
                    file_contents = remove_duplicates(file_contents)

                    # Sanitize content list after pruning and 'uniquifying'
                    file_contents = sanitizer(file_contents)

                    # Order the new file contents according to the original (TODO: Fix)
                    # file_contents = order_list(file_contents, original_file_contents)

                    # Check if there are differences (i.e. missing elements) after sanitizing and removing unnecessary strings
                    differences = find_differences(file_contents, original_file_contents)
                    if len(differences) > 0:
                        pprint_warning("There are elements missing:")
                        for i in range(len(differences)):
                            # Get current difference
                            curr_diff = differences[i]
                            # Print
                            print("{} = {}".format(i, curr_diff))
                    else:
                        pprint_info("No discrepancies found after sanitization.")

                    # Find duplicates that was in the original list, remove from the original list and return the new list
                    file_contents, duplicates, duplicates_counter = find_duplicates(file_contents)
                    for k,v in duplicates_counter.items():
                        pprint_warning("Duplicates [Counter: {}] : {}".format(v, k))

                    pprint_info("New File Contents: {}".format(file_contents))

                    # Write new file contents into a file
                    output_file_name = "{}-new{}".format(file_name_without_extension, file_ext)
                    export_file(output_file_name, file_contents)
                else:
                    # File does not exists
                    print("File {} does not exists.".format(file_name))
            case _:
                # Invalid option
                pprint_warning("Invalid action provided: {}".format(curr_val))

if __name__ == "__main__":
    main()

