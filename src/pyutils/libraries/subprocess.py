import os
import sys
from subprocess import Popen, PIPE, DEVNULL

def sync_exec(cmd_list:list, **kwargs):
    """
    Synchronously execute command with state communication

    :: Params
    - cmd_list : Specify a list of commands to execute
        + Type: List
    - **kwargs : Specify all variable-length keyword arguments you wish to pass into subprocess.Popen()
        + Type: Variable-Length kwargs; Dictionary

    :: Notes
    - This is similar to 'execute_command_communicate' except this has kwargs
    """
    # Initialize Variables
    rc:int = -1
    res_stdout = ""
    res_stderr = ""

    # Open a subprocess pipe to execute the command
    with Popen(cmd_list, **kwargs) as proc:
        # Synchronously execute command and communicate
        res_stdout, res_stderr = proc.communicate()

        # Get result status code
        rc = proc.returncode

    # Decode results
    if (res_stdout != None):
        res_stdout = res_stdout.decode("utf-8")
    else:
        res_stdout = ""
    if (res_stderr != None):
        res_stderr = res_stderr.decode("utf-8")
    else:
        res_stderr = ""

    # Return result
    return [res_stdout, res_stderr, rc]

def execute_command_communicate(cmd_list, stream_input=None):
    """
    Execute the provided command, as well as the standard input stream data required.
    The commands are executed in the background by subprocess.Popen and only after the program has been successfully completed will it release the standard output, error and return code to the caller

    :: Params
    - cmd_list : Specify a list of commands to execute
        + Type: List
    - stream_input : Specify a list of data to be passed into the command's stdin stream
        + Type: List
        + Default: None
    """
    # Initialize Variables
    stdout = ""
    stderr = ""
    retcode = -1

    try:
        # Open a subprocess process pipe and execute command in benchmark
        with Popen(cmd_list, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            # Check if input stream data is specified
            if stream_input is not None:
                stream_input = stream_input.encode("utf-8")

            # Execute command and return standard output
            proc_res = proc.communicate(input=stream_input)
            stdout = proc_res[0]
            stderr = proc_res[1]
            retcode = proc.returncode

            # Check for errors
            if retcode != 0:
                if stderr != None:
                    stderr = stderr.decode("utf-8")
            else:
                if stdout != None:
                    stdout = stdout.decode("utf-8")
    except Exception as ex:
        print("Exception: {}".format(ex))

    # Output/Return
    return stdout, stderr, retcode

def execute_command_real_time(cmd_list, stream_input=None, ttl_threshold=4):
    """
    Execute the provided command, as well as the standard input stream data required.
    The commands are printed in real time, line by line

    :: Params
    - cmd_list : Specify a list of commands to execute
        + Type: List
    - stream_input : Specify a list of data to be passed into the command's stdin stream
        + Type: List
        + Default: None
    - ttl_threshold : Specify the Time-to-Live max counter before the system closes the process
        + Type: Integer
        + Default: 4
    """
    # Initialize Variables
    line = ""
    stdout = ""
    stderr = ""
    retcode = -1
    ttl_counter = 0

    # Open a subprocess process pipe and execute command in benchmark
    proc = Popen(cmd_list, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    # Write standard input stream (stdin) into the subprocess
    if (stream_input is not None) and (len(stream_input) > 0):
        if proc.stdin != None:
            for element in stream_input:
                # Write the standard input data into the pipe's stream with a newline to end that entry
                proc.stdin.write("{}\n".format(element).encode("utf-8"))

            # Close the standard input pipe after writing to stop deadlock
            proc.stdin.close()

    # Create a while loop to keep looping until there are no more output/not polling (aka a return code is produced (0 = Success, > 0 = Error))
    print("Polling...", flush=True)

    while True:
        # Check if the subprocess standard output stream has data
        if proc.stdout != None:
            # Read the next line
            line = proc.stdout.readline()

        # Break Condition: Check if the process is still running (status code not produced yet) and if there are output
        if not line and proc.poll() is not None:
            # If the output is empty AND process is no longer running
            break

        # Time-to-Live (TTL) Condition: Check if the process is still running after a set amount of lines has passed
        if not line and proc.poll() is None:
            # Check if counter has reached the threshold
            if ttl_counter == ttl_threshold:
                # Exit
                break

            # Increment counter
            ttl_counter += 1

        # Null Validation: Check line is found
        if line != "":
            # Decode the encoded string
            line = line.decode().rstrip()
            print("{}".format(line))
            # Write the line to the standard output
            stdout += line

    # Wait for the process to finish and get return code
    retcode = proc.wait()

    # Output/Return
    return stdout, stderr, retcode


