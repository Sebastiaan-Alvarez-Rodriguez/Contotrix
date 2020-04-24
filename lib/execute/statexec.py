#!/usr/bin/env python
    # Credits to Realz Slaw for suggesting this way of measuring os parameters: 
    # https://stackoverflow.com/users/586784/realz-slaw
    # Question: 
    # https://stackoverflow.com/questions/13607391/

import sys
import os
import subprocess
import resource

def measure():
    # print('Statexec: got {0} parameters'.format(len(sys.argv)), file=sys.stderr)
    # print('execrule: {0}'.format(sys.argv[1]), file=sys.stderr)
    # print('repeats: {0}'.format(sys.argv[3]), file=sys.stderr)



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

    # https://docs.python.org/3/library/resource.html
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