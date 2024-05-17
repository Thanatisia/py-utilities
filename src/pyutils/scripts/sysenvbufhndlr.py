"""
System Environment Variable Buffer Handler/manager
"""
import os
import sys
from json import load, loads, dump, dumps

def init():
    """
    Pre-Initialization function
    """
    global app_name, app_vers, exec, argv, argc
    # Initialize application information
    app_name = "sysenvhndlr"
    app_vers = "v0.1.0"

    # Get command line arguments
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

def display_help():
    """
    Display help message
    """
    msg = f"""
Synopsis/Syntax
    {app_name} <options> <arguments> [action]

Parameters:
    - Positionals
        - action : Specify the action to apply to the environment variables
            + Type: String
            - Actions
                + print : Print the environment variable(s)
                - 'split [delimiter/separator]' : Split the environment variable according to a provided deliiter/separator and print the result
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
            + --hide-header
            + -h | --help
            + --show-targets
            + --show-positional-arguments
            + --show-optional-arguments
            + -v | --version
            + -V | --verbose

Usage:
    - Print environment variable to Standard Output (stdout)
        {app_name} -e ENV_VAR print

    - Split an environment variable by a delimiter/separator and print to stdout
        - Using positionals
            {app_name} -e ENV_VAR split ;
        - Using optionals
            {app_name} -e ENV_VAR split -d ;
    """
    print(msg)

def display_system_version():
    """
    Display system version
    """
    vers = """
Name: {}
Version: {}
    """.format(app_name, app_vers)
    print(vers)

def get_cli_arguments():
    """
    Obtain and get CLI arguments parsed by the user
    """
    # Initialize Variables
    argparsed = {
        "positionals" : [],
        "optionals" : {
            "with-arguments" : {
                "delimiter" : "",
                "environment-variables" : [],
                "export-format" : "text",
            },
            "flags" : {
                "hide-header" : False,
                "help" : False,
                "show-targets" : False,
                "show-positional-arguments" : False,
                "show-optional-arguments" : False,
                "verbose" : False,
                "version" : False,
            }
        }
    }
    i = 0

    # Iterate and process and filter command line argument key-values
    if argc > 0:
        while i < argc:
            # Get current argument
            curr_arg = argv[i]

            # Switch-case check current argument
            match curr_arg:
                case "-d" | "--delimiter":
                    ## Check if index i+1 (next element) is provided
                    next_index = i+1
                    if next_index <= argc-1:
                        ## Next index is less than or equals to the entire argument counter (last element): Is provided
                        ## Get delimiter argument (if provided)
                        delimiter = argv[next_index]

                        ## Set a delimiter/separator for use
                        argparsed["optionals"]["with-arguments"]["delimiter"] = delimiter

                        # Increment index to skip the next element
                        i += 1
                    else:
                        print("[-] Delimiter is not specified")
                        exit(1)
                case "-e" | "--environment-variable":
                    ## Append the environment variable you wish to print; Repeat this for every environment variable you wish to work with
                    ## Check if index i+1 (next element) is provided
                    next_index = i+1
                    if next_index <= argc-1:
                        ## Next index is less than or equals to the entire argument counter (last element): Is provided
                        ## Get delimiter argument (if provided)
                        env = argv[next_index]

                        ## Set a delimiter/separator for use
                        argparsed["optionals"]["with-arguments"]["environment-variables"].append(env)

                        # Increment index to skip the next element
                        i += 1
                    else:
                        print("[-] Environment Variable is not specified")
                        exit(1)
                case "-x" | "--export-format":
                    ## Export and print the standard output in the specified format
                    ## Formats:
                    ## - text : (Default) Display standard output as string
                    ## - json : Display results as JSON

                    ## Supported Formats
                    supported_formats = ["text", "json"]

                    ## Check if index i+1 (next element) is provided
                    next_index = i+1
                    if next_index <= argc-1:
                        ## Next index is less than or equals to the entire argument counter (last element): Is provided
                        ## Get delimiter argument (if provided)
                        format = argv[next_index]

                        # Check if format is in the supported_formats list
                        if not (format.lower() in supported_formats):
                            # Not in the list, default to 'text'
                            print("[-] Specified export format [{}] is not supported, defaulting to 'text'".format(format))
                            format = "text"

                        # Increment index to skip the next element
                        i += 1
                    else:
                        print("[-] Export Format is not specified, defaulting to 'text'")
                        format = "text"

                    ## Set a delimiter/separator for use
                    argparsed["optionals"]["with-arguments"]["export-format"] = format
                case "--hide-header":
                    ## Hide the header message when printing the environment variable
                    argparsed["optionals"]["flags"]["hide-header"] = True
                case "-h" | "--help":
                    ## Display help menu
                    argparsed["optionals"]["flags"]["help"] = True
                case "--show-targets":
                    ## Show all specified environment variables
                    argparsed["optionals"]["flags"]["show-targets"] = True
                case "--show-positional-arguments":
                    ## Show all positional arguments
                    argparsed["optionals"]["flags"]["show-positional-arguments"] = True
                case "--show-optional-arguments":
                    ## Show all optional arguments (with arguments + flags)
                    argparsed["optionals"]["flags"]["show-optional-arguments"] = True
                case "-v" | "--version":
                    ## Display system version
                    argparsed["optionals"]["flags"]["version"] = True
                case "-V" | "--verbose":
                    ## Display information message
                    argparsed["optionals"]["flags"]["verbose"] = True
                case _:
                    ## Default value: Positionals
                    argparsed["positionals"].append(curr_arg)

            # Increment the counter to skip to the next index
            i += 1
    else:
        print("[i] No arguments provided.")
        exit(1)

    return argparsed

def main():
    # Perform system initialization
    init()

    # Get CLI arguments parsed
    argparsed = get_cli_arguments()

    # Initialize Variables
    positionals = argparsed["positionals"]
    optionals = argparsed["optionals"]
    optional_with_Arguments = optionals["with-arguments"]
    optional_Flags = optionals["flags"]
    number_of_positionals = len(positionals)
    number_of_options_with_arguments = len(optional_with_Arguments)
    number_of_options_Flags = len(optional_Flags)
    json_objects = []

    # Iterate through optionals
    for opt_category,opt_category_values in optionals.items():
        # Dive into subdictionaries
        for opt_key,opt_value in opt_category_values.items():
            # Switch-case and filter the optional key-values
            match opt_key:
                case "delimiter":
                    ## Obtain the delimiter
                    delimiter = opt_value
                case "help":
                    ## Display help menu
                    if opt_value == True:
                        print("Display help menu")
                        display_help()
                        exit(1)
                case "version":
                    ## Display system version information
                    if opt_value == True:
                        print("Display system version information")
                        display_system_version()
                        exit(1)
                case opt_key if not (opt_key in list(opt_category_values.keys())):
                    ## Optional key is not found in the current dictionary
                    print("[-] Invalid optional: {}".format(opt_key))

    # Get all environment variables
    env_vars = optional_with_Arguments["environment-variables"]
    number_of_env_vars = len(env_vars)

    # Check if environment variables are specified
    if number_of_env_vars == 0:
        ## No environment variables, obtain from positionals
        print("No environment variables specified, please specify at least 1 environment variable using ['-e' or '--environment-variable' <your-environment-variable>].")
    else:
        # Display pre-program information here (if enabled)
        if optional_Flags["show-targets"] == True:
            print("[i] Environment Variables: {}".format(env_vars))

        if optional_Flags["show-positional-arguments"] == True:
            print("[i] Positional Arguments: {}".format(positionals))

        if optional_Flags["show-optional-arguments"] == True:
            print("[i] Optional Arguments: {}".format(optional_with_Arguments))
            print("[i] Optional Flags: {}".format(optional_Flags))

        print("")

        # Check if positionals provided
        if number_of_positionals > 0:
            # Iterate through all environment variables
            for i in range(number_of_env_vars):
                # Get current environment variable
                curr_env_key = env_vars[i]

                # Import Environment Variable
                env_value = os.getenv(curr_env_key)

                # Check if environment variable is set (os.env() will return None if not set)
                if env_value != None:
                    if number_of_positionals > 0:
                        action = positionals[0]
                    else:
                        # Get action to be taken
                        action = input("Action [print|split]: ")

                    if optional_Flags["verbose"] == True:
                        print("[i] Action: {}".format(action))

                    # Switch-case filter the action
                    match action:
                        case "print":
                            # Print environment variable
                            if ("hide-header" in optional_Flags) and (optional_Flags["hide-header"] == False):
                                print("Environment Variable: {}".format(curr_env_key))

                            match optional_with_Arguments["export-format"]:
                                case "text":
                                    print(env_value)
                                case "json":
                                    ## Prepare dictionary object to import/parse into a JSON-formatted string
                                    json_obj = [{"key" : curr_env_key, "value" : env_value}]

                                    # Append into JSON objects
                                    json_objects.append(json_obj)

                                    ## Import/Format the dictionary object into a JSON string
                                    json_str = dumps(json_obj, indent=4)

                                    ## Print in JSON
                                    print(json_str)
                                case _:
                                    ## Invalid format
                                    print("Invalid format: {}".format(optional_with_Arguments["export-format"]))

                            print("")
                        case "split":
                            # Get delimiter
                            if ("delimiter" in optional_with_Arguments) and (optional_with_Arguments["delimiter"] != ""):
                                delimiter = optional_with_Arguments["delimiter"]
                            elif number_of_positionals > 1:
                                delimiter = positionals[1]
                            else:
                                delimiter = str(input("Delimiter/Separator: "))

                            if optional_Flags["verbose"] == True:
                                print("[i] Delimiter: {}".format(delimiter))

                            # Split the environment variable by the delimiter
                            env_value_split = env_value.split(delimiter)

                            # Sanitize list
                            for i in range(len(env_value_split)): env_value_split[i].strip()

                            # Null Validation at the start and the end
                            env_value_split = [val for val in env_value_split if val != ""]

                            match optional_with_Arguments["export-format"]:
                                case "text":
                                    # Print results
                                    print(env_value_split)
                                    print("Number of values: {}".format(len(env_value_split)))
                                case "json":
                                    ## Prepare dictionary object to import/parse into a JSON-formatted string
                                    json_obj = [{"key" : curr_env_key, "value" : env_value_split}]

                                    ## Import/Format the dictionary object into a JSON string
                                    json_str = dumps(json_obj, indent=4)

                                    ## Print in JSON
                                    print(json_str)
                                case _:
                                    ## Invalid format
                                    print("Invalid format: {}".format(optional_with_Arguments["export-format"]))

                            print("")
                        case _:
                            # Default
                            print("[i] No actions provided.")
        else:
            print("[i] No positionals provided.")

if __name__ == "__main__":
    main()

