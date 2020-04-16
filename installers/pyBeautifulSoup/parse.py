#!/usr/bin/env python
import sys

from bs4 import BeautifulSoup

def main():
    if len(sys.argv) != 2:
        print('Usage: {0} <repeats>'.format(sys.argv[0]))
        return 1

    try:
        repeats = int(sys.argv[1])
    except Exception as e:
        print('Could not convert "{0}" to number'.format(sys.argv[1]))
        return 2

    with open(0, 'rb') as f:
        f.read(4)
        contentbytes = f.read()
    content = contentbytes.decode('utf-8')

    for x in range(repeats-1):
        parsed = BeautifulSoup(content, features='html.parser')
    parsed = BeautifulSoup(content, features='html.parser')
    print(str(len([x for x in parsed.find_all('a', href=True)])))

if __name__ == '__main__':
    main()