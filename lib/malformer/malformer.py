
import lib.fs as fs
from lib.ui.menu import standard_yesno, ask_directory
from lib.ui.color import Color, printc, printerr
from lib.settings import settings

import lib.malformer.minor as minor
import lib.malformer.major as major


def help():
    print('''
Commands:
    h/help
        Show this info

    all
        Generates all graphs
    minor <amount>
        Generates <amount> html pages with minor faults: 
            * Removes <!DOCTYPE html>
            * Strips image src or alt attribute for each img tag
    major <amount>
        Generates <amount> html pages with major faults:
            * Removes <head>'s
            * Removes closing </html> tag
            * Places tags without matching closing tags in body
            * Places closing tags without matching opening tags in body
    back
        Returns to main menu
    exit/quit
        Exits program
''')


def get_command():
    try:
        printc('malformer> ', Color.PRP, end='')
        return input('').strip()
    except (KeyboardInterrupt, EOFError,) as e:
        print('\n')
        return 'q'


# Main function of this submodule
# Returns True if program should be exited, otherwise False
def submenu(command=None):
    if command == None:
        command = get_command()

    while command.lower() not in ['b', 'back', 'q', 'quit', 'exit']:
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
        elif head == 'minor':
            minor.gen(tail)
        elif head == 'major':
            major.gen(tail)
        else:
            print('Command "{0}" not recognized'.format(head))
        command = get_command()
    return command in ['q', 'quit', 'exit']