#!/usr/bin/env python
import sys

from bs4 import BeautifulSoup

def main():
    if len(sys.argv) != 3:
        print('Usage: {0} <htmlsize> <repeats>'.format(sys.argv[0]))
        return 1

    try:
        htmlsize = int(sys.argv[1])
        repeats = int(sys.argv[2])
    except Exception as e:
        print('Could not convert "{0}" or "{1}" to number'.format(sys.argv[1], sys.argv[2]))
        return 2

    with open(0, 'rb') as f:
        contentbytes = f.read(htmlsize)

    for x in range(repeats-1):
        parsed = BeautifulSoup(contentbytes, features='html.parser')
    parsed = BeautifulSoup(contentbytes, features='html.parser')
    print(str(len([x for x in parsed.find_all('a', href=True)])))

if __name__ == '__main__':
    main()