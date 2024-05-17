# CHANGELOGS

## Table of Contents
+ [2023-12-21](#2023-12-21)
+ [2024-01-05](#2024-01-05)
+ [2024-01-30 - v0.1.0](#2024-01-30)
+ [2024-01-31](#2024-01-31)
+ [2024-03-25](#2024-03-25)
+ [2024-04-18](#2024-04-18)
+ [2024-04-19](#2024-04-19)
+ [2024-04-20](#2024-04-20)
+ [2024-04-27](#2024-04-27)
+ [2024-04-28](#2024-04-28)
+ [2024-05-15](#2024-05-15)
+ [2024-05-16](#2024-05-16)
+ [2024-05-18](#2024-05-18)

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

#### 1541H
- Updates
    - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
        + Fixed bug with 'check_software_exists()' where process pipe will print result to standard output

#### 1605H
- Updates
    - Updated document 'USAGE.md'
        + Added pre-requisites and setup
    - Updated document 'scripts.md' in 'docs/'
        + Added information and documentation for script 'asciinema-util'

#### 1613H
+ Version: v0.2.5

- Version Changes
    - Scripts
        - 'src/pyutils/scripts/asciinemawrapper.py'
            + Updated version to v0.1.3
            + Added new function 'check_software_exists(software_name)' for checking if a software exists
            + Added new function 'validate_dependencies()' to execute during the pre-initialization setup checking if the dependencies executables exists.
            + Integrated 'validate_dependencies()' into main()
    - Bug Fixes
        - Fixed bug issue where application crashes if the dependency application/executable isnt found
            + Added a dependency checker
    - Documentations
        - 'USAGE.md'
            + Added pre-requisites and setup
        - 'docs/scripts.md'
            + Added information and documentation for script 'asciinema-util'

- Updates
    - Updated document 'README.md'
        + Updated to version v0.2.5
    - Updated python packaging configuration file 'pyproject.toml'
        + Updated to version v0.2.5
    - Updated document 'USAGE.md'
        + Added pre-requisites and setup
    - Updated document 'scripts.md' in 'docs/'
        + Added information and documentation for script 'asciinema-util'
    - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
        + Updated version to v0.1.3
        - Bug Fixes
            - Fixed bug issue where application crashes if the dependency application/executable isnt found
                + Added a dependency checker
        + Added new function 'check_software_exists(software_name)' for checking if a software exists
        + Added new function 'validate_dependencies()' to execute during the pre-initialization setup checking if the dependencies executables exists.
        + Integrated 'validate_dependencies()' into main()

#### 0006H
+ Version: v0.2.6

- Version Changes
    - New Files
        + Added new python packages and depedencies file 'requirements.txt'
    - Bug Fixes
        - 'src/pyutils/scripts/asciinemwrapper.py'
            + Fixed bug where parsing '--asciinema-agg-opts' will result in an error due to command line parsing issue
    - Feature Changes
        - 'src/pyutils/scripts/asciinemwrapper.py'
            + Replaced debug print from string to list for improved clarity

- New
    + Added new python packages and depedencies file 'requirements.txt'

- Updates
    - Updated document 'README.md'
        + Updated to version v0.2.6
    - Updated python packaging configuration file 'pyproject.toml'
        + Updated to version v0.2.6
    - Updated document 'scripts.md' in 'docs/'
        + Updated version for 'asciinema-util' to v0.1.4
    - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
        + Updated version to v0.1.4
        + Replaced debug print from string to list for improved clarity
        - Bug Fixes
            + Fixed bug where parsing '--asciinema-agg-opts' will result in an error due to command line parsing issue

#### 1012H
- Updates
    - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
        + Added new function 'format_argument_key_values(cmd_list, opts)' for searcing for all CLI argument key-values and storing them into a list properly
        - Bug Fixes
            + Moved the statements used to fix the '--asciinema-agg-opts' argument parser into a dedicated function 'format_argument_key_values(cmd_list, opts)'
            + Fixed bug where parsing '--asciinema-opts' will result in an error due to command line parsing issue

#### 1653H
- Updates
    - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
        + Added information printing to before recording and converting

#### 2131H
+ Version: v0.2.7

- Version Changes
    - Bug Fixes
        - 'src/pyutils/scripts/asciinemwrapper.py'
            + Moved the statements used to fix the '--asciinema-agg-opts' argument parser into a dedicated function 'format_argument_key_values(cmd_list, opts)'
            + Fixed bug where parsing '--asciinema-opts' will result in an error due to command line parsing issue
    - Feature Changes
        - 'src/pyutils/scripts/asciinemwrapper.py'
            + Added new function 'format_argument_key_values(cmd_list, opts)' for searcing for all CLI argument key-values and storing them into a list properly
            + Added information printing to before recording and converting

- Updates
    - Updated document 'README.md'
        + Updated to version v0.2.7
    - Updated python packaging configuration file 'pyproject.toml'
        + Updated to version v0.2.7
    - Updated document 'scripts.md' in 'docs/'
        + Updated version for 'asciinema-util' to v0.1.5
    - Updated script 'asciinemawrapper.py' in 'src/pyutils/scripts'
        + Updated version to v0.1.4
        + Added new function 'format_argument_key_values(cmd_list, opts)' for searcing for all CLI argument key-values and storing them into a list properly
        + Added information printing to before recording and converting
        - Bug Fixes
            + Moved the statements used to fix the '--asciinema-agg-opts' argument parser into a dedicated function 'format_argument_key_values(cmd_list, opts)'
            + Fixed bug where parsing '--asciinema-opts' will result in an error due to command line parsing issue

### 2024-04-27
#### 1401H
- New
    - Added new directory 'decorators' in 'src/pyutils/' to hold all decorators
        + Added new module 'benchmark.py' containing decorator functions for benchmarking

    + Added new unit test 'test-decorators.py' in 'tests/' containing unit tests for decorators

#### 1403H
+ Version: v0.2.8

- Version Changes
    - Bug Fixes
    - Additions
        - Added new directory 'decorators' in 'src/pyutils/' to hold all decorators
            + Added new module 'benchmark.py' containing decorator functions for benchmarking
        + Added new work-in-progress CLI utility 'benchmark.py' in 'src/pyutils/scripts': A Software test benchmarker for python that aims to make python code testing easier on the shell/TTY level
    - Feature Changes

- New
    - Added new directory 'decorators' in 'src/pyutils/' to hold all decorators
        + Added new module 'benchmark.py' containing decorator functions for benchmarking
    + Added new unit test 'test-decorators.py' in 'tests/' containing unit tests for decorators
    + Added new work-in-progress CLI utility 'benchmark.py' in 'src/pyutils/scripts': A Software test benchmarker for python that aims to make python code testing easier on the shell/TTY level

- Updates
    - Updated document 'README.md'
        + Updated version to 'v0.2.8'
        + Updated documentations to include more context
    - Updated python packaging configuration file 'pyproject.toml'
        + Updated version to 'v0.2.8'
        + Added new work-in-progress CLI utility 'benchmarker'
    - Updated document 'USAGE.md'
        + Added information on the decorator functions
    - Updated document 'scripts.md' in 'docs/'
        + Added Work-in-Progress CLI utility 'benchmarker.py' to the list
    - Updated decorator 'benchmarker.py' in 'src/pyutils/decorators/'
        + Replaced description

#### 1535H
+ Version: v0.2.9

- Version Changes
    - Bug Fixes
    - Additions
    - Feature Changes
        - Updated decorator 'benchmark.py' in 'src/pyutils/decorators'
            + Added new argument 'return_result=False' to 'benchmark_custom': Enable (set this to true) if your function requires returning of a result

- Updates
    - Updated document 'README.md'
        + Updated version to 'v0.2.9'
    - Updated python packaging configuration file 'pyproject.toml'
        + Updated version to 'v0.2.9'
    - Updated document 'USAGE.md'
        + Added information on the decorator functions
    - Updated decorator 'benchmark.py' in 'src/pyutils/decorators/'
        + Implemented new argument key-value to decorator function 'benchmark_custom'

### 2024-04-28
#### 2232H
- New
    + Added new module 'subprocess.py' in 'src/pyutils/libraries/': A library/module that uses subprocess containing functions/implementation of executing commands either via 'subprocess.Popen().communicate()' or print in real time

- Updates
    - Updated module 'benchmark.py' in 'src/pyutils/decorators/'
        + Added new benchmark decorator function 'benchmark_loops()' for benchmarking functions by repeating the function N times
    - Updated benchmarker CLI utility source file 'benchmark.py' in 'src/pyutils/scripts/'
        + Updated version to 'v0.2.0'
        + Implemented a working benchmarker CLI utility containing arguments, to be improved
    - Updated unit test 'test-decorators.py' in 'tests/'
        + Added unit test for 'benchmark_loops'

#### 2239H
+ Version: v0.3.0

- Version Changes
    - Bug Fixes
    - Additions
        + Added new module 'subprocess.py' in 'src/pyutils/libraries/': A library/module that uses subprocess containing functions/implementation of executing commands either via 'subprocess.Popen().communicate()' or print in real time
    - Feature Changes
        - Updated module 'benchmark.py' in 'src/pyutils/decorators/'
            + Added new benchmark decorator function 'benchmark_loops()' for benchmarking functions by repeating the function N times
        - Updated benchmarker CLI utility source file 'benchmark.py' in 'src/pyutils/scripts/'
            + Implemented a working benchmarker CLI utility containing arguments, to be improved

- New
    + Added new module 'subprocess.py' in 'src/pyutils/libraries/': A library/module that uses subprocess containing functions/implementation of executing commands either via 'subprocess.Popen().communicate()' or print in real time

- Updates
    - Update document 'README.md'
        + Updated version to 'v0.3.0'
    - Updated python packaging configuration file 'pyproject.toml'
        + Updated version to 'v0.3.0'
    - Updated document 'scripts.md' in 'docs/'
        + Updated version to 'v0.2.0'
    - Updated document 'USAGE.md'
        + Added documentations for CLI utility 'benchmarker'
    - Updated module 'benchmark.py' in 'src/pyutils/decorators/'
        + Added new benchmark decorator function 'benchmark_loops()' for benchmarking functions by repeating the function N times
    - Updated benchmarker CLI utility source file 'benchmark.py' in 'src/pyutils/scripts/'
        + Updated version to 'v0.2.0'
        + Implemented a working benchmarker CLI utility containing arguments, to be improved
    - Updated unit test 'test-decorators.py' in 'tests/'
        + Added unit test for 'benchmark_loops'

### 2024-05-15
#### 1442H
- New
    - Added new directory 'man' in 'docs/'
        - Added new manual directory 'threadexec'
            + Added new document 'README.md'
            + Added new template JSON file 'commands.json': example configuration file for threadexec
        - Added new manual directory 'treeewalk'
            + Added new document 'README.md'
        - Added new manual directory 'git-mass-update'
            + Added new document 'README.md'
    - Added new library 'treelib.py' in 'src/pyutils/libraries/'
    - Added new CLI scripts to 'src/pyutils/scripts'
        + gitmassupdate.py
        + threadexec.py
        + treetraversal.py

- Updates
    - Updated Python packaging configuration file 'pyproject.toml'
        - Added CLI executables
            + threadexec
            + treewalk
            + git-mass-update
    - Updated library module 'subprocess.py' in 'src/pyutils/libraries/'
        + Added library variable 'path_separator' for obtaining the detected operating system's path separator (i.e. '/' for Liux, '\\' for Windows)
        + Added function 'sync_exec': Uses .communicate() but contains kwargs for customizability

#### 1606H
- Updates
    - Updated document 'scripts.md' in 'docs/'
        - Added new scripts
            + threadexec
            + treewalk
            + git-mass-update

### 2024-05-16
#### 0948H
+ Version: v0.4.0

- Version Changes
    - Bug Fixes
    - Additions
        - Added new directory 'man' in 'docs/'
            - Added new manual directory 'threadexec'
                + Added new document 'README.md'
                + Added new template JSON file 'commands.json': example configuration file for threadexec
            - Added new manual directory 'treeewalk'
                + Added new document 'README.md'
            - Added new manual directory 'git-mass-update'
                + Added new document 'README.md'
        + Added new library 'treelib.py' in 'src/pyutils/libraries/'
        - Added new CLI scripts to 'src/pyutils/scripts'
            + gitmassupdate.py
            + threadexec.py
            + treetraversal.py
    - Feature Changes

- New
    - Added new directory 'man' in 'docs/'
        - Added new manual directory 'threadexec'
            + Added new document 'README.md'
            + Added new template JSON file 'commands.json': example configuration file for threadexec
        - Added new manual directory 'treeewalk'
            + Added new document 'README.md'
        - Added new manual directory 'git-mass-update'
            + Added new document 'README.md'
    - Added new library 'treelib.py' in 'src/pyutils/libraries/'
    - Added new CLI scripts to 'src/pyutils/scripts'
        + gitmassupdate.py
        + threadexec.py
        + treetraversal.py

- Updates
    - Update document 'README.md'
        + Updated version to 'v0.4.0'
    - Updated python packaging configuration file 'pyproject.toml'
        - Added CLI executables
            + threadexec
            + treewalk
            + git-mass-update
        + Updated version to 'v0.4.0'
    - Updated document 'USAGE.md'
        + Added script entries
    - Updated library module 'subprocess.py' in 'src/pyutils/libraries/'
        + Added library variable 'path_separator' for obtaining the detected operating system's path separator (i.e. '/' for Liux, '\\' for Windows)
        + Added function 'sync_exec': Uses .communicate() but contains kwargs for customizability
    - Updated document 'scripts.md' in 'docs/'
        - Added new scripts
            + threadexec
            + treewalk
            + git-mass-update

#### 1041H
+ Version: v0.4.1

- Version Changes
    - Bug Fixes
    - Additions
    - Feature Changes
        - Updated script 'treetraversal.py' in 'src/pyutils/scripts'
            + Added 'delimiter' into the function argument header of 'print_git_repositores()' for optionals
            + Replaced delimiter ':' with '=' so as not to collide with system path handling when working with filters

- Updates
    - Update document 'README.md'
        + Updated version to 'v0.4.1'
    - Updated python packaging configuration file 'pyproject.toml'
        + Updated version to 'v0.4.1'
    - Updated document 'scripts.md' in 'docs/'
        + Updated version of 'treewalk' to 'v0.1.1'
    - Updated script 'treetraversal.py' in 'src/pyutils/scripts'
        + Added 'delimiter' into the function argument header of 'print_git_repositores()' for optionals
        + Replaced delimiter ':' with '=' so as not to collide with system path handling when working with filters

#### 1816H
- New
    - Added new Makefile 'documentations.Makefile' in 'docs/'
        + Added custom Makefile specifically for recording screen recording using asciinema and generating documentation GIF by converting the screen recording using asciinema-agg
- Updates
    - Updated document 'README.md'
        + Added documentation step - generating demo animation GIF using aciinema-agg and custom Makefile

#### 2219H
- Updates
    - Updated script 'treetraversal.py' in 'src/pyutils/scripts'
        + Adding JSON support and multi-standard output format/type (WIP)

#### 2249H
- Updates
    - Updated document 'README.md'
        + Added new notes for documentation
    - Updated Makefile 'documentations.Makefile' in 'docs/'
        + Moved quotation marks from variable into targets/rules for environment variable setting

### 2024-05-18
#### 0742H
- Updates
    - Updated script 'treetraversal.py' in 'src/pyutils/scripts'
        + Modified JSON export: Each entry is to be an entry in a list instead of an individual key-value mapping for better JSON support and readability

#### 1558H
- Updates
    - Updated document 'scripts.md' in 'docs/'
        + Updated version of 'threadexec' to 'v0.1.1'
    - Updated script 'threadexec.py' in 'src/pyutils/scripts'
        + Relocated the user input request so that it doesnt collide with the initial input


