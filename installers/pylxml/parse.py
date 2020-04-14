#!/usr/bin/env python
import sys
import os

import lxml.html

def main():
    if len(sys.argv) < 2:
        print('Usage: {0} <repeats>'.format(sys.argv[0]))
        return 1

    try:
        repeats = int(sys.argv[1])
    except Exception as e:
        print('Could not convert "{0}" to number'.format(sys.argv[1]))
        return 2

    sys.stdin.read(4)
    content = sys.stdin.read()

    for x in range(repeats-1):
        root = lxml.html.fromstring(content)
    root = lxml.html.fromstring(content)
    urls = root.xpath('//a/@href')
    print(str(len(urls)))

if __name__ == '__main__':
    main()