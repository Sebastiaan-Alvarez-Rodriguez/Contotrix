import os
import importlib

from lib.ui.menu import standard_yesno
from lib.ui.color import printc, Color
import lib.fs as fs

'''
This file contains a few utility functions
'''

# Returns True if a file with given extension is found in given directory, otherwise False
# If no directory is given, raises exception
def directory_has_extensions(directory, extension):
    with os.scandir(directory) as it:
        for entry in it:
            if entry.is_file() and entry.name.endswith(extension):
                return True


# Returns True if a module is available in this code execution, False otherwise
def has_module(name):
    return importlib.util.find_spec(name) != None


# Converts CSV to the more compact Apache Arrow
def convert_csv_to_pyarrow(location):
    if has_module('pyarrow'):
        from pyarrow import csv
        from pyarrow.parquet import write_table
        table = csv.read_csv(location)
        df = table.to_pandas()
        write_table(table, (location[:-4]+'.parquet'))
        printc('Conversion complete!', Color.GRN)
        if standard_yesno('Remove ".csv" file?'):
            fs.rm(location)
    else:
        raise RuntimeError('Module "pyarrow" unavailable. Cannot convert csv to pyarrow format"')