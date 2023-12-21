# My All-in-One library/package/framework collection for Python

## Information

### Background Summary
- An all-in-one package containing a collection of self-implemented Python packages/frameworks/libraries (the following will collectively be known as 'library') such that
    + you can add this into a project as a submodule and you can import the libraries directly

### Features
- Follows "Best Practice" python framework project structure (to the best of my ability)
    - Easy to modify

## Setup
### Dependencies
+ python3
+ pip

### Pre-Requisites

### Embedding library in your own project
- Change directory into your project root containing the git folder
    ```console
    cd [project-root]
    ```

- Importing as a git submodule
    ```console
    git submodule add https://github.com/Thanatisia/python-pkgs
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
        - packages/
            - frameworks/ : Place all frameworks and multi-library files here
            - libraries/  : Place all standalone libraries/modules and classes here

## Resources

## References

## Remarks
