"""
Unit Test: Ctypes and mounting disk filesystems
"""
import os
import sys
from pyutils.libraries.capi.fs import Filesystem

def init():
    global fs
    fs = Filesystem()

def main():
    # Perform pre-initialization setup
    init()

    # Mount the filesystems
    fs.mount('/dev/sdb2', '/mnt', 'ext4', 'rw')
    fs.mount('/dev/sdb1', '/mnt/boot', 'ext4', 'rw')
    fs.mount('/dev/sdb3', '/mnt/home', 'ext4', 'rw')

if __name__ == "__main__":
    main()

