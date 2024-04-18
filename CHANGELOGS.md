# CHANGELOGS

## Table of Contents
+ [2023-12-21](#2023-12-21)
+ [2024-01-05](#2024-01-05)
+ [2024-01-30 - v0.1.0](#2024-01-30)
+ [2024-01-31](#2024-01-31)
+ [2024-03-25](#2024-03-25)
+ [2024-04-18](#2024-04-18)

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

