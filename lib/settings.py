import sys
import lib.fs as fs

'''
The purpose of this file is to set some global variables that are used at many places
'''

class Settings(object):    
    def __init__(self):
        super(Settings, self).__init__()
        self.root = fs.abspath(fs.dirname(sys.argv[0]))

        self.idirname = 'installers'
        self.idir = fs.join(self.root, self.idirname)
        self.ifile = 'install.py'
        self.cfile = 'config.xml'
        self.efile = 'execute.py'
        self.wdir = fs.join(self.root,'installed')
        self.ddir = fs.join(self.root,'data')
        self.mdir = fs.join(self.ddir,'malformed')
        self.godirname = 'graph_outputs'
        self.godir = fs.join(self.root, self.godirname)
global settings
settings = Settings()