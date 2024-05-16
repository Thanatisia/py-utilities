# git-mass-update

## Information
### Description
+ A Git helper utility for going through every git repositories and updating/pulling changes for the currently-attached branch

### Notes
+ Currently git-mass-update only supports static parameter specifications (positional-only), however, Optional argument customizations in the form of flags are in the TODO pipeline

## Setup
### Dependencies

### Pre-Requisites

## Documentations

### Synopsis/Syntax
```bash
git-mass-update {options} <arguments>
```

### Parameters
- Positional
    - top_level_root_dir : Specify the top level root directory you wish to start the walking from
        + Type: String
        + Default: '.' (Current working directory)

- Optionals
    - With Arguments
    - Flags

### Usage
- Go through every git repositories and updating/pulling changes for the currently-attached branch
    ```bash
    git-mass-update [path]
    ```

## TODO
+ Optional argument customizations in the form of flags

## Resources

## References

## Remarks
