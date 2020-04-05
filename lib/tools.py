#!/usr/bin/env python
import lib.fs as fs

from lib.settings import settings

def install(name):
    if len(name) == 0:
        print('No installer name provided')
        return
    if not fs.isfile(fs.join(settings.idir,name,settings.ifile)):
        print('No installer for "{0}" available'.format(name))
        return

    fs.mkdir(fs.join(settings.wdir,name), exist_ok=True)
    
    print('Installation success!')


def remove(name):
    if len(name) == 0:
        print('No installer name provided')
        return
    if not fs.isdir(fs.join(settings.wdir,name)):
        print('Success! (no installed tool found)')
        return
    fs.rm(settings.wdir,name)
    print('Success!')