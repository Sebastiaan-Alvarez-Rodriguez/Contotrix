#!/usr/bin/env python
import sys
import lib.fs as fs

# The purpose of this file is to set some global variables that are used at many places

class Settings(object):    
    def __init__(self):
        super(Settings, self).__init__()
        self.root = fs.abspath(fs.dirname(sys.argv[0]))
        self.idir = fs.join(self.root,'installers')
        self.ifile = 'install.py'
        self.wdir = fs.join(self.root,'installed')

global settings
settings = Settings()