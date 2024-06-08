"""
Dictionary (Key-Value Mapping-based Container)-related helper wrapper functions and utilities

:: Notes
- Key-Value Mapping: Other names includes: Map, HashMap, Associative Array, Tables
"""
import os
import sys

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

def key_lookup(dict_obj, *keys):
    """
    Get the values of all specified keys (and nested subkeys) within the provided dictionary (Key-Value mapping; aka HashMap, Map, Table, Associative Array)

    :: Params
    - dict_obj : The target Dictionary (Key-Value) mapping you wish to search from
        + Type: dict

    - keys : List of all configuration keys to pull from the set configs
        + Type: vargs
        - Format
            + String key (1 layer) : key_lookup("key-name")
            + nested Keys (multi-layer) : key_lookup(["parent-root-key", "nested-key-1", "nested-key-2", ...])
    """
    # Initialize Variables
    results = []

    # Iterate through the keys provided
    for i in range(len(keys)):
        # Get current key
        curr_key = keys[i]

        # Check the type of the key
        match curr_key:
            case list():
                ## List element
                parent_key = curr_key[0] # Get the root key
                parent_root_val = dict_obj[parent_key] # Get the value mapped to the root key
                nested_subkeys = curr_key[1:] # Get the child subkeys under the parent key

                curr_res_val = ""
                curr_subkey_val = parent_root_val

                # Iterate the key and subkeys
                for j in range(len(nested_subkeys)):
                    # Get current subkey
                    curr_subkey = nested_subkeys[j]

                    # Get value of of subkey
                    curr_subkey_val = curr_subkey_val[curr_subkey]

                    # Set the previous value as the current value
                    curr_res_val = curr_subkey_val
            case str():
                ## String element
                curr_res_val = dict_obj[curr_key]
            case _:
                # Invalid type; Default
                curr_res_val = ""

        # Append into results
        results.append(curr_res_val)

    return results

