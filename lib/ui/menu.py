
from enum import Enum
from lib.ui.color import printerr
import lib.fs as fs

'''
This file provides functions to handle standard user-interaction
'''

# Simple method to ask user a yes/no question. Result returned as boolean.
# Returns True if user responded positive, otherwise False
def standard_yesno(question):
    while True:
        choice = input(question+' [Y/n] ').lower()
        if choice in ('y', 'yes'):
            return True
        elif choice in ('n', 'no'):
            return False
        else:
            printerr('Invalid option "{0}"'.format(choice))


# ask user for a directory
# must_exist determines whether given dir explicitly must or must not exist
def ask_directory(question, must_exist=True):
    while True:
        print(question)
        print('Paths may be absolute or relative to your working directory')
        print('Working directory: {0}'.format(fs.cwd()))
        print('Please specify a directory:')
        choice = input('')
        choice = fs.abspath(choice)
        if must_exist:
            if not fs.isdir(choice):
                printerr('No such directory - "{0}"'.format(choice))
            else:
                return choice
        else:
            if fs.isdir(choice):
                print('"{0}" already exists'.format(choice))
                if standard_yesno('continue?'):
                    return choice
            else:
                return choice
        print('')


# ask user for a path (directory+file)
def ask_path(question, must_exist=False, exist_ok=True, ask_override=True, directory=None, extension=None):
    while True:
        print(question)
        print('Paths may be absolute or relative to your working directory')
        print('Working directory: {0}'.format(fs.cwd()))
        print('Please specify a path:')
        choice = input('')
        choice = fs.abspath(choice)
        if not fs.isdir(fs.dirname(choice)):
            printerr('No such directory "{0}"'.format(fs.dirname(choice)))
        elif must_exist: #must exist
            if fs.isfile(choice):
                return choice
            else:
                printerr('"{0}" is not a file'.format(choice))
        elif (not must_exist) and exist_ok: #may exist, not has to exist
            if ask_override and standard_yesno('"{0}" exists, override?'.format(choice)):
                return choice
        elif (not must_exist) and (not exist_ok): #must not exist
            if fs.isfile(choice):
                printerr('"{0}" already exists'.format(choice))
            else:
                return choice
        print('')