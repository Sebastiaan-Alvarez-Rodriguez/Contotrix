#!/usr/bin/env python
import sys
import os

import lxml.html

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
        root = lxml.html.fromstring(contentbytes)
    root = lxml.html.fromstring(contentbytes)
    urls = root.xpath('//a/@href')
    print(str(len(urls)))

if __name__ == '__main__':
    main()