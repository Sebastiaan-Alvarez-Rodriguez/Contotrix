#!/usr/bin/env python
import lib.fs as fs
from lib.ui.menu import standard_yesno, ask_directory
from lib.ui.color import Color, printc, printerr
from lib.settings import settings

from lib.graphs.frame import Frame
import lib.graphs.implementations.barplot as barplot
import lib.graphs.implementations.pagefaults as pagefaults
import lib.graphs.implementations.sizetime as sizetime
import lib.graphs.implementations.sizetimeunbound as sizetimeunbound
import lib.graphs.implementations.timemem as timemem


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
    pagefaults [w(ell-formed)/i(ll-formed)]
        Generates barplot graph, containing pagefault statistics
    size_time [w(ell-formed)/i(ll-formed)]
        Generates size vs time graph
    size_time_unbound [w(ell-formed)/i(ll-formed)]
        Generates size vs time graph for unbound runs
    time_mem [w(ell-formed)/i(ll-formed)]
        Generates time vs max memory usage graph
    back
        Returns to main menu
    exit/quit
        Exits program
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
        if path != None:
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
        command = 'pagefaults w'
    while command.lower() not in ['b', 'back','q', 'quit', 'exit']:
        split = command.split(' ', 1)
        head, tail = (split[0], split[1],) if len(split) == 2 else (split[0], '',)
        head = head.lower()
        if head in ['h', 'help']:
            help()
        elif head == 'all':
            for x in [True,False]:
                barplot.gen(frames, x)
                pagefaults.gen(x)
                sizetime.gen(frames, x)
                sizetimeunbound.gen(frames, x)
                timemem.gen(frames, x)
        elif head == 'barplot':
            barplot.gen(frames, tail in ['w', 'wellformed', 'well-formed'])
        elif head == 'pagefaults':
            pagefaults.gen(frames, tail in ['w', 'wellformed', 'well-formed'])
        elif head in ['size_time', 'sizetime', 'size time']:
            sizetime.gen(frames, tail in ['w', 'wellformed', 'well-formed'])
        elif head in ['size_time_unbound', 'sizetimeunbound', 'size time unbound']:
            sizetimeunbound.gen(frames, tail in ['w', 'wellformed', 'well-formed'])
        elif head in ['time_mem', 'timemem', 'time mem']:
            timemem.gen(frames, tail in ['w', 'wellformed', 'well-formed'])
        else:
            print('Command "{0}" not recognized'.format(head))
        command = get_command()
    return command in ['q', 'quit', 'exit']