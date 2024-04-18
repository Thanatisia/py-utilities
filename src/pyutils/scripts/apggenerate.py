"""
A simple Android project structure generator to
streamline the setting up process of your host system for Android application development from command line (without Android Studio)
"""
import os
import sys
import platform
from pyutils.libraries.apg import AndroidProjectGenerator, APGLinux, APGWindows

def arg_remove(argv, values):
    """
    Pop and remove an element from the CLI argument list according to its index/positioning

    :: Params
    - argv : The CLI argument list to remove from
        Type: List

    - pos : List of position/index of the element to pop/remove
        Type: List
    """
    # Initialize Variables
    argc = len(argv)

    # Loop through list of positions
    for i in range(len(values)):
        # Get target values to remove
        value_to_remove = values[i]

        print("Removed: {}".format(value_to_remove))
        print("New List: {}".format(argv))

        # Pop the current element from the argument list (Shift to the left by 1 argument) after usage
        argv.remove(value_to_remove)

        # Format new list
        # argv = argv[i:]

        # Set new argc
        argc = len(argv)

    return [argv, argc]

def display_help():
    """
    Display help message
    """
    msg="""
{}

:: Synopsis/Syntax
python {} <global-options> [actions] <internal-options> <arguments>

:: Parameters
- Positionals
    - Actions
        - download [type] : Download the specified category/type
            - Items
                + dependencies : Download specified dependencies
        - setup : Prepare and setup user's shell for Android application development use
        - template : Generate a proper Mobile application project structure
            - Notes
                - The generated template project structure have certain sections populated by keywords that have to be edited by the user
                    + This is for user design
                + Hence, before building, please look through the project structure and edit according to your needs
        - gradle : Setup gradle files within the generated template project structure; To be used after 'template'
- Optionals
    + -h | --help : Display help message
    + -v | --version : Display system version
    + -s | --view-settings : Display current settings for system

:: Usage
- Full project run
    python {} download dependencies setup template gradle
""".format(
    application_Info["name"], 
    application_Info["executable"],
    application_Info["executable"]
)
    print(msg)

def init():
    """
    Perform global variable and class object initialization
    """
    global flags, application_Info, apg, apg_System, exec, argv, argc

    application_Info = {
        "name" : "APG - Android Project Generator",
        "executable" : "generator.py",
        "version" : "v0.1.0",
    }

    # Global Variables
    flags = {
        "help" : False
    }

    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

    # Initialize Class variables

    ## Check system
    match platform.system():
        case "Linux":
            # If platform is a Linux system
            apg_System = APGLinux()
        case "Windows":
            # If platform is a Linux system
            apg_System = APGWindows()
        case _:
            # Default
            print("Unable to determine platform.")
            exit(1)

    apg = AndroidProjectGenerator(apg_System)

def obtain_cli_args():
    """
    Obtain CLI arguments in a dictionary (Key-Value) object
    """
    # Initialize Variables
    args = {
        "positionals" : {
            # [ID] = "positional argument input"
        },
        "optionals" : {
            "with-arguments" : {
                # Options with subarguments/parameters
                # [option-name] : [subargument]
            },
            "flags" : {
                # Flags = No arguments, but boolean. True/False
                # [option-name] : [true|false]
            }
        }
    }
    argv_local = argv.copy()
    argc = len(argv_local)
    i = 0

    # Check if there are arguments
    if argc > 0:
        # While there are still arguments -> where the current index is less than the total argument count
        # Loop through and get all arguments
        while (i < argc):
            # Get current CLI argument
            curr_arg = argv_local[i]

            # Process argument
            match curr_arg:
                case "setup":
                    """
                    Setup system environment
                    """
                    ## Check if option is in arguments
                    if not ("setup" in args["positionals"]):
                        ## Initialize the entry
                        args["positionals"]["setup"] = True
                case "download":
                    """
                    Download a specified input value
                    """
                    # Get position index of argument input as a temporary variable
                    tmp_id = i+1

                    # Check if download type is specified
                    if tmp_id >= argc:
                        print("No download category/type specified.")
                    else:
                        # Get download category/type
                        category = argv_local[tmp_id]

                        ## Sanitize and validate if the input is valid
                        match category:
                            case "dependencies":
                                """
                                Download Dependencies
                                """
                                ## Check if option is in arguments
                                if not ("download" in args["positionals"]):
                                    # Map CLI optional argument to the value provided
                                    args["positionals"]["download"] = category

                                # (Alternative:) Pop the current element from the argument list (Shift to the left by 1 argument) after usage
                                # Set the current position index to the position of the subargument (argument input) to proceed to the following CLI argument
                                i = tmp_id
                            case _:
                                print("Invalid item download category/type specified: {}".format(category))
                                print("Supported: dependencies")
                case "template":
                    """
                    Generate template android project structure and source files
                    """
                    ## Check if option is in arguments
                    if not ("template" in args["positionals"]):
                        ## Initialize the entry
                        args["positionals"]["template"] = True
                case "gradle":
                    """
                    Setup Gradle build files within the generated template project

                    - Notes
                        - Please use this after 'template' or if there is an existing copy of the template project folder
                    """
                    ## Check if option is in arguments
                    if not ("gradle" in args["positionals"]):
                        ## Initialize the entry
                        args["positionals"]["gradle"] = True
                case "-s" | "--view-settings":
                    """
                    View settings
                    """
                    ## Check if option is in arguments
                    if not ("view-settings" in args["optionals"]["flags"]):
                        ## Initialize the entry
                        args["optionals"]["flags"]["view-settings"] = True
                case "-h" | "--help":
                    """
                    Display Help
                    """
                    ## Check if option is in arguments
                    if not ("help" in args["optionals"]["flags"]):
                        ## Initialize the entry
                        args["optionals"]["flags"]["help"] = True
                case "-v" | "--version":
                    """
                    Display system version
                    """
                    ## Check if option is in arguments
                    if not ("check-version" in args["optionals"]["flags"]):
                        ## Initialize the entry
                        args["optionals"]["flags"]["check-version"] = True
                case _:
                    # Default, incorrect option
                    print("Incorrect option provided : {}".format(curr_arg))
                    display_help()

            # Increment the index by 1 to place the pointer up to the next position index
            i += 1
    else:
        print("No arguments provided.")

    # Output
    return args

def process_cli_args(cli_args):
    """
    Process CLI arguments obtained

    :: Params
    - cli_args : Dictionary (Key-value) mapping of CLI argument (i.e. positionals, optional arguments - flags or with subarguments)
        Type: Dictionary
    """
    # Initialize Variables
    project_root_Dir = apg.settings["project_Info"]["project_root_Dir"]
    project_primary_Language = apg.settings["android_tools_Info"]["project_primary_Language"]
    target_directories = apg.settings["project_Info"]["target_directories"].copy()
    target_files = apg.settings["project_Info"]["target_files"].copy()

    positionals = cli_args["positionals"]
    optionals = cli_args["optionals"]
    opt_with_Args = optionals["with-arguments"]
    opt_Flags = optionals["flags"]

    # Check Optional Arguments
    ## Loop through optional arguments with Arguments
    for k,v in opt_with_Args.items():
        match k:
            case _:
                # Invalid argument
                print("Invalid option specified: {}".format(k))

    ## Loop through optional Flags
    for k,v in opt_Flags.items():
        # option = True|False
        match k:
            case "view-settings":
                #  Check if is true
                if v == True:
                    # Print settings for current system
                    for k,v in apg.settings.items():
                        print("{} = {}".format(k,v))
                        print("")
            case "help":
                # Check if is true
                if v == True:
                    # Is true
                    display_help()
                    exit(1)
            case "check-version":
                # Check if is true
                if v == True:
                    # Is true
                    print("System Version: {}".format(application_Info["version"]))
                    exit(1)
            case _:
                # Invalid option obtained
                print("Invalid option obtained: {}".format(k))

    # Loop through positional dictionary
    for k,v in positionals.items():
        match k:
            case "download":
                match v:
                    case "dependencies":
                        # Download the specified
                        print("Download Dependencies")
                        apg.dl_Dependencies()
                    case _:
                        # Invalid argument
                        print("Invalid argument specified: {}".format(v))
            case "setup":
                # Check if is true
                if v == True:
                    print("Setup system environment")
                    apg_System.setup_Env()
            case "template":
                # Check if is true
                if v == True:
                    print("Setup template project structure")
                    # Check if specified project exists
                    if not (os.path.isdir(project_root_Dir)):
                        # If project does not exist
                       
                        ## Generate template project structure
                        print("Generating template project...")
                        apg.generate_template_Project()

                        print("")

                        ## Populate project source files
                        print("Populating template project...")
                        apg.populate_template_Project()
                    else:
                        print("Project [{}] exists.".format(project_root_Dir))
            case "gradle":
                #  Check if is true
                if v == True:
                    # Create gradle files
                    print("Setup gradle")
                    apg.populate_build_Files()
        print("")

def setup():
    """
    Perform pre-initialization and project environment setup
    """
    global flags
    flags = obtain_cli_args()
    print("")

def main():
    """
    Run Generator
    """
    init()
    setup()

    print(flags)
    process_cli_args(flags)

if __name__ == "__main__":
    main()


