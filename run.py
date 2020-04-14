#!/usr/bin/env python
import sys

# Checks python version and exits if it is too low
# Must be specified before any lib imports (using v3.3) are done
if sys.version_info < (3,3):
    print('I am sorry, but this script is for python3.3+ only!')
    exit(1)

import lib.fs as fs
import lib.tools as tools


def help():
    print('''
Commands:
    help
        Show this info
    
    install <name(s)>
        Installs tool to use

    remove/deinstall/de-install <name(s)>
    
    execute <repeats> <name(s)>
        Executes test on all given names of tools
    
    download <begin url> <amount>
        Crawls the web, starting at <url>, for <amount> urls (or until no suitable urls remain)

    exit/quit
        Stops this program
''')


def get_command():
    try:
        return input("prompt> ").strip()
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
        if head == 'help':
            help()
        elif head == 'install':
            tools.install(tail)
        elif head in ['remove', 'deinstall', 'de-install']:
            tools.remove(tail)
        elif head in ['exec', 'execute']:
            tools.execute(tail)
        elif head in ['dl', 'download']:
            tools.download(tail)
        else:
            print('Command "{0}" not recognized'.format(head))
        command = get_command()


if __name__ == '__main__':
    main()