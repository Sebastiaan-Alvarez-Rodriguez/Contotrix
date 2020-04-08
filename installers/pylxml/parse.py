#!/usr/bin/env python
import sys
import os

import lxml.html

def main():
    if len(sys.argv) < 3:
        print('Usage: {0} <data> <repeats>'.format(sys.argv[0]))
        return 1
    data = sys.argv[1]
    try:
        repeats = int(sys.argv[2])
    except Exception as e:
        print('Could not convert "{0}" to number'.format(sys.argv[2]))
        return 2

    for item in os.listdir(data):
        path = data+os.sep+item
        with open(path, 'r') as file:
            contents = file.read()
        for x in range(repeats):
            root = lxml.html.fromstring(contents)

if __name__ == '__main__':
    main()