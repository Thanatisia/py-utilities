"""
Terminal recorder using asciinema and convert to gif using asciinema-agg

:: Dependencies
- asciinema : In python
- asciinema-agg : In cargo
"""

# Import/Source libraries
import os
import sys
from subprocess import PIPE, Popen
from pyutils.libraries.utils import pprint_error, pprint_info, pprint_warning

"""
Application Function
"""
def display_help():
    """
    Display help message
    """
    msg="""
Help:

- Synopsis/Syntax
    {} {options} <arguments> [actions]

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
    """.format(exec)
    print(msg)

def display_system_version():
    """
    Display system version
    """
    msg="""
System Version:
    Executable: {}
    Version   : {}
    """.format(exec, sys_version)
    print(msg)

"""
System Functions
"""
def init():
    """
    Initialize System Global Information
    """
    global sys_version, exec, argv, argc

    sys_version = "v0.1.0"
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

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
    # print(opts)

    ## Process Optionals
    for k,v in opts.items():
        # Switch case current key-value
        match k:
            case "help":
                ## Display help message
                display_help()
            case "version":
                ## Display system version information
                display_system_version()
            case "print-opts-all":
                ## Print 'opts' associative array containing both flags and options with arguments
                print_dict(opts)
            case "print-opts-flags":
                ## Print 'opt_Flags' associative array containing flags
                print_dict(opt_Flags)
            case "print-opts-with-args":
                ## Print 'opt_with_arguments' associative array containg options with arguments
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

                # Locally store CLI argument values
                cmd_to_exec = opt_with_arguments["command-to-execute"]
                asciinema_opts = opt_with_arguments["asciinema-opts"]
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
                    cmd_list.append(asciinema_opts)

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
                    print(" ".join(cmd_list))
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

                # Locally store CLI argument values
                theme = opt_with_arguments["theme"]
                asciinema_agg_opts = opt_with_arguments["asciinema-agg-opts"]
                input_terminal_recording_filename = opt_with_arguments["input-terminal-recording-filename"]
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
                    # Get options
                    asciinema_agg_opts_spl = asciinema_agg_opts.split()
                    cmd_list.extend(asciinema_agg_opts_spl)

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
                    print(" ".join(cmd_list))
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
