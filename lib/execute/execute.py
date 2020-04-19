import subprocess
import multiprocessing
import time
import os
import sys

from lib.ui.color import printc, Color, printerr
import lib.fs as fs
from lib.execute.logger import Logger

def print_success(tool_name, html_name):
    print('Execution of ', end='')
    printc('{0} '.format(tool_name), Color.CAN, end='')
    print('on {0} '.format(html_name), end='')
    printc('complete!', Color.GRN)

def print_failure(tool_name, html_name):
    print('Execution of ', end='')
    printc('{0} '.format(tool_name), Color.CAN, end='')
    print('on {0} '.format(html_name), end='')
    printc('failed!', Color.RED)

# Function which handles the running of one parser call
# Tasks should be an iterable of lists of form ([parser, htmlfilename, htmldata, repeats], ...)
def parallel_execute(tool_name, tool_cwd, tool_execrule, html_name, html_content_path, repeats, logqueue, doprint=False):
    with open(html_content_path, 'rb') as file:
        html_content = file.read()
    html_size = len(html_content)

    if doprint:
        print('Starting execution of ', end='')
        printc('{0} '.format(tool_name), Color.CAN, end='')
        print('on ', end='')
        printc('{0} '.format(html_name), Color.YEL, end='(size={0})\n'.format(html_size))
    start = time.time()
    err = False
    try:
        output = subprocess.check_output([sys.executable, 'statexec.py', ' '.join(tool_execrule), str(html_size), str(repeats), str(tool_cwd)], env=os.environ.copy(), cwd=fs.abspathfile(__file__), input=html_content)
    except Exception as e:
        err = True
    end = time.time()

    if err:
        if doprint:
            print_failure(tool_name, html_name)
        links_found = 0
        ru_utime,ru_stime,ru_maxrss,ru_minflt,ru_majflt = [0,0,0,0,0]
        errmsg = str(err).replace(',', '|')
    else:
        if doprint:
            print_success(tool_name, html_name)
        splitted = output.decode('utf-8').strip().split(',')
        links_found = int(splitted[0])
        ru_utime,ru_stime,ru_maxrss,ru_minflt,ru_majflt = splitted[1:]
    total_time = end - start

    logqueue.put('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}'.format(
        tool_name,
        html_name,
        html_size,
        total_time,
        links_found,
        ru_utime,
        ru_stime,
        ru_maxrss,
        ru_minflt,
        ru_majflt,
        err
    ))


# Ask how many cores to use for execution
def ask_cores(max_cores=None):
    if max_cores != None:
        show_max = min(max_cores, multiprocessing.cpu_count())
    else:
        show_max = None
    while True:
        print('You have {0} cores.'.format(multiprocessing.cpu_count()))
        if show_max != None:
            answer = input('How many cores to use for processing? (max={0}) '.format(show_max))
        else:
            answer = input('How many cores to use for processing? ')
        try:
            amount = int(answer)
        except Exception as e:
            printerr('Could not convert "{0}" to a number'.format(answer))
            continue

        if amount < 1:
            printerr('Need at least 1 core')
            continue
        if amount > multiprocessing.cpu_count():
            printerr('You do not have {0} cores'.format(amount))
            continue
        if show_max != None and int(amount) > show_max:
            printerr('Please do not specify more than {0} cores'.format(show_max))
            continue
        return amount


def argument_generator(data, repeats, tools, logqueue):
    for item in [x for x in fs.ls(data) if x.endswith('.html')]:
        for tool in tools:
            yield (tool[0], tool[1], tool[2], item, fs.join(data, item), repeats, logqueue,)


# Data, repeats, [[name, location, execrule], ...], csvlocation
def execute(data, repeats, tools, csvlocation):
    cores = ask_cores()
    logger = Logger(csvlocation)
    args = [x for x in argument_generator(data, repeats, tools, logger.logqueue)]
    logger.start()
    with multiprocessing.Pool(processes=cores) as pool:
        pool.starmap(parallel_execute, args)
    logger.stop()