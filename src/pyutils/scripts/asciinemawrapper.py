"""
Terminal recorder using asciinema and convert to gif using asciinema-agg

:: Dependencies
- asciinema : In python
- asciinema-agg : In cargo
"""

# Import/Source libraries
import os
import sys
from subprocess import PIPE, Popen, DEVNULL, STDOUT
from pyutils.libraries.utils import pprint_error, pprint_info, pprint_warning

"""
Utilities Function
"""
def check_software_exists(software_name):
    """
    Check if the command exists and return status

    :: Params
    - software_name : Specify name of software binary/executable
        + Type: String

    :: Return
    - exists : Flag specifying if the application exists or not
        + Type: Boolean
    """
    # Initialize Variables
    exists = False
    retcode = -1 # Return Code

    # Open process pipe and check for output
    proc = Popen(["which", software_name], stdin=PIPE, stdout=DEVNULL, stderr=STDOUT)

    # Start executing command and wait for the command to complete via .communicate()
    stdout, stderr = proc.communicate()

    # Get Return Code
    retcode = proc.returncode

    # Check/Process through standard output
    if retcode == 0:
        exists = True

    return exists

"""
Application Function
"""
def format_argument_key_values(cmd_list, opts) -> None:
    """
    Split the optional arguments string (i.e. --key "argument-1" "argument-2" ...) and split it into a list
    to find all arguments and its associated values
        + Keys are identified by the '-' and '--' delimiters
        - The values are all non-key arguments until the next key is found
            + Every value will be grouped in a single list entry

    :: Params
    - cmd_list : Specify the command list to place the command line argument key and its corresponding values into
        + Type: List
    - opts : Specify the optional argument string specified by the user
        + Type: String
        - Notes
            + The identifier for CLI argument option keys (aka names) is the '-'/'--' delimiter/separator
        - Examples
            + --key "argument-1" "argument-2" == ["--key", "argument-1", "argument-2"]
    """
    # Initialize Variables
    curr_arg_list = []
    curr_flag = ""
    prev_flag = ""

    # Get all options separated
    opts_spl = opts.split()

    # Iterate through all optionals, starting with the key and find all the values to be mapped to the key
    for i in range(len(opts_spl)):
        # Get current option
        curr_opt = opts_spl[i]

        # Check if current element contains '-' and '--'
        if (curr_opt.startswith('-')) or (curr_opt.startswith("--")):
            # Flags/Optionals

            # Check if list is empty AND flag has moved to the next flag
            if ((len(curr_arg_list) != 0) and (prev_flag != curr_flag)):
                ## Append into command list
                cmd_list.append(' '.join(curr_arg_list))

                ## Set previous flag
                prev_flag = curr_flag

            ## Append into command list
            cmd_list.append(curr_opt)

            ## Set current optional flag
            curr_flag = curr_opt

            # Initialize/Reset arguments list
            curr_arg_list = []
        else:
            # Arguments to the flag
            ## Join the current option into a complete string
            curr_opt_joined = "".join(curr_opt)

            ## Append into arguments list
            curr_arg_list.append(curr_opt_joined)

        ## Check if last element
        if i == len(opts_spl)-1:
            ## Is last elemnt
            ## Check if list is empty AND previous flag is not current element
            if (len(curr_arg_list) != 0) and (prev_flag != curr_flag):
                ## Append final list into command list
                cmd_list.append(' '.join(curr_arg_list))

def display_help():
    """
    Display help message
    """
    msg="""
Help:

- Synopsis/Syntax
    {} [options] <arguments> [actions]

- Parameters
    - With Arguments
        + -c | --command [command-to-execute] : Specify a command to execute in asciinema to record
        + -t | --theme [theme-name] : Specify the theme to apply to the terminal background in the recording
        + --output-terminal-rec-filename [filename] : Specify the file name of the terminal recording output file
        + --output-animation-filename    [filename] : Specify the file name of the output converted animation GIF 
        + --input-terminal-rec-filename  [filename] : Specify the target file name of the terminal recording file you want to convert via asciinema-agg
        + --asciinema-opts [other opts ...]         : Specify all options you want to pass into asciinema
        + --asciinema-agg-opts [other opts ...]     : Specify all options you want to pass into asciinema-agg
    - Flags
        + --debug : Set program to 'debug mode'; All commands will be printed out instead
        + -h | --help : Display help message
        + -v | --version : Display system version
        + --print-opts-all : Print all optionals (with arguments and flags)
        + --print-opts-with-arguments : Print all optionals with arguments
        + --print-opts-flags : Print all flags (optionals without arguments)

- Usage
    - Record terminal screen using asciinema
        python asciinema-record-gif.py record -c 'make' --output-terminal-rec-filename output.cast
    - Convert the terminal recording into animation gif using asciinema (with gifski)
        python asciinema-record-gif.py convert --theme solarized-light --input-terminal-rec-filename output.cast --output-animation-filename output.gif
    - Record terminal screen using asciinema and convert recording to gif using asciinema-agg
        python asciinema-record-gif.py \
            record -c make --output-terminal-rec-filename output.cast \
            convert --theme solarized-light --input-terminal-rec-filename output.cast --output-animation-filename output.gif
    - Passthrough CLI arguments 
        - into asciinema directly
            python asciinema-record-gif.py --asciinema-opts "options here ..."
        - into asciinema-agg directly
            python asciinema-record-gif.py --asciinema-agg-opts "options here ..."
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
    global sys_version, exec, exec_path, exec_name, argv, argc

    sys_version = "v0.1.4"
    exec = sys.argv[0]
    exec_path = os.path.split(exec)[0]
    exec_name = os.path.split(exec)[1]
    argv = sys.argv[1:]
    argc = len(argv)

def validate_dependencies():
    """
    Check if the packages/dependencies are found
    """
    # Initialize Variables
    exec_dependencies = {"pip" : ["asciinema"], "cargo" : ["agg"]}

    # Iterate through dependencies
    for pkg_mgr, dependency_list in exec_dependencies.items():
        # Iterate through dependency lists
        for curr_exec in dependency_list:
            # Check if software exists
            exec_exists = check_software_exists(curr_exec)

            # If software does not exists
            if exec_exists == False:
                # Exit
                print("Executable [{}] is not installed/can not be found, please install it using {}".format(curr_exec, pkg_mgr))
                exit(1)

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
                case "--asciinema-opts":
                    ## Specify all options you want to pass into asciinema

                    ### Set properties
                    curr_key = "asciinema-opts"

                    ### Check if argument is provided
                    if i+1 < argc:
                        # Get argument value
                        asciinema_opts = argv[i+1]

                        # Check if current keyword exists, and if not = initialize an entry
                        if not (curr_key in opts["optionals"]["with-arguments"]):
                            opts["optionals"]["with-arguments"][curr_key] = ""

                        # Populate current keyword entry with value
                        opts["optionals"]["with-arguments"][curr_key] = asciinema_opts

                        # Shift 1 position to the left to jump to the next argument
                        # argc = len(argv)
                        i+=1
                    else:
                        pprint_warning("Asciinema options not specified")
                case "--asciinema-agg-opts":
                    ## Specify all options you want to pass into asciinema-agg

                    ### Set properties
                    curr_key = "asciinema-agg-opts"

                    ### Check if argument is provided
                    if i+1 < argc:
                        # Get argument value
                        asciinema_agg_opts = argv[i+1]

                        # Check if current keyword exists, and if not = initialize an entry
                        if not (curr_key in opts["optionals"]["with-arguments"]):
                            opts["optionals"]["with-arguments"][curr_key] = ""

                        # Populate current keyword entry with value
                        opts["optionals"]["with-arguments"][curr_key] = asciinema_agg_opts

                        # Shift 1 position to the left to jump to the next argument
                        i += 1
                    else:
                        pprint_warning("Asciinema-agg options not specified")
                case "-c" | "--command":
                    ## Specify a command to execute in asciinema to record
                    ### Set properties
                    curr_key = "command-to-execute"

                    ### Check if argument is provided
                    if i+1 < argc:
                        # Get argument value
                        cmd_to_exec = argv[i+1]

                        # Check if current keyword exists, and if not = initialize an entry
                        if not (curr_key in opts["optionals"]["with-arguments"]):
                            opts["optionals"]["with-arguments"][curr_key] = ""

                        # Populate current keyword entry with value
                        opts["optionals"]["with-arguments"][curr_key] = cmd_to_exec

                        # Shift 1 position to the left to jump to the next argument
                        i += 1
                    else:
                        pprint_warning("Command not specified")
                case "-t" | "--theme":
                    ## Specify the theme to apply to the terminal background in the recording
                    ### Set properties
                    curr_key = "theme"

                    ### Check if argument is provided
                    if i+1 < argc:
                        # Get argument value
                        theme_name = argv[i+1]

                        # Check if current keyword exists, and if not = initialize an entry
                        if not (curr_key in opts["optionals"]["with-arguments"]):
                            opts["optionals"]["with-arguments"][curr_key] = ""

                        # Populate current keyword entry with value
                        opts["optionals"]["with-arguments"][curr_key] = theme_name

                        # Shift 1 position to the left to jump to the next argument
                        i += 1
                    else:
                        pprint_warning("Theme not specified")
                case "--output-terminal-rec-filename":
                    ## Specify the file name of the terminal recording output file
                    ### Set properties
                    curr_key = "output-terminal-recording-filename"

                    ### Check if argument is provided
                    if i+1 < argc:
                        # Get argument value
                        filename = argv[i+1]

                        # Check if current keyword exists, and if not = initialize an entry
                        if not (curr_key in opts["optionals"]["with-arguments"]):
                            opts["optionals"]["with-arguments"][curr_key] = ""

                        # Populate current keyword entry with value
                        opts["optionals"]["with-arguments"][curr_key] = filename

                        # Shift 1 position to the left to jump to the next argument
                        i += 1
                    else:
                        pprint_warning("Terminal recording output file not specified")
                case "--output-animation-filename":
                    ## Specify the file name of the output converted animation GIF
                    ### Set properties
                    curr_key = "output-animation-filename"

                    ### Check if argument is provided
                    if i+1 < argc:
                        # Get argument value
                        filename = argv[i+1]

                        # Check if current keyword exists, and if not = initialize an entry
                        if not (curr_key in opts["optionals"]["with-arguments"]):
                            opts["optionals"]["with-arguments"][curr_key] = ""

                        # Populate current keyword entry with value
                        opts["optionals"]["with-arguments"][curr_key] = filename

                        # Shift 1 position to the left to jump to the next argument
                        i += 1
                    else:
                        pprint_warning("Converted animation output file not specified")
                case '--input-terminal-rec-filename':
                    ## Specify the target file name of the terminal recording file you want to convert via asciinema-agg
                    ### Set properties
                    curr_key = "input-terminal-recording-filename"

                    ### Check if argument is provided
                    if i+1 < argc:
                        # Get argument value
                        filename = argv[i+1]

                        # Check if current keyword exists, and if not = initialize an entry
                        if not (curr_key in opts["optionals"]["with-arguments"]):
                            opts["optionals"]["with-arguments"][curr_key] = ""

                        # Populate current keyword entry with value
                        opts["optionals"]["with-arguments"][curr_key] = filename

                        # Shift 1 position to the left to jump to the next argument
                        i += 1
                    else:
                        pprint_warning("Target input terminal recording file not specified")
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

def print_dict(dict_obj):
    """
    Print all dictionaries (key-value/associative array) provided
    """
    # Initialize Variables

    # Iterate through associative array
    for k,v in dict_obj.items():
        # Print
        print("{} : {}\n".format(k, v))

def merge_dictionary(dict_1, dict_2):
    """
    Merge 2 dictionaries together
    """
    # Initialize Variables
    merged_dictionary = {}

    # Merge optionals with arguments and flags together
    for k,v in dict_1.items():
        merged_dictionary[k] = v
    for k,v in dict_2.items():
        merged_dictionary[k] = v

    # Output/Return
    return merged_dictionary

def main():
    init()
    validate_dependencies()

    # Get CLI arguments
    opts = get_cli_arguments()

    # Process and begin operation

    # Split dictionary into standalone objects
    positionals = opts["positionals"]
    opts_complete = opts["optionals"]
    opt_with_arguments = opts_complete["with-arguments"]
    opt_Flags = opts_complete["flags"]

    # Merge optionals with arguments and flags together
    merged_dictionary = merge_dictionary(opt_with_arguments, opt_Flags)

    # print(merged_dictionary)

    ## Process Optionals
    for k,v in merged_dictionary.items():
        # Switch case current key-value
        match k:
            case "help":
                ## Display help message
                if v == 1:
                    display_help()
            case "version":
                ## Display system version information
                if v == 1:
                    display_system_version()
            case "print-opts-all":
                ## Print 'opts' associative array containing both flags and options with arguments
                if v == 1:
                    print_dict(opts)
            case "print-opts-flags":
                ## Print 'opt_Flags' associative array containing flags
                if v == 1:
                    print_dict(opt_Flags)
            case "print-opts-with-args":
                ## Print 'opt_with_arguments' associative array containg options with arguments
                if v == 1:
                    print_dict(opt_with_arguments)
            #case _:
            #    # Invalid option
            #    pprint_warning "Invalid key provided: $key"

    ## Process Positional Arguments
    for i in range(len(positionals)):
        # Get current value
        curr_val = positionals[i]

        # Switch case current key-value
        match curr_val:
            case "record":
                ## Initialize Variables
                cmd = "asciinema rec"
                cmd_flags = ""
                cmd_list = ["asciinema", "rec"]
                cmd_to_exec = ""
                asciinema_opts = ""
                output_terminal_recording_filename = ""

                # Locally store CLI argument values
                if "command-to-execute" in opt_with_arguments:
                    cmd_to_exec = opt_with_arguments["command-to-execute"]
                if "asciinema-opts" in opt_with_arguments:
                    asciinema_opts = opt_with_arguments["asciinema-opts"]
                if "output-terminal-recording-filename" in opt_with_arguments:
                    output_terminal_recording_filename = opt_with_arguments["output-terminal-recording-filename"]

                if "debug" in opt_Flags:
                    debug_mode = opt_Flags["debug"]
                else:
                    debug_mode = 0

                ## Sanitize/Verify CLI options
                if cmd_to_exec != "":
                    # cmd_flags += " -c \"{}\" ".format(cmd_to_exec)
                    cmd_list.append("-c")
                    cmd_list.append(cmd_to_exec)

                if asciinema_opts != "":
                    # cmd_flags+=" {} ".format(asciinema_opts)
                    format_argument_key_values(cmd_list, asciinema_opts)

                if output_terminal_recording_filename != "":
                    # cmd_flags+=" {} ".format(output_terminal_recording_filename)
                    cmd_list.append(output_terminal_recording_filename)
                else:
                    # Default name
                    # cmd_flags+=" output.cast "
                    cmd_list.append("output.cast")

                # Format command string
                cmd_str="{} {}".format(cmd, cmd_flags)

                if debug_mode == 1:
                    ## Record terminal using asciinema
                    # print(cmd_str)
                    # print(" ".join(cmd_list))
                    print(cmd_list)
                else:
                    # Open a subprocess pipe to execute system command for executing asciinema
                    with Popen(cmd_list, stdout=PIPE) as proc:
                        # Execute process
                        stdout = proc.communicate()[0].decode("utf-8")

                    print("Standard Output: {}".format(stdout))

            case "convert":
                ## Initialize Variables
                cmd="agg"
                cmd_flags=""
                cmd_list = ["agg"]
                theme = ""
                asciinema_agg_opts = ""
                input_terminal_recording_filename = ""
                output_animation_filename = ""

                # Locally store CLI argument values
                if "theme" in opt_with_arguments:
                    theme = opt_with_arguments["theme"]
                if "asciinema-agg-opts" in opt_with_arguments:
                    asciinema_agg_opts = opt_with_arguments["asciinema-agg-opts"]
                if "input-terminal-recording-filename" in opt_with_arguments:
                    input_terminal_recording_filename = opt_with_arguments["input-terminal-recording-filename"]
                if "output-animation-filename" in opt_with_arguments:
                    output_animation_filename = opt_with_arguments["output-animation-filename"]

                if "debug" in opt_Flags:
                    debug_mode = opt_Flags["debug"]
                else:
                    debug_mode = 0

                ## Sanitize/Verify CLI options
                if theme != "":
                    # cmd_flags+=" --theme $theme "
                    cmd_list.append("--theme")
                    cmd_list.append(theme)

                if asciinema_agg_opts != "":
                    # cmd_flags+=" {} ".format(asciinema_agg_opts)
                    format_argument_key_values(cmd_list, asciinema_agg_opts)

                if input_terminal_recording_filename != "":
                    # cmd_flags+=" {} ".format(input_terminal_recording_filename)
                    cmd_list.append(input_terminal_recording_filename)
                else:
                    pprint_error("No input terminal recording file provided, please provide the file to convert")

                if output_animation_filename != "":
                    # cmd_flags+=" {} ".format(output_animation_filename)
                    cmd_list.append(output_animation_filename)
                else:
                    # cmd_flags+=" output.gif "
                    cmd_list.append("output.gif")

                if debug_mode == 1:
                    ## Convert terminal recording by asciinema into gif using asciinema-agg
                    # print(" ".join(cmd_list))
                    print(cmd_list)
                else:
                    # Open a subprocess pipe to execute system command for executing asciinema
                    with Popen(cmd_list, stdout=PIPE) as proc:
                        # Execute process
                        stdout = proc.communicate()[0].decode("utf-8")

                    print("Standard Output: {}".format(stdout))
            case _:
                # Invalid option
                pprint_warning("Invalid action provided: {}".format(curr_val))

if __name__ == "__main__":
    main()

