#!/usr/bin/env python
import sys

# Checks python version and exits if it is too low
# Must be specified before any lib imports (using v3.5) are done
if sys.version_info < (3,5):
    print('I am sorry, but this script is for python3.5+ only!')
    exit(1)

import lib.fs as fs
import lib.tools as tools
from lib.ui.color import printc, Color
import lib.download.crawl.crawl as crawl
import lib.download.commoncrawl.crawl as commoncrawl
import lib.graphs.graphs as graphs

def help():
    print('''
Commands:
    h(elp)
        Show this info

    install <name(s)>
        Installs tool to use

    remove/deinstall/de-install <name(s)>

    execute <repeats> <name(s)>
        Executes test on all given names of tools

    crawl <begin url> <amount>
        Crawls the web, starting at <url>, for <amount> urls (or until no suitable urls remain)

    commoncrawl <amount> <year> <magicnumber>
        Downloads <amount> collected pages from the commoncrawl collective for the given <year> and <magicnumber>
        <magicnumber> is the number found in the list at https://commoncrawl.org/the-data/get-started/,
        in the main list, as s3://commoncrawl/crawl-data/CC-MAIN-<year>-<magicnumber>.

    malform(er) <optional: command>
        Construct malformed html from existing html in the data directory

    graph(s) <optional: path>
        Starts graph submodule. If path is given, loads in parquet files from given path

    exit/quit
        Stops this program
''')


def get_command():
    try:
        printc('prompt> ', Color.BLU, end='')
        return input('').strip()
    except (KeyboardInterrupt, EOFError,) as e:
        print('\n')
        return 'q'


# Main function of this framework. Prints current installation state and
# allows user to install, execute and reconfigure, dependening on this state
def main():
    command = get_command()
    while command.lower() not in ['q', 'quit', 'exit']:
        split = command.split(' ', 1)
        head, tail = (split[0], split[1],) if len(split) == 2 else (split[0], '',)
        head = head.lower()
        if head in ['h', 'help']:
            help()
        elif head == 'install':
            tools.install(tail)
        elif head in ['remove', 'deinstall', 'de-install']:
            tools.remove(tail)
        elif head in ['exec', 'execute']:
            tools.execute(tail)
        elif head == 'crawl':
            crawl.crawl(tail)
        elif head == 'commoncrawl':
            commoncrawl.crawl(tail)
        elif head in ['graph', 'graphs']:
            if graphs.submenu(path=tail if tail != '' else None):
                return
        else:
            print('Command "{0}" not recognized'.format(head))
        command = get_command()


if __name__ == '__main__':
    main()