#!/usr/bin/env python
import importlib
import lib.fs as fs
import lib.util as util

from lib.ui.color import Color, printc, printerr
from lib.settings import settings
import lib.execute.execute as exe

def install(names):
    if len(names) == 0:
        printerr('No installer name provided')
        return
    modnames = names.split(' ')
    for name in modnames:
        installFile = fs.join(settings.idir,name,settings.ifile)
        if not fs.isfile(installFile):
            printerr('No installer for "{0}" available'.format(name))
            return

    for name in modnames:
        installLocation = fs.join(settings.wdir,name)
        if fs.isdir(installLocation):
            fs.rm(installLocation)

        fs.mkdir(installLocation)

        moduleLoc = settings.ifile[:-3] if settings.ifile.endswith('.py') else settings.ifile
        moduleLoc = fs.join(settings.idirname, name, moduleLoc).replace(fs.sep(), '.')
        module = importlib.import_module(moduleLoc)

        if module.install(installLocation, fs):
            printc('Installation of {0} successful!'.format(name), Color.GRN)
        else:
            printerr('Installation of {0} failed.'.format(name))


def remove(names):
    if len(names) == 0:
        printerr('No installer name provided')
        return
    modnames = names.split(' ')
    for name in modnames:
        if not fs.isdir(fs.join(settings.wdir,name)):
            printc('Success! (no such installed tool found)', Color.YEL)
            continue
        fs.rm(settings.wdir,name)
        printc('Success!', Color.GRN)


def execute(args):
    splitted = args.split(' ')
    if len(splitted) < 2:
        printerr('Need at least 2 arguments to execute: <repeats>, <name(s)>')
        return

    if not fs.isdir(settings.ddir):
        printerr('Directory "{0}" does not exist'.format(settings.ddir))
        return
    elif fs.isemptydir(settings.ddir) or not util.directory_has_extensions(settings.ddir, '.html'):
        printerr('Directory "{0}" does not contain .html files'.format(settings.ddir))
        return
    try:
        repeats = int(splitted[0])
    except Exception as e:
        printerr('Cannot convert "{0}" to number'.format(splitted[0]))
        return

    modnames = splitted[1:]

    for name in modnames:
        if not fs.isdir(fs.join(settings.wdir,name)):
            printerr('No tool named "{0}" installed'.format(name))
            return

    html_files_found = len([x for x in fs.ls(settings.ddir) if x.endswith('.html')])

    # Make tools a list of lists, like [[name, call]]
    tools = []
    for name in modnames:
        moduleLoc = settings.efile[:-3] if settings.efile.endswith('.py') else settings.efile
        moduleLoc = fs.join(settings.idirname, name, moduleLoc).replace(fs.sep(), '.')
        module = importlib.import_module(moduleLoc)

        execrule = module.execute(fs.join(settings.wdir,name), fs)
        tools.append([name, fs.join(settings.wdir,name), execrule])


    loglocation = '/tmp/loggo_sebastiaano.log'
    #TODO: Ask user for location


    printc('Starting execution for ', Color.CAN, end='')
    printc('{0} html files'.format(html_files_found), Color.PRP, end='')
    print(', ', end='')
    printc('{0} repeats'.format(repeats), Color.YEL)


    exe.execute(settings.ddir, repeats, tools, loglocation)
    printc('Execution successful!', Color.GRN)