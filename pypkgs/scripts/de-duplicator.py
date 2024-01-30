"""
De-duplicator CLI utility
"""
import os
import sys

def sanitizer(target_list:list):
    """
    Sanitize the target list by removing new lines from the last element (if exists)

    :: Params
    - target_list : The list you wish to sanitize and remove empty elements from
    """
    # Initialize Variables
    sanitized_list = target_list.copy()
    empty_indexes = []

    # Loop through list and look for newlines
    for i in range(len(sanitized_list)):
        # Get current element
        curr_val:str = sanitized_list[i]

        # Check for new line
        if "\n" in curr_val:
            # Right-Strip newlines from the string
            curr_val = curr_val.rstrip()

            # Replace with removed string
            sanitized_list[i] = curr_val

    # Loop through list and look for empty blocks
    sanitized_list = list(filter(None, sanitized_list))

    # Output
    return sanitized_list

def find_differences(src_list, target_list):
    """
    Compare the sources list to the target 'difference' list and check if there are any missing elements that are found in the sources (primary) list but not in the difference (target) list
    by ordering the source list according to the difference list (List that you want to find the missing elements from) based on the element 'keys' order

    :: Params
    - src_list : The primary list that you want to use to cross-reference the missing elements from the difference list
        Type: List

    - target_list : The target list you want to cross-reference with the source list
        Type: List
    """
    # Initialize Variables
    new_list = [] # The new source list with duplicates removed
    difference = [] # List of duplicates found in the sources list
    src_element_Map = {} # Dictionary containing count of items

    # Loop through source list and 
    # map out number of each elements in the list
    for i in range(len(src_list)):
        # Get current element
        curr_element = src_list[i]

        # Check if current element is in the new list
        if curr_element not in target_list:
            # Element not in the target comparison list

            # Append differences
            difference.append(curr_element)

    # Output
    return difference

def find_duplicates(src_list):
    """
    Check for any duplicates in the source list and returns the de-duplicated list, and the duplicates list

    :: Params
    - src_list : The primary list that you want to use to cross-reference the missing elements from the difference list
        Type: List
    """
    # Initialize Variables
    new_list = [] # The new source list with duplicates removed
    duplicates = [] # List of duplicates found in the sources list
    src_element_Map = {} # Dictionary containing count of items

    # Loop through source list and 
    # map out number of each elements in the list
    for i in range(len(src_list)):
        # Get current element
        curr_element = src_list[i]

        # Check if current element is in the new list
        if curr_element not in src_element_Map:
            # Element not in counter dictionary/map

            # Append into new list
            new_list.append(curr_element)

            # Map new element with default counter in key-value
            src_element_Map[curr_element] = 0

        # Increment key counter
        src_element_Map[curr_element] += 1

    # Loop through key-value mapping and 
    # search for elements with more than 1 count
    for k,v in src_element_Map.items():
        if v > 1:
            # Append into duplicates list
            duplicates.append(k)

    # Output
    return [new_list, duplicates]

def order_list(order_leader_list, order_follower_list):
    """
    Order a 'follower' list according to an order 'leader' list based on the element 'keys' order

    :: Params
    - order_leader_list : The primary list you wish for the other follower lists to base its element order to
        Type: List

    - order_follower_list : The list you want to order according to the leader list
        Type: List
    """
    # Initialize Variables
    res_list = [] # Result list to hold all values

    # Convert the leader list into dictionary by using the list elements as keys to follow
    leader_dict = dict.fromkeys(order_leader_list) 

    # Convert the follower list into dictionary using the list elements as keys to follow
    follower_dict = dict.fromkeys(order_follower_list)

    # Loop through all keys of the leader dictionary
    for curr_key in leader_dict:
        # Check if the current leader key is in the current follower dictionary
        if curr_key in follower_dict:
            # Current leader key not in the current follower dictionary
            # Append current leader key into results list
            res_list.append(curr_key)

    # Convert list into dictionary using the list elements as keys to remove duplicates
    result_dict = dict.fromkeys(res_list)

    # Retrieve the keys only and convert into the results list
    res_list = list(result_dict.keys())

    # Return list
    return res_list

def order_lists(order_leader_list, order_follower_lists):
    """
    Order multiple separate order 'follower' lists according to an order 'leader' list based on the element 'keys' order

    :: Params
    - order_leader_list : The primary list you wish for the other follower lists to base its element order to
        Type: List

    - order_follower_lists : List of all lists you want to order according to the leader list
        Type: List<List>
    """
    # Initialize Variables
    leader_dict = dict.fromkeys(order_leader_list) # Convert the leader list into dictionary by using the list elements as keys to follow
    res_list = [] # Result list to hold all values

    # Loop through all follower lists
    for i in range(len(order_follower_lists)):
        # Get current follower list
        curr_follower_list = order_follower_lists[i]

        # Convert the follower list into dictionary using the list elements as keys to follow
        curr_follower_dict = dict.fromkeys(curr_follower_list)

        # Loop through all keys of the leader dictionary
        for curr_key in leader_dict:
            # Check if the current leader key is in the current follower dictionary
            if curr_key not in curr_follower_dict:
                # Current leader key not in the current follower dictionary
                # Append current leader key into results list
                res_list.append(curr_key)

    # Convert list into dictionary using the list elements as keys to remove duplicates
    result_dict = dict.fromkeys(res_list)

    # Retrieve the keys only and convert into the results list
    res_list = list(result_dict.keys())

    # Return list
    return res_list

def remove_duplicates(target_list):
    """
    Using sets to remove all duplicate values from the list by converting it into a set

    :: Params
    - target_list : The list you wish to remove duplicates from
        Type: List
    """
    # Initialize Variables

    # Convert list into set
    set_without_duplicates = set(target_list)
    
    # Convert set back into list
    list_without_duplicates = sorted(list(set_without_duplicates))
    
    # Output
    return list_without_duplicates

def import_file(f_Name):
    """
    Open and read a file into a list and return

    :: Params
    - f_Name : The name of the file
        Type: String
    """
    # Initialize Variables
    res = []
    line = ""

    # Open file for reading
    with open(f_Name, "r+") as read_file:
         # Read first line
         line = read_file.readline()

         # While there are still lines
         while line != "":
             # Append line into list
             res.append(line)

             # Read subsequent lines
             line = read_file.readline()

         # Close file after usage
         read_file.close()

    # Output
    return res

def export_file(f_Name, file_contents):
    """
    Open and write a list of contents into the file

    :: Params
    - f_Name : The name of the file
        Type: String

    - file_contents : List containing all lines of the contents to write
        Type: List
    """
    # Initialize Variables
    res = []
    line = ""

    # Open file for reading
    with open(f_Name, "a+") as export_file:
         # Loop through the list
         for i in range(len(file_contents)):
             # Get current line
             line = file_contents[i]

             # Write current line into the file
             export_file.write(line)

             # Write newline
             export_file.write("\n")

         # Close file after usage
         export_file.close()

def split_and_replace(file_contents, delimiter=","):
    """
    Take a list of file contents and process through all lines,
    split each line with the delimiter and replace the value of that index with the first index
    """
    # Initialize Variables
    res = []
    
    # Loop through all URLs
    for i in range(len(file_contents)):
        # Get current link
        curr_line = file_contents[i]

        # Split string into list by the delimiter
        delim_split = curr_line.split(delimiter)

        # Retrieve the target index and the alternative 'remainder'
        delim_split_target = delim_split[0]
        delim_split_alt = delim_split[1:]

        # Replace current index value with the URL domain
        file_contents[i] = delim_split_target

        # Append result list with the alternate/remainder after the split
        res.append(delim_split_alt)

    # Output
    return res

def get_cli_arguments():
    # Initialize Variables
    cli_arguments = {
        "positionals" : [],
        "optionals" : {

        }
    }

    # Get CLI arguments from user
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

    # Check if there are arguments
    if argc > 0:
        # There are arguments
        # Loop through counter
        for i in range(argc):
            # Get argument value
            arg = argv[i]

            # Process and check argument
            match arg:
                case _:
                    # Default: Positional argument
                    cli_arguments["positionals"].append(arg)
    else:
        # There are no arguments
        print("No arguments provided.")
        exit(1)

    # Output
    return cli_arguments

def main():
    argv = get_cli_arguments()
    argv_pos = argv["positionals"]
    argv_opt = argv["optionals"]

    # Check if positionals are provided
    if len(argv_pos) >= 2: 
        # Positionals are found

        # Get target file name and file source
        file_name = argv_pos[0]
        file_src = argv_pos[1]

        # Split file name metadata
        file_name_split = file_name.split(".")
        file_name_without_extension = file_name_split[0]
        file_ext = file_name_split[1]

        # Check if file exists
        if os.path.isfile(file_name):
            # File exists

            # Import file contents using file name
            file_contents = import_file(file_name)

            # Sanitize content list
            original_file_contents = sanitizer(file_contents)

            # Remove duplicates
            file_contents = remove_duplicates(original_file_contents)

            # Order the new file contents according to the original
            file_contents = order_list(original_file_contents, file_contents)

            # Check if there are differences
            differences = find_differences(original_file_contents, file_contents)
            if len(differences) > 0:
                print("There are elements missing:")
                for i in range(len(differences)):
                    print("{} = {}".format(i, differences))
            else:
                print("No discrepancies found.")

            # Process through file source
            match file_src:
                case "none":
                    """
                    No Split
                    """
                case "youtube" | "yt":
                    """
                    Youtube URL: truncate/split link by the '?' delimiter
                    """
                    # Initialize variables
                    delimiter = "?"

                    # Loop through all URLs
                    for i in range(len(file_contents)):
                        # Get current link
                        curr_line = file_contents[i]

                        # Split string into list by the delimiter
                        delim_split = curr_line.split(delimiter)

                        # Retrieve the domain and the search queries
                        url_domain = delim_split[0]
                        url_search_query = delim_split[1:]

                        # Replace current index value with the URL domain
                        file_contents[i] = url_domain
                case _:
                    print("Invalid file source provided: {}".format(file_src))
                    exit(1)

            # Find duplicates that was in the original list
            duplicates_removed, duplicates = find_duplicates(original_file_contents)
            print("Duplicates: {}".format(duplicates))

            # Write new file contents into a file
            output_file_name = "{}-new.{}".format(file_name_without_extension, file_ext)
            export_file(output_file_name, file_contents)
        else:
            # File does not exists
            print("File {} does not exists.".format(file_name))
    else:
        print("No positionals found.")
        print("""
Please provide 2 arguments: 
    - 1. file name and 
    - 2. the file source (i.e. yt|youtube)
              """
              )

if __name__ == "__main__":
    main()
