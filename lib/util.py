#!/usr/bin/env python
import os

# Returns True if a file with given extension is found in given directory, otherwise False
# If no directory is given, raises exception
def directory_has_extensions(directory, extension):
    for file in os.listdir(directory):
        if file.endswith(extension):
            return True
    return False