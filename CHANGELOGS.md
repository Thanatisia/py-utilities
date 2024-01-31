# CHANGELOGS

## Table of Contents
+ [2023-12-21](#2023-12-21)
+ [2024-01-05](#2024-01-05)
+ [2024-01-30](#2024-01-30)
+ [2024-01-31](#2024-01-31)

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

