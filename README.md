# My All-in-One library/package/framework collection for Python

## Information

### Background Summary
+ A python one-stop-shop mono-repo containing various useful python utilities, packages/frameworks/libraries that you can just install and use

### Project
+ Current Version: v0.2.7

## Setup
### Dependencies
+ python3
+ pip

### Pre-Requisites
- Generate Python Virtual Environment
    - Create Virtual Environment
        ```bash
        python3 -m venv [virtual-environment-name]
        ```
    - Chroot into Virtual Environment
        - Linux
            ```bash
            . [virtual-environment-name]/bin/activate
            ```
        - Windows
            ```bash
            .\[virtual-environment-name]\Scripts\activate
            ```

### Installing
- Using python pip
    - Install git repository
        ```bash
        python3 -m pip install git+https://github.com/Thanatisia/py-utilities{@[branch-tag-name]}
        ```

- Manually via cloning
    - Clone git repository
        ```bash
        git clone https://github.com/Thanatisia/py-utilities
        ```
    - Change directory into project root
        ```bash
        cd py-utilities
        ```
    - (Optional) Install python dependencies
        ```bash
        python3 -m pip install -Ur requirements.txt
        ```
    - Install package as development mode
        ```bash
        pip install .
        ```
    - (Optional) Uninstall package
        ```bash
        pip uninstall py-utilities
        ```

### Embedding library in your own project
- Change directory into your project root containing the git folder
    ```console
    cd [project-root]
    ```

- Importing as a git submodule
    ```console
    git submodule add https://github.com/Thanatisia/py-utilities
    ```

### Following usage setup
- Initialization after cloning project
    ```console
    git submodule --init
    ```

## Documentations

## Wiki
### Project Structure
- root/
    - src/
        - pyutils/
            - frameworks/ : Place all frameworks and multi-library files here
            - libraries/  : Place all standalone libraries/modules and classes here
            - scripts/    : Place all scripts/CLI utilities here

## Resources

## References

## Remarks

