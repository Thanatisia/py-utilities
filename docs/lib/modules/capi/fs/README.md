# C programming API: Filesystem and disk management library

## Information

### Module
+ Type: Library/module

### Description
+ Library containing various core Android Project Generator-related objects to assist in the generating of a working, Out-of-the-Box (OOTB), Mobile (Android) Application Development Environment project and workspace
+ Library containing various C programming API functionalities related to Filesystems and disk management library

## Documentations

### Packages
- pyutils.libraries.capi

### Modules
- pyutils.libraries.capi
    - `.fs`

### Classes
- pyutils.libraries.capi.fs
    - `.Filesystem()` : Initializes the main filesystem C-API class
        - Return
            - fs : Return the initialized Filesystem() class object
                + Type: `class<Filesystem()>`

### Data Types/Objects

### Functions
- pyutils.libraries.capi.fs.Filesystem()
    - `.mount(self, source, target, fs, options='')`: Mount the specified source disk label to the target mount directory/point according to the specified filesystem type and the permission modifiers
        - Parameter Signature/Headers
            - source : Specify the source disk label to mount
                + Type: String

            - target : Specify the target mount point you wish to mount the disk label to
                + Type: String

            - fs : Specify the filesystem type of the disk you want to mount
                + Type: String

            - options : Specify other options you want to pass to the mounting process
                + Type: String

        - Usage
            - Mount an ext4 partition
                ```python
                .mount('disk-label', 'mount-point', 'ext4', 'rw')
                ```
            - Bind Mount
                ```python
                .mount('disk-label', 'mount-point', 'none', 'bind')
                ```

### Attributes/Variables
- pyutils.libraries.capi.fs.Filesystem()
    - `.libc` : Initialize glibc and C programming language
        + Type: ctypes.CDLL
    - `.libc.mount.argtypes` : Specify a tuple of mount argument types
        + Type: Tuple

### Usage
- Initialize class object
    ```python
    import os
    import sys
    from pyutils.libraries.capi.fs import Filesystem

    fs = Filesystem()
    ```
- Mount an ext4 partition
    ```python
    fs.mount('disk-label', 'mount-point', 'ext4', 'rw')
    ```

- Bind Mount
    ```python
    fs.mount('disk-label', 'mount-point', 'none', 'bind')
    ```

## Wiki

## Resources

## References
+ [Stackoverflow - Questions - 1667257 - How do I mount a filesystem using python](https://stackoverflow.com/questions/1667257/how-do-i-mount-a-filesystem-using-python)

## Remarks

