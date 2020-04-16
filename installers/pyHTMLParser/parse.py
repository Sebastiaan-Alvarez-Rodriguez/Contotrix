#!/usr/bin/env python
import sys
import os

from html.parser import HTMLParser

class LinkParser(HTMLParser):
    def __init__(self):
        self.counter = 0
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'a' and 'href' in [x for x,_ in attrs]:
            self.counter += 1


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
        parser = HTMLParser()
        parser.feed(content)

    parser = LinkParser()
    parser.feed(content)
    print(str(parser.counter))

if __name__ == '__main__':
    main()