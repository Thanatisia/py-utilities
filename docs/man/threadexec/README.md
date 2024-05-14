# Multithread command execution 

## Information
### Description
+ Execute multiple commands concurrently using Multithreading based on commands provided in a configuration file

### Operational Workflow
1. Define all commands you want to execute in a configuration file (JSON, YAML, TOML etc)
2. Create a new thread for all elements (aka 'task') in the list of commands to execute and store the thread in the pool
3. Execute all the threads in the pool concurrently and wait for them to be completed
4. Receive all standard outputs (if any)

## Setup
### Dependencies

### Pre-Requisites
- Prepare the JSON configuration file 'commands.json' containing all the tasks you wish to execute multithreaded
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
threadexec {options} <arguments
```

### Parameters

### Usage

## TODO
+ Asynchronous execution
+ Multiprocessing for Parallel Execution
+ SSH Remote command execution with sanitization

## Resources

## References

## Remarks

