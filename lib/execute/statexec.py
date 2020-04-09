#!/usr/bin/env python

#     #Credits to Realz Slaw: https://stackoverflow.com/users/586784/realz-slaw
#     #Question: https://stackoverflow.com/questions/13607391/

import sys
import subprocess
import resource

print('Statexec: got {0} parameters'.format(len(sys.argv)), file=sys.stderr)
print('execrule: {0}'.format(sys.argv[1]), file=sys.stderr)
print('repeats: {0}'.format(sys.argv[2]), file=sys.stderr)
# output = subprocess.check_output(['installed/haut/Haut', 'data/', '2000'], cwd='/home/radon/Uni/mir/final/final')
cmd = sys.argv[1].split(' ') # execrule
cmd.append(sys.argv[2])      # repeats
output = subprocess.check_output(cmd, cwd=sys.argv[3], universal_newlines=True, input=sys.stdin.read())
usages = resource.getrusage(resource.RUSAGE_CHILDREN)
# https://docs.python.org/3/library/resource.html
fields = []
fields.append(output)
fields.append(usages.ru_utime)  # User time (float)
fields.append(usages.ru_stime)  # System time (float)
fields.append(usages.ru_maxrss) # Maximal ram usage (kb)
fields.append(usages.ru_minflt) # Soft page faults
fields.append(usages.ru_majflt) # Hard page faults
print(','.join(map(str, fields)))