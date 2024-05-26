# Multithread command execution 

## Information
### Description
+ Execute multiple commands concurrently using Multithreading based on commands provided in a configuration file

### Operational Workflow
1. Define all commands you want to execute in a configuration file (JSON, YAML, TOML etc)
2. Create a new thread for all elements (aka 'task') in the list of commands to execute and store the thread in the pool
3. Execute all the threads in the pool concurrently and wait for them to be completed
4. Receive all standard outputs (if any)

### System Flow
- the application will look for commands passed via CLI positionals arguments.
    - If no commands are passed via positional arguments, the application will look for the commands list titled 'commands.json'
        + If commands.json is not found, it will then get the user's commands via user input

## Setup
### Dependencies

### Pre-Requisites
- Prepare the JSON configuration file 'commands.json' containing all the tasks you wish to execute multithreaded
    - Explanation
        - the key 'tasks' holds all commands (aka 'tasks') you wish to be executed concurrently in separate threads
            + Please refer to [Configurations](#configurations) for a full template
    ```json
    {
        "tasks" : [
            ["command-1", "arguments", "here", ...],
            ["command-2", "arguments", "here", ...],
            ["command-N", "arguments", "here", ...],
        ]
    }
    ```

## Configurations
+ Configuration File: commands.json
+ Type: JSON
- Description: This command list JSON configuration file contains all the tasks you wish to execute multithreaded
    - Explanation
        - the key 'tasks' holds all commands (aka 'tasks') you wish to be executed concurrently in separate threads

```json
{
    "tasks" : [
        ["command-1", "arguments", "here", ...],
        ["command-2", "arguments", "here", ...],
        ["command-N", "arguments", "here", ...],
    ]
}
```

## Documentations

### Synopsis/Syntax
```bash
threadexec {options} <arguments> [command-strings ...]
```

### Parameters
- Positionals
    - command-strings : Specify a list of command strings you wish to execute. Each command will be executed in its own individual thread/process and once setup is completed, the entire pool of tasks (aka commands) will be executed concurrently.
        + Type: List

- Optionals
    - With Arguments
    - Flags

### Usage
- Execute a set of command strings and output the results as JSON string
    ```bash
    threadexec "commands" "to" "be" "executed"
    ```

- Execute a set of command strings, output the results as JSON string and format the output using jq
    - Obtain the results, command, stdout and stderr
        ```bash
        threadexec "commands" "to" "be" "executed" | jq -c '.results[] | .command, .stream.stdout, .stream.stderr' -r
        ```

## TODO
+ Asynchronous execution
+ Multiprocessing for Parallel Execution
+ SSH Remote command execution with sanitization

## Resources

## References

## Remarks

