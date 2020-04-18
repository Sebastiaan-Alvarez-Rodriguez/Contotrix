#!/usr/bin/env python
import os

# Returns True if a file with given extension is found in given directory, otherwise False
# If no directory is given, raises exception
def directory_has_extensions(directory, extension):
    with os.scandir(directory) as it:
        for entry in it:
            if entry.is_file() and entry.name.endswith(extension):
                return True