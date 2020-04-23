#!/usr/bin/env python
import sys

import lib.fs as fs
from lib.ui.menu import standard_yesno, ask_directory
from lib.ui.color import Color, printc, printerr
from lib.settings import settings

from lib.graphs.frame import Frame
import lib.graphs.implementations.barplot as barplot
import lib.graphs.implementations.sizetime as sizetime


def get_pqfiles(location):
    for x in fs.ls(location):
        if fs.isfile(location, x) and x.endswith('.parquet'):
            yield fs.join(location, x)

def get_frames(location):
    for x in get_pqfiles(location):
        yield Frame(x)

def help():
    print('''
Commands:
    h/help
        Show this info

    all
        Generates all graphs
    barplot [w(ell-formed)/i(ll-formed)]
        Generates barplot graph, containing general statistics
    size_time [w(ell-formed)/i(ll-formed)]
        Generates size vs time graph

    back/exit/quit
        Returns to main menu
''')

def get_command():
    try:
        printc('graphs> ', Color.YEL, end='')
        return input('').strip()
    except (KeyboardInterrupt, EOFError,) as e:
        print('\n')
        return 'q'

# Main function of this submodule
# Returns True if program should be exited, otherwise False
def submenu(path=None):
    if path == None or not fs.isdir(path):
        if not fs.isdir(path):
            printerr('Optional argument "path" does not provide a valid directory')
        path = ask_directory('Where to get parquet files from?', must_exist=True)

    frames = list(get_frames(path))
    if len(frames) == 0:
        printerr('Found no sources (files with extension ".parquet")')
        return
    print('Found {0} sources'.format(len(frames)))

    frames.sort()

    command = get_command()
    if command == '':
        command = 'sizetime w'
    while command.lower() not in ['b', 'back','q', 'quit', 'exit']:
        split = command.split(' ', 1)
        head, tail = (split[0], split[1],) if len(split) == 2 else (split[0], '',)
        head = head.lower()
        if head in ['h', 'help']:
            help()
        # elif head == 'all':
        #     impl.generate_all(csvs)
        elif head == 'barplot':
            barplot.gen(frames, tail in ['w', 'wellformed', 'well-formed'])
        elif head in ['size_time', 'sizetime', 'size time']:
            sizetime.gen(frames, tail in ['w', 'wellformed', 'well-formed'])
        else:
            print('Command "{0}" not recognized'.format(head))
        command = get_command()
    return command in ['q', 'quit', 'exit']
 # TODO use vaex? (only for large plots?)
 # https://vaex.readthedocs.io/en/latest/examples.html
 # TODO think of nice plot