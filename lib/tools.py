#!/usr/bin/env python
import importlib
import subprocess

import lib.fs as fs
import lib.util as util
import lib.xml as xml

from lib.ui.color import Color, printc, printerr
from lib.settings import settings
from lib.ui.menu import ask_path, standard_yesno
import lib.execute.execute as exe

def install(names):
    if len(names) == 0:
        printerr('No installer name provided')
        return
    modnames = names.split(' ')
    for name in modnames:
        if not fs.isfile(fs.join(settings.idir,name,settings.ifile)):
            printerr('No installer for "{0}" available'.format(name))
            return
        if not fs.isfile(fs.join(settings.idir,name,settings.cfile)):
            printerr('No config file available')
            return

        xmlconf = xml.Config(fs.join(settings.idirname, name, settings.cfile))
        deps = xmlconf.get_dependencies()
        if len(deps) > 0:
            maxnamelen = max([len(x[0]) for x in deps])
            print('You need to have the following installed for ', end='')
            printc('{0}'.format(name), Color.CAN, end=':\n')
            printc('{0:20}  {1}'.format('Name', 'minimum'), Color.GRN)
            for name, minimum in deps:
                print('{0:20}  {1}'.format(name, minimum))
        else:
            print('No dependencies found for {0}'.format(name))
        if not standard_yesno('Continue?'):
            printerr('Installation cancelled')
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
        if not fs.isfile(fs.join(settings.idir,name,settings.efile)):
            print('Filepath was: {0}'.format(fs.join(settings.wdir,name,settings.efile)))
            printerr('Tool "{0}" has no {1} to run it'.format(name, settings.efile))
            return

    html_files_found = len([x for x in fs.ls(settings.ddir) if x.endswith('.html')])

    tools = []
    for name in modnames:
        moduleLoc = settings.efile[:-3] if settings.efile.endswith('.py') else settings.efile
        moduleLoc = fs.join(settings.idirname, name, moduleLoc).replace(fs.sep(), '.')
        module = importlib.import_module(moduleLoc)

        execrule = module.execute(fs.join(settings.wdir,name), fs)
        tools.append([name, fs.join(settings.wdir,name), execrule])


    csvloc = ask_path('We need a path to store CSV output.', exist_ok=False)
    if fs.isfile(csvloc):
        fs.rm(csvloc)

    print('Starting execution for ', end='')
    printc('{0} '.format(html_files_found), Color.CAN, end='')
    print('html files, ', end='')
    printc('{0} '.format(repeats), Color.GRN, end='')
    print('repeats')


    exe.execute(settings.ddir, repeats, tools, csvloc)
    printc('Execution successful!', Color.GRN)