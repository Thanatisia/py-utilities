"""
C programming API: Filesystem and disk management library
"""
import os
import sys
import ctypes
import ctypes.util

class Filesystem():
    """
    Filesystem and Disk management functions
    """
    def __init__(self):
        # Initialize glibc and C programming language
        self.libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

        # Specify a tuple of mount argument types
        self.libc.mount.argtypes = (ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_ulong, ctypes.c_char_p)

    def mount(self, source, target, fs, options=''):
        """
        Mount the specified source disk label to the target mount directory/point according to the specified filesystem type and the permission modifiers

        :: Parameter Signature/Headers
        - source : Specify the source disk label to mount
            + Type: String

        - target : Specify the target mount point you wish to mount the disk label to
            + Type: String

        - fs : Specify the filesystem type of the disk you want to mount
            + Type: String

        - options : Specify other options you want to pass to the mounting process
            + Type: String

        :: Usage
        - Mount an ext4 partition
            .mount('disk-label', 'mount-point', 'ext4', 'rw')
        - Bind Mount
            .mount('disk-label', 'mount-point', 'none', 'bind')
        """
        ret = self.libc.mount(source.encode(), target.encode(), fs.encode(), 0, options.encode())
        if ret < 0:
            errno = ctypes.get_errno()
            raise OSError(errno, f"Error mounting {source} ({fs}) on {target} with options '{options}': {os.strerror(errno)}")


