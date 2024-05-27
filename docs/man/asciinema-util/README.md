# asciinema-util

## Information
### Description
+ Terminal recorder using asciinema and convert to gif using asciinema-agg

### Notes

## Setup
### Dependencies
+ python
+ python-pip
+ rust
+ cargo
- asciinema : In python
    - Install using python-pip
        ```bash
        python3 -m pip install asciinema
        ```
- asciinema-agg : In cargo
    - Update rust (and cargo) using rustup
        ```bash
        rustup
        ```
    - Install using cargo
        ```bash
        cargo install --git https://github.com/asciinema/agg
        ```

### Pre-Requisites

## Documentations

### Synopsis/Syntax
- Standard
    ```bash
    asciinema-util {options} <arguments> [actions (record|convert)]
    ```

### Parameters
- Positionals
    + record  : Begin recording the screen terminal using asciinema
    + convert : Convert the terminal screen recording into an animation gif using asciinema-agg

- Optionals
    - With Arguments
        + `-c | --command [command-to-execute]`       : Specify a command to execute in asciinema to record
        + `-t | --theme [theme-name]`                 : Specify the theme to apply to the terminal background in the recording
        + `--output-terminal-rec-filename [filename]` : Specify the file name of the terminal recording output file
        + `--output-animation-filename    [filename]` : Specify the file name of the output converted animation GIF 
        + `--input-terminal-rec-filename  [filename]` : Specify the target file name of the terminal recording file you want to convert via asciinema-agg
        + `--asciinema-opts [other opts ...]`         : Specify all options you want to pass into asciinema
        + `--asciinema-agg-opts [other opts ...]`     : Specify all options you want to pass into asciinema-agg

    - Flags
        + --debug : Set program to 'debug mode'; All commands will be printed out instead
        + -h | --help : Display help message
        + -v | --version : Display system version
        + --print-opts-all : Print all optionals (with arguments and flags)
        + --print-opts-with-arguments : Print all optionals with arguments
        + --print-opts-flags : Print all flags (optionals without arguments)

### Usage
- Record terminal screen using asciinema
    ```bash 
    asciinema-util record -c 'make' --output-terminal-rec-filename output.cast
    ```
- Convert the terminal recording into animation gif using asciinema (with gifski)
    ```bash
    asciinema-util convert --theme solarized-light --input-terminal-rec-filename output.cast --output-animation-filename output.gif
    ```
- Record terminal screen using asciinema and convert recording to gif using asciinema-agg
    ```bash 
    asciinema-util \
        record -c make --output-terminal-rec-filename output.cast \
        convert --theme solarized-light --input-terminal-rec-filename output.cast --output-animation-filename output.gif
    ```
- Set mode to debug and print out the commands instead of executing directly
    ```bash
    asciinema-util --debug
    ```
- Passthrough CLI arguments 
    - into asciinema directly
        ```bash
        asciinema-util --asciinema-opts "options here ..."
        ````
    - into asciinema-agg directly
        ```bash
        asciinema-util --asciinema-agg-opts "options here ..."
        ```
- All-in-One record and convert 
    ```bash
    asciinema-util \
        --debug \
        record --output-terminal-rec-filename output.cast --asciinema-opts '--overwrite' -c "commands arguments values" \
        convert --theme solarized-light --input-terminal-rec-filename output.cast --output-animation-filename output.gif  --asciinema-agg-opts '--cols 71 --rows 13 --font-size 16'
    ```

## TODO
+ Optional argument customizations in the form of flags

## Resources

## References

## Remarks

