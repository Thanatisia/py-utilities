"""
Multithread exec
"""
import os
import sys
import json
import threading
from subprocess import Popen, PIPE

results = []
results_mapping = {
    # Contains the results of the command execution
    # results : [
    #   { "thread-id" : thread_id, "command" : command, "stream" : { "stdin" : stdin, "stdout" : stdout, "stderr" : stderr } }
    # ]
    "results" : []
}
def exec(task, index=0, test_command=False):
    """
    Execute the given task
    """
    # Check if flag 'test_command' is Enabled
    if test_command:
        # Debug: Only print out the command/task to validate
        print("Executing: {}".format(task))
    else:
        # Sanitization: Convert the task command list elements into string before proceeding
        for i in range(len(task)): task[i] = str(task[i])

        # Open a Subprocess pipe and execute the task command
        with Popen(task, stdout=PIPE, stdin=PIPE, stderr=PIPE) as proc:
            # Execute task and communicate
            res = proc.communicate()
            stdout = res[0]
            stderr = res[1]

        # Decode if any
        if stdout != "":
            stdout = stdout.decode("utf-8")
        if stderr != "":
            stderr = stderr.decode("utf-8")

        # Return result of current task
        results.append({"task" : task, "stdout" : stdout, "stderr" : stderr})

        # Store the current tasks' stdout and stderr to the corresponding results mappings
        results_mapping["results"][index]["stream"]["stdout"] = stdout
        results_mapping["results"][index]["stream"]["stderr"] = stderr

def main():
    # Initialize Variables
    thread_pool = []
    threads_status = {} # Container for storing the alive status of all the created threads
    json_commands_file = "commands.json"
    json_config_Contents = {}
    json_supported_keys = [
        "multithread", # All commands that is to be executed concurrently on multiple threads
        "serial", # All commands that is to be executed serially (Back to back)
        "main", # All commands that is to be executed on the Main system thread
    ]
    cmdlist = []
    sstream_msg = [] # Standard Output messages that are to be printed are stored here
    verbose = False # Enable/Disable message output except the final standard output
    export_format = ["text", "json"][1] # Specify the format to print the final standard output results to the user (formats: text, json)

    # Get CLI arguments
    argv = sys.argv[1:] # Obtain all commands to be executed (separated by space delimiter)
    argc = len(argv)

    # Check if there are arguments provided
    if argc == 0:
        # No arguments (commands) provided : Import via JSON configuration file

        # Check if file exists
        if os.path.isfile(json_commands_file):
            # Open the JSON file to obtain the file pointer
            with open(json_commands_file, "r") as read_json_commands_list:
                # Load and read JSON file containing the commands and arguments into system buffer/memory
                json_config_Contents = json.load(read_json_commands_list)

                # Close file after usage
                read_json_commands_list.close()

            if verbose:
                # Print JSON configuration file contents
                print("[i] JSON Configuration file contents: {}".format(json_config_Contents))

            # Obtain commands list
            json_tasks = json_config_Contents["tasks"]
            # Iterate through all tasks and append into commands list
            for task in json_tasks:
                cmdlist.append(task)
        else:
            # Commands list not provided

            if verbose:
                print("[WARN] JSON file '{}' not found".format("commands.json"))

            # Obtain commands from user
            line = ""
            cmdlist = []

            print("Please enter all your commands to execute (Press 'enter' without any texts to exit): ")
            line = input("> ")
            while line:
                # Check if line is empty
                if line != "":
                    # Split the line into a list
                    curr_command_list = line.split(" ")

                    # Append current list into the command list
                    cmdlist.append(curr_command_list)
                else:
                    break
                # Get next line
                line = input("> ")
    else:
        # Iterate through arguments provided
        for i in range(argc):
            # Get current command
            curr_cmd_str = argv[i]

            # Split the current command into a list
            curr_cmd_list = curr_cmd_str.split(" ")

            # Append into the command list
            cmdlist.append(curr_cmd_list)

    # Get argument count
    number_of_commands = len(cmdlist)

    # Calculate number of threads to create
    number_of_threads = number_of_commands

    # Check if there are any tasks
    if number_of_commands > 0:
        for i in range(number_of_threads):
            # Get current task
            task = cmdlist[i]

            # Initialize new Thread for the current task
            thread = threading.Thread(target=exec, args=(task, i,))

            # Initialize results dictionary
            results_mapping["results"].append({"thread" : { "id" : i, "name" : str(thread.getName()), "object" : str(thread),}, "command" : task, "stream" : {"stdin" : "", "stdout" : "", "stderr" : ""}})

            # Store current thread in a thread pool
            thread_pool.append(thread)

        # Iterate through all threads in the pool and start
        for thread in thread_pool: 
            if verbose:
                print("[i] Starting thread: {}".format(thread.name))
            thread.start()

        # Create a mapping of the created threads in the threads_status container for storing the alive status of the threads
        for thread in thread_pool:
            threads_status[thread] = thread.is_alive()

        # Iterate through all threads in the pool and wait for the thread to complete
        for thread in thread_pool: 
            if verbose:
                print("[i] Waiting for thread to complete: {}".format(thread.name))
            thread.join()

        if verbose:
            print("[+] Threads completed.")

        # Print results
        for i in range(len(results)):
            # Get current result
            curr_task = results[i]

            # Get current task, standard output and standard error
            curr_task_command = curr_task["task"]
            curr_task_stdout = curr_task["stdout"]
            curr_task_stderr = curr_task["stderr"]

        # Match-case the standard output formats
        match export_format:
            case "text":
                # Get results
                output = results_mapping["results"]

                # Iterate through results
                for i in range(len(output)):
                    # Get current element
                    curr_element = output[i]

                    # Get current command
                    curr_command = curr_element["command"]

                    # Get task results
                    curr_stream = curr_element["stream"]
                    curr_stream_stdout = curr_stream["stdout"]
                    curr_stream_stderr = curr_stream["stderr"]

                    # Print standard output
                    print("[i] Command: {}".format(curr_command))
                    if curr_stream_stdout != "":
                        print("[i]\tStandard Output:\n{}".format(curr_stream_stdout))
                    if curr_stream_stderr != "":
                        print("[i]\tStandard Error:\n{}".format(curr_stream_stderr))
                    print("")

            case "json":
                # Convert and Parse result_mapping dictionary object to JSON string
                json_str = json.dumps(results_mapping, indent=4)

                # Print JSON string
                print(json_str)
            case _:
                print("[-] Invalid format: {}".format(export_format))
    else:
        print("[i] No arguments provided.")

if __name__ == "__main__":
    main()

