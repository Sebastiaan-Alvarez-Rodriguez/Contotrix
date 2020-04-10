import subprocess
import multiprocessing
import time
import os

from lib.ui.color import printerr
import lib.fs as fs
from lib.execute.logger import Logger

# Function which handles the running of one parser call
# Tasks should be an iterable of lists of form ([parser, htmlfilename, htmldata, repeats], ...)
def parallel_execute(tool_name, tool_cwd, tool_execrule, html_name, html_content, repeats, logqueue):
    html_size = len(html_content)
    cmd_input = html_size.to_bytes(4, byteorder='little', signed=False)
    cmd_input += html_content
    start = time.time()
    output = subprocess.check_output(['/usr/bin/python3', 'statexec.py', ' '.join(tool_execrule), str(repeats), str(tool_cwd)], cwd=fs.abspathfile(__file__), input=cmd_input)
    end = time.time()

    splitted = output.decode('utf-8').strip().split(',')
    links_found = int(splitted[0])
    ru_utime,ru_stime,ru_maxrss,ru_minflt,ru_majflt = splitted[1:]

    total_time = end - start

    logqueue.put('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}'.format(
        tool_name,
        html_name,
        html_size,
        total_time,
        links_found,
        ru_utime,
        ru_stime,
        ru_maxrss,
        ru_minflt,
        ru_majflt
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
            printerr('Could not convert "{0}" to a number'.format(amount))
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
        with open(fs.join(data, item), 'rb') as file:
            content = file.read()
        for tool in tools:
            yield (tool[0], tool[1], tool[2], item, content, repeats, logqueue,)


# Data, repeats, [[name, location, execrule], ...], loglocation
def execute(data, repeats, tools, loglocation):
    cores = ask_cores()
    logger = Logger(loglocation)
    args = [x for x in argument_generator(data, repeats, tools, logger.logqueue)]
    logger.start()
    with multiprocessing.Pool(processes=cores) as pool:
        pool.starmap(parallel_execute, args)
    logger.stop()