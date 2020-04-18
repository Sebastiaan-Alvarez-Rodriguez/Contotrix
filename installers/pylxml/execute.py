import sys

def execute(location, fs):
    return [sys.executable, fs.join(location, 'parse.py')]