"""
Software Code Benchmarking CLI utility
"""
import os
import sys
from subprocess import Popen, PIPE, STDOUT
from pyutils.libraries.subprocess import execute_command_communicate, execute_command_real_time
from pyutils.decorators.benchmark import benchmark, benchmark_custom

def read_file_to_list(file_name):
    # Read the input file
    with open(file_name, "r") as f_read:
        # Read all URLs into a input list
        input_data = f_read.read().strip().split("\n")
    return input_data

@benchmark_custom(return_result=True)
def execute_command(cmd_list, stream_input=None, ttl_threshold=4):
    stdout, stderr, retcode = execute_command_real_time(cmd_list, stream_input, ttl_threshold)
    return stdout, stderr, retcode

def display_results(stdout, stderr, retcode):
    # Return/Output
    print("Return Code: {}".format(retcode))
    if retcode == 0:
        print("Standard Output: {}".format(stdout.strip()))
    else:
        print("Standard Error: [{}]".format(stderr.strip()))

def start_benchmark(cmd_list, input_data, ttl_threshold=4):
    """
    Begin the benchmarking
    """
    try:
        # Begin benchmark and run program
        print("Starting Benchmark")
        print("")
        stdout, stderr, retcode = execute_command(cmd_list, stream_input=input_data, ttl_threshold=ttl_threshold)
        print("Return Code: {}".format(retcode))
    except Exception as ex:
        print("Exception: {}".format(ex))

def get_command_line_arguments():
    """
    Get Command Line Arguments and/or standard input stream
    """
    # Get executable's name
    exec = sys.argv[0]

    # Use stdin stream if its full
    if not sys.stdin.isatty():
        # Initialize Variables
        argv = []

        # Get standard input stream
        in_stream = sys.stdin

        # Process standard input
        for line in in_stream:
            # Sanitize current line
            line = line.strip()

            # Split the line into elements to accept pipe/stream arguments
            elements = line.split()

            for val in elements:
                # Append into arguments list
                argv.append(val)
    else:
        # Get CLI arguments
        argv = sys.argv[1:]

    # Calculate argument count
    argc = len(argv)

    return [exec, argv, argc]

def main():
    # Initialize Variables
    i = 0
    cmd_list = []
    input_data = []

    # Get CLI arguments
    exec, argv, argc = get_command_line_arguments()

    print("Arguments ({}) : {}".format(argc, argv))

    # Check if there are arguments provided
    if argc > 0:
        # Arguments provided
        while i < argc:
            # Get current argument
            curr_arg = argv[i]

            # Switch-case current argument/line
            match curr_arg:
                case "-h" | "--help":
                    # Display help
                    print("HELP")
                case "--set-command":
                    """
                    Set the command string
                    """
                    # Check if option argument is provided by user
                    next_index = i+1
                    if next_index <= argc:
                        # Get command string from user
                        arg_value = argv[next_index]

                        # Split the string into a list
                        cmd_list = arg_value.split(" ")

                        # Shift 1 position to the right and jump to the following argument
                        i += 1
                case "--set-stdin-data":
                    """
                    Set the stdin stream data to pass into the command
                    """
                case "--input-file":
                    """
                    Read the input file into a standard input stream data
                    """
                    # Check if option argument is provided by user
                    next_index = i+1
                    if next_index < argc:
                        # Get command string from user
                        arg_value = argv[next_index]

                        # Read the file contents and store into a list
                        input_data = read_file_to_list(arg_value)

                        # Shift 1 position to the right and jump to the following argument
                        i += 1
                case "start":
                    # Prepare command list
                    # cmd_list = ["yt-obtain-url"]
                    # cmd_list = ["ip", "a", "s"]
                    # cmd_list = ["ping", "-c", "5", "8.8.8.8"]

                    # Check if command list is provided
                    if len(cmd_list) == 0:
                        print("Command not provided.")
                    else:
                        # Print information
                        print("[i] Executing command: {}".format(cmd_list))
                        print("[i] Standard Input (stdin) stream data: {}".format(input_data))

                        # begin benchmarking
                        start_benchmark(cmd_list, input_data, ttl_threshold=2)
                case _:
                    # Default action
                    print("Invalid option/positional: {}".format(curr_arg))

            # Increment line number
            i += 1
    else:
        print("No arguments provided.")

if __name__ == "__main__":
    main()

