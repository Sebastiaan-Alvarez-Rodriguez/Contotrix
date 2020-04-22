#!/usr/bin/env python
import sys

import lib.fs as fs
from lib.ui.menu import standard_yesno, ask_directory
from lib.ui.color import Color, printc, printerr
from lib.settings import settings

from lib.graphs.csv.csv import CSV
import lib.graphs.implementations.barplot as barplot


def get_csvfiles(location):
    for x in fs.ls(location):
        if fs.isfile(location, x) and x.endswith('.csv'):
            yield fs.join(location, x)

def get_csvs():
    for x in get_csvfiles(ask_directory('Where to get CSV files from?', must_exist=True)):
        yield CSV(x)

def help():
    print('''
Commands:
    h/help
        Show this info

    all
        Generates all graphs
    barplot [b(enign)/w(rong)]
        Generates barplot graph, containing correct,incorrect,timeout,error bars
    size_time
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
def submenu():
    printc('WARNING: ', Color.PRP, end='In this part, we read all data from all CSV files\n')
    print('\tThis may cost you a lot of memory, dependening on amount of results.\n')

    csvs = list(get_csvs())
    if len(csvs) == 0:
        printerr('Found no sources (files with extension ".csv")')
        return
    print('Found {0} sources'.format(len(csvs)))

    csvs.sort()

    command = get_command()
    while command.lower() not in ['b', 'back','q', 'quit', 'exit']:
        split = command.split(' ', 1)
        head, tail = (split[0], split[1],) if len(split) == 2 else (split[0], '',)
        head = head.lower()
        if head in ['h', 'help']:
            help()
        # elif head == 'all':
        #     impl.generate_all(csvs)
        elif head == 'barplot':
            barplot.gen(csvs, tail in ['b', 'benign'])
        # elif head in ['size_time', 'sizetime', 'size time']:
        #     impl.generate_sizetime(csvs)
        else:
            print('Command "{0}" not recognized'.format(head))
        command = get_command()
    return command in ['q', 'quit', 'exit']
