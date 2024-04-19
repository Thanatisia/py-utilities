# CHANGELOGS

## Table of Contents
+ [2023-12-21](#2023-12-21)
+ [2024-01-05](#2024-01-05)
+ [2024-01-30 - v0.1.0](#2024-01-30)
+ [2024-01-31](#2024-01-31)
+ [2024-03-25](#2024-03-25)
+ [2024-04-18](#2024-04-18)
+ [2024-04-19](#2024-04-19)

## Logs
### 2023-12-21
#### 2211H
+ Initial Commit

- New
    - .gitignore
    - CHANGELOGS.md
    - README.md
    - USAGE.md
    - unittest.py
    - src/
        - packages/
            - __init__.py
            - frameworks/
                - README.md
                - __init__.py
            - libraries/
                - README.md
                - __init__.py
                - sqlite_lib.py

### 2024-01-05
#### 1115H
- New
    - Added new python package library 'apg.py' in 'src/packages/libraries/' - Android Project Generator library
    - Added new directory 'scripts/' in 'src/packages/' for standalone python scripts

### 2024-01-30
#### 1608H
- New
    - Added new source file 'setup.py' in root directory
        + This is the setuptools setup.py python packaging configuration file
    - Added new source file '__init__.py' in 'src/'
    - Added new document 'README.md' in 'src/packages/scripts'
    - Added new source file '__init__.py' in 'src/packages/scripts' to initialize the package as importable

- Updates
    - Updated script 'de-duplicator.py'


#### 2055H
- Updates
    - Migrated 'python-pkgs' from 'src/' pypkgs to the root directory
        - Bug: setuptools unable to use the package without explicitly calling 'src.package-name' when the package is in a src directory layout
    - Updated USAGE.md
        - Added instructions to libraries and scripts
    - Updated setup.py
        - Converted 'src/package' => 'pypkgs'

#### 2104H
- Updated
    - Updated 'CONTRIBUTING.md'
        + Updated build steps: Fixed step to clone directly from github repository
        + Added the target branch to open a pull request to in the case you want to contribute

#### 2127H
+ Updated to v0.1.0

- New
    - Added new file '.gitmodules' for all submodules
    - Added new submodule link for framework package 'https://github.com/Thanatisia/distinstall-python'

- Updates
    - Updated document 'CONTRIBUTING.md' with new pre-requisites: git submodules

### 2024-01-31
#### 1243H
- New
    - Added new directory 'tests' for storing all unit tests
    - Added new script 'apg-generate.py'
        + Uses the AndroidProjectGenerator (apg) library as a dependency to work as a working android project file structure generator
        + You can use this as a baseline on how to use the apg library

- Updates
    - Updated 'USAGE.md'
        + Added documentations for new script 'apg-generate.py'
    - Moved 'unittest.py' from root to 'tests/'
        + Modified unittest.py to use pypkgs instead of static import
        + Renamed 'unittest.py' to 'unittest-sqlite_lib.py'

### 2024-03-25
#### 2029H
- New
    + Added new library 'mkparser.py' referenced from the makefile parser repository [Thanatisia/makefile-parser-python](https://github.com/Thanatisia/makefile-parser-python)

- Updates
    - Updated document 'USAGE.md'
        + Added reference to USAGE.md of the repository

### 2024-04-18
#### 1023H
+ Version: v0.2.0

- Version Changes
    - Mass Overhaul
        + Modernising documentations for reusability
        + Refactoring project packages
    + Renamed project repository from 'python-pkgs' to 'py-utilities'
    + Renamed package from 'pypkgs' to 'pyutils'
    + Migrated 'pypkgs' from root to 'src/'
    + Replaced python packaging script 'setup.py' to the python packaging configuration file 'pyproject.toml'
    - Updated pyproject.toml
        + Added new dependency 'distinstall-python' to 'pyproject.toml'
        + Added new dependencies
        + Updated version to 'v0.2.0'
        + Added new script 'asciinema-util' mapped to 'src/pyutils/scripts/asciinemawrapper.py'
        + Fixed CLI utility entry points
    - Renamed scripts in 'src/pyutils/scripts'
        - Removed all dashes and hyphens to comply with python packaging format and requirements
            + 'apg-generate.py' => 'apggenerate.py'
            + 'de-duplicator.py' => 'deduplicator.py'
    + Added new library 'utils.py' in 'src/pyutils/libraries' containing functions and utilities for adding information of various types (debugging, pretty-fying etc)
    + Added new script 'asciinemawrapper.py' in 'src/pyutils/scripts/'
    - Updated script 'apggenerate.py' in 'src/pyutils/scripts'
        + Replaced package import 'pypkgs' => 'pyutils'
        + Moved commands from '__name__ == "__main__".py' to 'main()'

- New
    - Added python configuration file 'pyproject.toml' to replaced python packaging script 'setup.py'
        + Added new dependency 'distinstall-python' to 'pyproject.toml'
        + Added new dependencies
        + Updated version to 'v0.2.0'
        + Added new script 'asciinema-util' mapped to 'src/pyutils/scripts/asciinemawrapper.py'
        + Fixed CLI utility entry points
    + Added new script 'asciinemawrapper.py' in 'src/pyutils/scripts/'
    + Added new library 'utils.py' in 'src/pyutils/libraries' containing functions and utilities for adding information of various types (debugging, pretty-fying etc)

- Updates
    - Updated document 'CONTRIBUTING.md'
        + Modernised and refactoring contribution steps
    - Updated document '.gitignore'
        + Added files to be ignored
    - Updated document 'README.md'
        + Refactored introductory message
    - Updated document 'USAGE.md'
        + Added new scripts
        + Updated documentations for script 'asciinema-utils'
        + Refactored documentations in general
    - Renamed scripts in 'src/pyutils/scripts'
        - Removed all dashes and hyphens to comply with python packaging format and requirements
            + 'apg-generate.py' => 'apggenerate.py'
            + 'de-duplicator.py' => 'deduplicator.py'
    - Updated script 'apggenerate.py' in 'src/pyutils/scripts'
        + Replaced package import 'pypkgs' => 'pyutils'
        + Moved commands from '__name__ == "__main__".py' to 'main()'

#### 1451H
- New
    - Added folder 'docs' for storing documentations
        + Added document 'scripts.md' housing a list of all documentations

- Updates
    - Updated document 'pyproject.toml'
        + Testing fixing of dependencies

#### 1912H
- Updates
    - Updated python packaging configuration file
        + Fixed dependencies list

#### 1916H
+ Version: v0.2.1

- Version Changes
    - Bug Fixes
        + Fixed pyproject.toml dependencies list

- New
    - Added folder 'docs' for storing documentations
        + Added document 'scripts.md' housing a list of all documentations

- Updates
    - Updated document 'README.md'
        + Updated to version v0.2.1
    - Updated python packaging configuration file 'pyproject.toml'
        + Fixed pyproject.toml dependencies list
        + Updated to version v0.2.1

#### 1932H
- Updates
    - Updated python packaging configuration file 'pyproject.toml'
        + Removed dependencies to make it less bloated

#### 1943H
- Updates
    - Updated python packaging configuration file 'pyproject.toml'
        + Removed dependencies to make it less bloated

#### 1952H
+ Version: v0.2.2

- Version Changes
    - Updated python packaging configuration file 'pyproject.toml'
        + Removed dependencies to make it less bloated

- Updates
    - Updated document 'README.md'
        + Updated to version v0.2.2
    - Updated python packaging configuration file 'pyproject.toml'
        + Removed dependencies to make it less bloated
        + Updated to version v0.2.2

#### 2033H
- Updates
    - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
        + Updated version to v0.1.1
        + Fixing bug where optional arguments (flags) are not being recognized
        + Refactoring to be more efficient

#### 2037H
- Updates
    - Updated document 'USAGE.md'
        + Cleaned up/Removed remanent backslash
    - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
        + Merged variables 'opt_with_arguments' and 'opt_Flags' together 
        + Replaced 'opt_with_Flags' with 'merged_dictionary' so that the iterator is going through every single optional arguments, not just flags

#### 2043H
+ Version: v0.2.3

- Version Changes
    - General Changes
        + Updated version of 'asciinemwrapper.py' in 'src/pyutils/scripts' to v0.1.1
    - Bug Fixes
        - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
            + Fixed bug where the optional arguments are not being processed
    - Feature change/additions
        - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
            + Merged optional arguments with value and flags together and 
            + Replaced key-value for loop with the merged dictionary

- Updates
    - Updated document 'README.md'
        + Updated to version v0.2.3
    - Updated document 'USAGE.md'
        + Cleaned up/Removed remanent backslash
    - Updated python packaging configuration file 'pyproject.toml'
        + Updated to version v0.2.3
    - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
        + Updated version to v0.1.1
        + Fixing bug where optional arguments (flags) are not being recognized
        + Refactoring to be more efficient
        + Merged variables 'opt_with_arguments' and 'opt_Flags' together 
        + Replaced 'opt_with_Flags' with 'merged_dictionary' so that the iterator is going through every single optional arguments, not just flags
        + Cleaned up and removed debug prints

### 2024-04-19
#### 1430H
+ Version: v0.2.4

- Version Changes
    - Scripts
        - 'src/pyutils/scripts/asciinemawrapper.py'
            + Updated version to v0.1.2
    - Bug Fixes
        - Error/crashes when '--asciinema-opts' is not provided but '--asciinema-agg-opts' is provided
            + Added key-value guards to check if it exists in the option dictionaries

- Updates
    - Updated document 'README.md'
        + Updated to version v0.2.4
    - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
        + Updated version to v0.1.2
        - Bug Fixes
            - Error/crashes when '--asciinema-opts' is not provided but '--asciinema-agg-opts' is provided
                + Added key-value guards to check if it exists in the option dictionaries

#### 1512H
- Updates
    - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
        + Added new function 'check_software_exists(software_name)' for checking if a software exists
        + Added new function 'validate_dependencies()' to execute during the pre-initialization setup checking if the dependencies executables exists.
        + Integrated 'validate_dependencies()' into main()

#### 1518H
- Updates
    - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
        + Removed 'subprocess.' from 'subprocess.Popen' in function 'check_software_exists()'

