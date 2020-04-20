import sys
import os

def ask_java_path(fs):
    while True:
        ans = input('What is your path to java?\n')
        if len(ans) == 0:
            print('Please provide an input')
        elif not fs.isfile(fs.abspath(ans)):
            print('No such file "{0}"'.format(fs.abspath(ans)))
        else:
            return fs.abspath(ans)

def execute(location, fs):
    env = os.environ.copy()
    if 'JAVA_HOME' in env:
        java_home = env['JAVA_HOME']
    else:
        java_home = ask_java_path(fs)
    return [java_home, '-jar {0}'.format(fs.join(location, 'hpar.jar'))]