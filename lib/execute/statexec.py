#!/usr/bin/env python

    '''
    File responsible to act as drone, in case called program segfaults.
    This file gets executed from the main framework.
    In the stdin to this process is the contents of the HTML file.
    This process should pipe it to any children it calls.
    In the system arguments is the command to execute,
    the html content size residing in stdin (useful for C programs),
    amount of times to repeat parsing,
    a location to use as working directory, 
    a timeout, 
    and a boolean indicating whether we must surpress stderr

    Credits to Realz Slaw for suggesting using resource to measure os parameters: 
    https://stackoverflow.com/users/586784/realz-slaw
    Question: 
    https://stackoverflow.com/questions/13607391/


    '''

import sys
import os
import subprocess
import resource

def measure():
    cmd = sys.argv[1].split(' ') # execrule
    cmd.append(sys.argv[2])      # html size
    cmd.append(sys.argv[3])      # repeats
    
    print_stderr = sys.argv[6] == 'True'
    output = None
    try:
        if print_stderr:
            output = int(subprocess.check_output(cmd, env=os.environ.copy(), cwd=sys.argv[4], input=sys.stdin.buffer.read(), timeout=float(sys.argv[5])))
        else:
            output = int(subprocess.check_output(cmd, env=os.environ.copy(), cwd=sys.argv[4], input=sys.stdin.buffer.read(), timeout=float(sys.argv[5]), stderr=subprocess.DEVNULL))
    except subprocess.TimeoutExpired as e:
        print(','.join(['0' for x in range(6)])+',True,False')
        return
    except Exception as e:
        print(','.join(['0' for x in range(6)])+',False,True')
        return

    usages = resource.getrusage(resource.RUSAGE_CHILDREN)

    fields = []
    fields.append(output)           # Number of links found
    fields.append(usages.ru_utime)  # User time (float)
    fields.append(usages.ru_stime)  # System time (float)
    fields.append(usages.ru_maxrss) # Maximal ram usage (kb)
    fields.append(usages.ru_minflt) # Soft page faults
    fields.append(usages.ru_majflt) # Hard page faults
    fields.append(False)            # Timeout
    fields.append(False)            # Error
    print(','.join(map(str, fields)))

if __name__ == '__main__':
    measure()