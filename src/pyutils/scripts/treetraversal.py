"""
Walking through all files and subdirectories in the top level root directory down the separate branches
"""
import os
import sys
from json import load, loads, dump, dumps
from pyutils.libraries.utils import pprint_error, pprint_info, pprint_info, pprint_warning
from pyutils.libraries.treelib import tree_traversal, path_separator

def print_tree_branches(tree_branch_mappings, filters="all", delimiter="=", stdout_type="json", json_dump_opts={"indent" : 4}):
    """
    Print the tree branch mappings

    :: Params
    - top_level_root_dir : Specify the top level root directory to begin searching from
        + Type: String
        + Default: '.'

    - filters : Specify the filter topic you wish to view from the standard output
        + Type: String
        + Default: all
        - Filters
            + all : Display all key-values
            + directories : Display directories only
            + files : Display files only

    - delimiter : Specify the delimiter to map the directory name to the parent directory path
        + Type: String
        + Default: '='

    - stdout_type : Specify the type of standard output to print the results with
        + Type: String
        + Default: 'text'
        - Standard output formats
            + text
            + dictionary (aka JSON)

    - json_dump_opts : Specify a dictionary containing the options you wish to pass into 'json.dumps()'
        + Type: Dictionary
        - Default
            {
                "indent" : 4
            }
    """
    match filters:
        case "all":
            # Switch case the standard output format
            match stdout_type:
                case "text":
                    ## Print all keys
                    for k,v in tree_branch_mappings.items():
                        print("{} {} {}".format(k, delimiter, v))
                case "json":
                    # Initialize variables
                    json_contents = []

                    for k,v in tree_branch_mappings.items():
                        # Initialize a new JSON entry for current directory
                        curr_branch_json = {}

                        # Map the 'name' key to the directory name
                        curr_branch_json["path"] = k
                        # Map the 'path' key to the directory path
                        curr_branch_json["contents"] = v

                        # Append into list
                        json_contents.append(curr_branch_json)

                    # Format the dictionary object into a JSON string
                    json_str = dumps(json_contents, **json_dump_opts)

                    # Print the JSON string
                    print(json_str)
        case "files":
            # Switch case the standard output format
            match stdout_type:
                case "text":
                    # Print files only
                    for k,v in tree_branch_mappings.items():
                        curr_branch_files = v["files"]
                        print("{} {} {}".format(k, delimiter, curr_branch_files))
                case "json":
                    # Initialize variables
                    json_contents = []

                    for k,v in tree_branch_mappings.items():
                        # Initialize a new JSON entry for current directory
                        curr_branch_json = {}

                        # Obtain file vlaues
                        curr_branch_files = v["files"]

                        # Map the 'name' key to the directory name
                        curr_branch_json["path"] = k
                        # Map the 'path' key to the directory path
                        curr_branch_json["contents"] = { "files" : curr_branch_files }

                        # Append into list
                        json_contents.append(curr_branch_json)

                    # Format the dictionary object into a JSON string
                    json_str = dumps(json_contents, **json_dump_opts)

                    # Print the JSON string
                    print(json_str)
        case "directories":
            # Switch case the standard output format
            match stdout_type:
                case "text":
                    # Print directories only
                    for k,v in tree_branch_mappings.items():
                        curr_branch_directories = v["directories"]
                        print("{} {} {}".format(k, delimiter, curr_branch_directories))
                case "json":
                    # Initialize variables
                    json_contents = []

                    for k,v in tree_branch_mappings.items():
                        # Initialize a new JSON entry for current directory
                        curr_branch_json = {}

                        # Obtain directory values
                        curr_branch_directories = v["directories"]

                        # Map the 'name' key to the directory name
                        curr_branch_json["path"] = k
                        # Map the 'path' key to the directory path
                        curr_branch_json["contents"] = { "directories" : curr_branch_directories }

                        # Append into list
                        json_contents.append(curr_branch_json)

                    # Format the dictionary object into a JSON string
                    json_str = dumps(json_contents, **json_dump_opts)

                    # Print the JSON string
                    print(json_str)
        case _:
            print("Invalid format: {}".format(format))

def get_git_repositories(root_dir="."):
    """
    Get git repositories based on the .git identifier
    """
    # Initialize Variables
    all_git_dirs = []

    # Get all directories in each tree branch
    tree_branch_mappings = tree_traversal(root_dir)
    for k,v in tree_branch_mappings.items():
        curr_dir_dirs = v["directories"]

        # Check if curr_obj is a directory called .git
        if ".git" in curr_dir_dirs:
            # Is a .git
            all_git_dirs.append(k)

    return all_git_dirs

def print_git_repositories(top_level_root_dir=".", delimiter="=", stdout_type="text", json_dump_opts={"indent" : 4}):
    """
    Get and print all git repositories at the top level directory down

    :: Params
    - top_level_root_dir : Specify the top level root directory to begin searching from
        + Type: String
        + Default: '.'

    - delimiter : Specify the delimiter to map the directory name to the parent directory path
        + Type: String
        + Default: '='

    - stdout_type : Specify the type of standard output to print the results with
        + Type: String
        + Default: 'text'
        - Standard output formats
            + text
            + dictionary (aka JSON)

    - json_dump_opts : Specify a dictionary containing the options you wish to pass into 'json.dumps()'
        + Type: Dictionary
        - Default
            {
                "indent" : 4
            }
    """
    all_git_dirs = get_git_repositories(root_dir=top_level_root_dir)

    # Switch case the standard output format
    match stdout_type:
        case "text":
            # print("All git repositories: {}".format(all_git_dirs))
            print("Name {} Parent".format(delimiter))
            for dir in all_git_dirs:
                # Split directory into parts
                dir_parts = dir.split(path_separator)
                # Get every element in the list until the second last element, and merge them together with the "/" delimiter
                dir_parents = path_separator.join(dir_parts[:-1])
                # Get the last element in the list
                dir_name = dir_parts[::-1][0]
                print("{} {} {}".format(dir_name, delimiter, dir_parents))
        case "json":
            # Initialize variable
            json_contents = []

            for dir in all_git_dirs:
                # Initialize a new JSON entry for current directory
                curr_git_json = {}

                # Split directory into parts
                dir_parts = dir.split(path_separator)
                # Get every element in the list until the second last element, and merge them together with the "/" delimiter
                dir_parents = path_separator.join(dir_parts[:-1])
                # Get the last element in the list
                dir_name = dir_parts[::-1][0]

                # Map the 'name' key to the directory name
                curr_git_json["name"] = dir_name
                # Map the 'path' key to the directory path
                curr_git_json["path"] = dir_parents

                # Append into list
                json_contents.append(curr_git_json)

            # Format the dictionary object into a JSON string
            json_str = dumps(json_contents, **json_dump_opts)

            # Print the JSON string
            print(json_str)
        case _:
            # Invalid type
            print("[-] Invalid type provided: {}".format(stdout_type))

def display_help():
    """
    Display Help Menu
    """
    msg = """
:: Synopsis/Syntax
- Standard
    treewalk <optionals> <arguments>

:: Parameters
- Positionals
    - top-level-root-directory-path : Specify the top-level root directory path to start the search. Ignored if '-t|--top-level-root-dir' is provided
        + Type: String
    - filter : Specify the search/archive targets you wish to scan for (i.e. files, directories or all (both)). Ignored if '-f|--filter' is provided
        + Type: String
        - Filter keywords
            + all : Display all files and (sub)directories found in the tree, branches and subbranches starting from the top level root directory
            + directories : Display all directories found in the tree, branches and subbranches starting from the top level root directory
            + files : Display all files found in the tree, branches and subbranches starting from the top level root directory
    - search-keyword : Specify the target search category/topic to find (i.e. tree = Regular Files and Directories, git = git repositories)
        + Type: String
        - Search Category/Topic
            + git : Search for git directories down the tree, branches and subbranches starting from the top level root directory
            + tree : Search for regular files and directories down the tree, branches and subbranches starting from the top level root directory
    - export-format : Specify the format to export/print the standard output as
        + Type: String
        - Search Category/Topic
            + text : Regular text format
            + json : Export/Output the result as a parsed JSON-formatted string to standard output
- Optionals
    - With Arguments
        - "-f | --filter <filter-keyword>" : Explicitly specify a custom keyword to filter/display
            + Type: String
            + Default: all
            - Filter keywords
                + all : Display all files and (sub)directories found in the tree, branches and subbranches starting from the top level root directory
                + directories : Display all directories found in the tree, branches and subbranches starting from the top level root directory
                + files : Display all files found in the tree, branches and subbranches starting from the top level root directory
        - "-s | --search-category <category>": Explicitly specify the target search category/topic to find
            + Type: String
            + Default: tree
            - Search Category/Topic
                + git : Search for git directories down the tree, branches and subbranches starting from the top level root directory
                + tree : Search for regular files and directories down the tree, branches and subbranches starting from the top level root directory
        - "-t | --top-level-root-dir <top-level-root-directory-path>" : Explicitly specify a custom top level root directory using a optional value
            + Type: String
            + Default: "."
        - "-x | --export-format <formats>" : Explicitly specify the type/format to export/print the standard output as
            + Type: String
            + Default: text
            - Search Category/Topic
                + text : Regular text format
                + json : Export/Output the result as a parsed JSON-formatted string to standard output
    - Flags
        + -h | --help : Display help message
        + -v | --version : Display system version information
        + -V | --verbose : Enable Verbose output

:: Usage
- Default run
    - Notes
        - This is the same as:
            treewalk -t -x -s -f
    treewalk -t . -f all -s tree -x text

- Traverse through the default route with default configurations
    ```bash
    treewalk -t
    ```

- Export result as JSON
    - Notes
        - This is the same as:
            treewalk -t -x json -s -f
    treewalk -t . -f all -s tree -x json
    """
    print(msg)

def display_system_version():
    """
    Display Help Menu
    """
    msg = """
Executable Name: {}
Executable Version: {}
    """.format(exec_name, exec_vers)
    print(msg)

def init():
    """
    Perform Pre-Initialization Setup
    """
    # Define global variables
    global argparser, default_top_level_root_dir, default_filter, default_export_format, default_search_category, accepted_filters, accepted_export_formats, accepted_search_categories, exec_name, exec_vers

    # Initialize Variables
    argparser = {
        "positionals" : [],
        "optionals" : {
            "with-arguments" : {},
            "flags" : {}
        }
    }
    default_top_level_root_dir = "."
    default_filter = "all"
    default_export_format = "text"
    default_search_category = "tree"
    accepted_filters = ["all", "directories", "files"]
    accepted_export_formats = ["text", "json"]
    accepted_search_categories = ["tree", "git"]
    exec_name = "treewalk"
    exec_vers = "v0.2.0"

def get_next_element(current_index, target_list:list) -> list:
    """
    Get the next element in a list
    """
    # Initialize Variables
    argc = len(target_list)
    res = ""

    ## Get next index
    next_idx = current_index+1

    ## Check if next argument value is provided
    if next_idx <= (argc-1):
        # Next index is not last element
        next_element = target_list[next_idx]

        # Increment index counter by 1 to jump to the subsequent element
        current_index += 1

        # Set the result to return
        res = next_element
    else:
        # Argument not provided
        res = ""

    # Output/return
    return [next_idx, res]

def get_cli_arguments():
    """
    Get and parse CLI arguments provided by users
    """
    global argparser

    # Initialize Variables

    # Get CLI arguments
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

    # Iterate through all CLI arguments and format into the arguments parser
    i:int = 0
    while i < argc:
        # Get current argument
        curr_arg = argv[i]

        # Match/switch case the current argument
        match curr_arg:
            ## Optional Flags
            case "-f" | "--filter":
                # Set display format
                # Accepted values: [all, directories, files]
                ## Get next index
                next_idx = i+1
                ## Check if next argument value is provided
                if next_idx <= (argc-1):
                    # Next index is not last element
                    filter_val = argv[next_idx]

                    # Data Validation: Check if a filter value is specified
                    if filter_val != "":
                        # Data Validation: Check Filter Value
                        if filter_val in accepted_filters:
                            # Accepted Filter
                            # Map the optional to the filter
                            argparser["optionals"]["with-arguments"]["filter"] = filter_val

                            # Increment index counter by 1 to jump to the subsequent element
                            i += 1
                        else:
                            # Map the optional to the default value
                            argparser["optionals"]["with-arguments"]["filter"] = default_filter
                    else:
                        # Empty value: set to default
                        # Map the optional to the default filter
                        argparser["optionals"]["with-arguments"]["filter"] = default_filter
                else:
                    # Argument not provided
                    # Map the optional to the default value
                    argparser["optionals"]["with-arguments"]["filter"] = default_filter
            case "-s" | "--search-category":
                # Explicitly specify the search category/topic to find
                ## Get next index
                next_idx = i+1
                ## Check if next argument value is provided
                if next_idx <= (argc-1):
                    # Next index is not last element
                    search_category = argv[next_idx]

                    # Data Validation: Check if a search category is specified
                    if search_category != "":
                        # Data Validation: Check if the export format is valid
                        if search_category in accepted_search_categories:
                            # Accepted category
                            # Map the optional to the specified category
                            argparser["optionals"]["with-arguments"]["search-category"] = search_category

                            # Increment index counter by 1 to jump to the subsequent element
                            i += 1
                        else:
                            # Invalid path
                            # Map the optional to the default category
                            argparser["optionals"]["with-arguments"]["search-category"] = default_search_category
                    else:
                        # Empty value: set to default
                        # Map the optional to the default category
                        argparser["optionals"]["with-arguments"]["search-category"] = default_search_category
                else:
                    # Argument not provided
                    # Map the optional to the default category
                    argparser["optionals"]["with-arguments"]["search-category"] = default_search_category
            case "-t" | "--top-level-root-dir":
                # Explicitly specify a custom top level root directory using a optional value
                ## Get next index
                next_idx = i+1
                ## Check if next argument value is provided
                if next_idx <= (argc-1):
                    # Next index is not last element
                    top_level_root = argv[next_idx]

                    # Data Validation: Check a top level root directory is specified
                    if top_level_root != "":
                        # Data Validation: Check if the top level root directory is valid
                        if os.path.isdir(top_level_root):
                            # Is a directory
                            # Map the optional to the specified path
                            argparser["optionals"]["with-arguments"]["top-level-root"] = top_level_root

                            # Increment index counter by 1 to jump to the subsequent element
                            i += 1
                        else:
                            # Invalid path
                            # Map the optional to the default path
                            argparser["optionals"]["with-arguments"]["top-level-root"] = default_top_level_root_dir
                    else:
                        # Empty value: set to default
                        # Map the optional to the default path
                        argparser["optionals"]["with-arguments"]["top-level-root"] = default_top_level_root_dir
                else:
                    # Argument not provided
                    # Map the optional to the default path
                    argparser["optionals"]["with-arguments"]["top-level-root"] = default_top_level_root_dir
            case "-x" | "--export-format":
                # Explicitly specify the export type/format
                ## Get next index
                next_idx = i+1
                ## Check if next argument value is provided
                if next_idx <= (argc-1):
                    # Next index is not last element
                    export_format = argv[next_idx]

                    # Data Validation: Check a export format is specified
                    if export_format != "":
                        # Data Validation: Check if the export format is valid
                        if export_format in accepted_export_formats:
                            # Accepted format
                            # Map the optional to the specified path
                            argparser["optionals"]["with-arguments"]["export-format"] = export_format

                            # Increment index counter by 1 to jump to the subsequent element
                            i += 1
                        else:
                            # Invalid path
                            # Map the optional to the default path
                            argparser["optionals"]["with-arguments"]["export-format"] = default_export_format
                    else:
                        # Empty value: set to default
                        # Map the optional to the default format
                        argparser["optionals"]["with-arguments"]["export-format"] = default_export_format
                else:
                    # Argument not provided
                    # Map the optional to the default path
                    argparser["optionals"]["with-arguments"]["export-format"] = default_export_format
            ## Optional With Arguments
            case "-h" | "--help":
                # Display help menu
                argparser["optionals"]["flags"]["help"] = True
            case "-v" | "--version":
                # Display system version information
                argparser["optionals"]["flags"]["version"] = True
            case "-V" | "--verbose":
                # Enable Verbose output
                argparser["optionals"]["flags"]["verbose"] = True
            case _:
                # Default: Positional
                argparser["positionals"].append(curr_arg)

        # Increment index counter and go to the next element
        i += 1

    # Output/Return
    return argparser

def main():
    """
    Perform Pre-Initialization Setup
    """
    init()

    """
    Initialize Local Variables
    """
    top_level_root = ""
    filter = ""
    search_category = ""
    export_format = ""

    """
    Get CLI arguments
    """
    argparser = get_cli_arguments()

    """
    Extract CLI arguments as necessary
    """
    positionals = argparser["positionals"]
    optionals = argparser["optionals"]
    opt_with_args = optionals["with-arguments"]
    opt_with_args_Keys = list(opt_with_args.keys())
    opt_Flags = optionals["flags"]
    opt_flags_Keys = list(opt_Flags.keys())
    number_of_pos = len(positionals)
    number_of_opt = len(optionals)

    if ("verbose" in opt_flags_Keys):
        if opt_Flags["verbose"]:
            pprint_info(argparser)
            pprint_info(opt_with_args_Keys)

    """
    Process obtained CLI arguments
    """
    ## Iterate through the optional categories
    for opt_category_key, opt_category_values in optionals.items():
        for opt_name, opt_value in opt_category_values.items():
            # Switch case and check values
            match opt_name:
                case "help":
                    ## Display Help Menu
                    pprint_info("Display Help Menu")
                    display_help()
                    exit(0)
                case "version":
                    ## Display System Version Information
                    pprint_info("Display System Version Information")
                    display_system_version()
                    exit(0)
                case opt_name if not (opt_name in list(opt_category_values.keys())):
                    ## Default: If current option is not in the list
                    pprint_error("Invalid optional provided in category [{}]: {}={}".format(opt_category_key, opt_name, opt_value))

    """
    Default value checks
    """
    # Check if top level root directory optional ('-t'/'--top-level-root-dir') is mapped
    if ("top-level-root" in opt_with_args_Keys):
        if (opt_with_args["top-level-root"] == ""):
            # Set as default
            top_level_root = default_top_level_root_dir
        else:
            # Top Level Root Diectory is set
            top_level_root = opt_with_args["top-level-root"]
    else:
        # Set as default
        top_level_root = default_top_level_root_dir

    # Check if filters is set
    if ("filter" in opt_with_args_Keys):
        if (opt_with_args["filter"] == ""):
            # Check if top-level-root is set
            if top_level_root == "":
                # Argument 1 is not set
                pprint_error("Top-level root directory to start searching is not set.")
                exit(1)
            else:
                # Set as default
                filter = default_filter
        else:
            # Filter is set
            filter = opt_with_args["filter"]
    else:
        # Set as default
        filter = default_filter

    # Check if a search category is specified
    if ("search-category" in opt_with_args_Keys):
        if (opt_with_args["search-category"] == ""):
            # Check if previous positionals are set
            if top_level_root == "":
                # Check if top-level-root-dir is set
                # Argument 1 is not set
                pprint_error("The top-level root directory to start searching is not set.")
                exit(1)
            elif filter == "":
                # Check if filter is set
                # Argument 2 is not set
                pprint_error("Filter Keyword ['all', 'files', 'directories'] is not set.")
                exit(1)
            else:
                # Set as default
                search_category = default_search_category
        else:
            # Filter is set
            search_category = opt_with_args["search-category"]
    else:
        # Set as default
        search_category = default_search_category

    # Check if a export type is specified
    if ("export-format" in opt_with_args_Keys):
        if (opt_with_args["export-format"] == ""):
            # Check if previous positionals are set
            if top_level_root == "":
                # Check if top-level-root-dir is set
                # Argument 1 is not set
                pprint_error("The top-level root directory to start searching is not set.")
                exit(1)
            elif filter == "":
                # Check if filter is set
                # Argument 2 is not set
                pprint_error("Filter Keyword ['all', 'files', 'directories'] is not set.")
                exit(1)
            elif search_category == "":
                # Check if the search category is set
                # Argument 3 is not set
                pprint_error("Search Category ('tree', 'git'] is not set.")
                exit(1)
            else:
                # Set as default
                export_format = default_export_format
        else:
            # Export Format is set
            export_format = opt_with_args["export-format"]
    else:
        # Set as default
        export_format = default_export_format

    # Verbose message: Display information regarding filters
    if ("verbose" in opt_flags_Keys):
        if opt_Flags["verbose"]:
            pprint_info("Top Level Root Directory: {}".format(top_level_root))
            pprint_info("Filter Keyword: {}".format(filter))
            pprint_info("Search Category: {}".format(search_category))
            pprint_info("Export Format: {}".format(export_format))

    if search_category == "":
        # Check if the search category is set
        # Argument 3 is not set
        pprint_error("Search Category ('tree', 'git'] is not set.")
        exit(1)
    else:
        match search_category:
            case "tree":
                if top_level_root == "":
                    # Check if top-level-root-dir is set
                    # Argument 1 is not set
                    pprint_error("The top-level root directory to start searching is not set.")
                    exit(1)
                elif filter == "":
                    # Check if filter is set
                    # Argument 2 is not set
                    pprint_error("Filter Keyword ['all', 'files', 'directories'] is not set.")
                    exit(1)
                elif export_format == "":
                    # Check if the export format is set
                    # Argument 3 is not set
                    pprint_error("Export Format ('text', 'json'] is not set.")
                    exit(1)
                else:
                    tree_branch_mappings = tree_traversal(top_level_root)
                    print_tree_branches(tree_branch_mappings, filters=filter, stdout_type=export_format)
            case "git":
                if top_level_root == "":
                    # Check if top-level-root-dir is set
                    # Argument 1 is not set
                    pprint_error("The top-level root directory to start searching is not set.")
                    exit(1)
                elif export_format == "":
                    # Check if the export format is set
                    # Argument 3 is not set
                    pprint_error("Export Format ('text', 'json'] is not set.")
                    exit(1)
                else:
                    print_git_repositories(top_level_root, stdout_type=export_format)


if __name__ == "__main__":
    main()

