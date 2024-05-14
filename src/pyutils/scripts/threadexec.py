"""
Multithread exec
"""
import os
import sys
import json
import threading
from subprocess import Popen, PIPE

results = []
def exec(task, test_command=False):
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
    argv = []

    # Check if file exists
    if os.path.isfile(json_commands_file):
        # Open the JSON file to obtain the file pointer
        with open(json_commands_file, "r") as read_json_commands_list:
            # Load and read JSON file containing the commands and arguments into system buffer/memory
            json_config_Contents = json.load(read_json_commands_list)

            # Close file after usage
            read_json_commands_list.close()

        # Print JSON configuration file contents
        print("JSON Configuration file contents: {}".format(json_config_Contents))

        # Obtain commands list
        json_tasks = json_config_Contents["tasks"]
        # Iterate through all tasks and append into commands list
        for task in json_tasks:
            argv.append(task)
    else:
        # Commands list not provided
        print("JSON file '{}' not found".format("commands.json"))
        # Obtain commands from user
        line = ""
        argv = []

        print("Please enter all your commands to execute (Press 'enter' without any texts to exit): ")
        line = input("> ")
        while line:
            # Get next line
            line = input("> ")

            # Check if line is empty
            if line != "":
                # Split the line into a list
                curr_command_list = line.split(" ")

                # Append current list into the command list
                argv.append(curr_command_list)
            else:
                break

    # Get argument count
    argc = len(argv)

    # Calculate number of threads to create
    number_of_threads = len(argv)

    # Check if there are any tasks
    if argc > 0:
        for i in range(number_of_threads):
            # Get current task
            task = argv[i]

            # Initialize new Thread for the current task
            thread = threading.Thread(target=exec, args=(task,))

            # Store current thread in a thread pool
            thread_pool.append(thread)

        # Iterate through all threads in the pool and start
        for thread in thread_pool: 
            print("[i] Starting thread: {}".format(thread.name))
            thread.start()

        # Create a mapping of the created threads in the threads_status container for storing the alive status of the threads
        for thread in thread_pool:
            threads_status[thread] = thread.is_alive()

        # Iterate through all threads in the pool and wait for the thread to complete
        for thread in thread_pool: 
            print("[i] Waiting for thread to complete: {}".format(thread.name))
            thread.join()

        print("[+] Threads completed.")

        # Print results
        for i in range(len(results)):
            # Get current result
            curr_task = results[i]

            # Iterate through current task
            for k,v in curr_task.items():
                print("{} = {}".format(k,v))

            print("")
    else:
        print("[i] No arguments provided.")

if __name__ == "__main__":
    main()

