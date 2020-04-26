import importlib

import lib.fs as fs
from lib.ui.menu import standard_yesno, ask_directory
from lib.ui.color import Color, printc, printerr
from lib.settings import settings
from lib.util import has_module

'''
Graphs submodule, responsible for all result generation
'''

if not has_module('vaex'):
    printerr('You need vaex in order to generate graphs\n\t(install with "pip3 install vaex --user")')
else:
    from lib.graphs.frame import Frame
    import lib.graphs.implementations.barplot as barplot
    import lib.graphs.implementations.memplot as memplot
    import lib.graphs.implementations.pagefaults as pagefaults
    import lib.graphs.implementations.sizetime as sizetime
    import lib.graphs.implementations.sizetimeunbound as sizetimeunbound
    import lib.graphs.implementations.timemem as timemem
    import lib.graphs.implementations.stats as stats


    def get_pqfiles(location):
        for x in fs.ls(location):
            if fs.isfile(location, x) and x.endswith('.parquet'):
                yield fs.join(location, x)

    def get_frames(location):
        for x in get_pqfiles(location):
            yield Frame(x)

    # Help function for this submodule
    def help():
        print('''
    Commands:
        h/help
            Show this info

        toggle show/large <optional: on/off>
            Toggles show/large value
             * "show" determines whether we show generated figures
             * "large" determines whether we create figures with larger font

        all
            Generates all graphs

        barplot [w(ell-formed)/i(ll-formed)]
            Generates barplot graph, containing general statistics
        memplot [w(ell-formed)/i(ll-formed)]
            Average max memory barplot
        pagefaults [w(ell-formed)/i(ll-formed)]
            Generates barplot graph, containing pagefault statistics
        size_time [w(ell-formed)/i(ll-formed)]
            Generates size vs time graph
        size_time_unbound [w(ell-formed)/i(ll-formed)]
            Generates size vs time graph for unbound runs
        stats
            Generates general statistics for the results
        time_mem [w(ell-formed)/i(ll-formed)]
            Generates time vs max memory usage graph
        back
            Returns to main menu
        exit/quit
            Exits program

    Good-to-know type info:
        1. ALL graphs are saved as vector image (.eps) in directory {0}
    '''.format(settings.godir))

    # Gets commands from commandline
    def get_command(print_large):
        try:
            printc('graphs (large)> ' if print_large else 'graphs> ', Color.YEL, end='')
            return input('').strip()
        except (KeyboardInterrupt, EOFError,) as e:
            print('\n')
            return 'q'


    def print_show(show):
        print('Set ', end='')
        printc('show ', Color.CAN, end='')
        print('to {0}'.format(show))

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

        print_large = False
        show_output = False


        command = get_command(print_large)

        if command == '':
            if not show_output:
                show_output = True
                print_large = True
            command = 'stats'
        while command.lower() not in ['b', 'back','q', 'quit', 'exit']:
            split = command.split(' ', 1)
            head, tail = (split[0], split[1],) if len(split) == 2 else (split[0], '',)
            head = head.lower()
            if head in ['h', 'help']:
                help()
            elif head == 'toggle':
                subsplit = tail.split(' ', 1)
                if subsplit[0] in ['s', 'show']:
                    if len(subsplit) > 2:
                        show_output = subsplit[1] == 'on'
                    else:
                        show_output = not show_output
                    print_show(show_output)

                elif subsplit[0] in ['l', 'large']:
                    if len(subsplit) >= 2:
                        print_large = subsplit[1] == 'on'
                    else:
                        print_large = not print_large
                else:
                    printerr('Please specify what to toggle: "show" or "large"')
            elif head in ['s', 'show']:
                subsplit = tail.split(' ', 1)
                if len(subsplit) >= 2:
                    show_output = subsplit[1] == 'on'
                else:
                    show_output = not show_output
                print_show(show_output)
            elif head == 'all':
                for x in [True,False]:
                    barplot.gen(frames, x, print_large=print_large, show_output=show_output)
                    pagefaults.gen(x, print_large=print_large, show_output=show_output)
                    sizetime.gen(frames, x, print_large=print_large, show_output=show_output)
                    sizetimeunbound.gen(frames, x, print_large=print_large, show_output=show_output)
                    timemem.gen(frames, x, print_large=print_large, show_output=show_output)
            elif head == 'barplot':
                barplot.gen(frames, tail in ['w', 'wellformed', 'well-formed'], print_large=print_large, show_output=show_output)
            elif head == 'memplot':
                memplot.gen(frames, tail in ['w', 'wellformed', 'well-formed'], print_large=print_large, show_output=show_output)
            elif head == 'pagefaults':
                pagefaults.gen(frames, tail in ['w', 'wellformed', 'well-formed'], print_large=print_large, show_output=show_output)
            elif head in ['size_time', 'sizetime', 'size time']:
                sizetime.gen(frames, tail in ['w', 'wellformed', 'well-formed'], print_large=print_large, show_output=show_output)
            elif head in ['size_time_unbound', 'sizetimeunbound', 'size time unbound']:
                sizetimeunbound.gen(frames, tail in ['w', 'wellformed', 'well-formed'], print_large=print_large, show_output=show_output)
            elif head in ['stat', 'stats']:
                stats.gen(frames)
            elif head in ['time_mem', 'timemem', 'time mem']:
                timemem.gen(frames, tail in ['w', 'wellformed', 'well-formed'], print_large=print_large, show_output=show_output)
            else:
                print('Command "{0}" not recognized'.format(head))
            command = get_command(print_large)
        return command in ['q', 'quit', 'exit']