#!/usr/bin/env python
import importlib
import lib.fs as fs

from lib.settings import settings

def install(name):
    if len(name) == 0:
        print('No installer name provided')
        return
    installFile = fs.join(settings.idir,name,settings.ifile)
    if not fs.isfile(installFile):
        print('No installer for "{0}" available'.format(name))
        return

    installLocation = fs.join(settings.wdir,name)
    if fs.isdir(installLocation):
        fs.rm(installLocation)

    fs.mkdir(installLocation)

    moduleLoc = settings.ifile[:-3] if settings.ifile.endswith('.py') else settings.ifile
    moduleLoc = fs.join(settings.idirname,name, moduleLoc).replace(fs.sep(), '.')
    module = importlib.import_module(moduleLoc)

    if module.install(installLocation, fs):
        print('Installation success!')
    else:
        print('Installation failure.')


def remove(name):
    if len(name) == 0:
        print('No installer name provided')
        return
    if not fs.isdir(fs.join(settings.wdir,name)):
        print('Success! (no such installed tool found)')
        return
    fs.rm(settings.wdir,name)
    print('Success!')