#!/usr/bin/env python
import vaex

import matplotlib.pyplot as plt
from lib.ui.color import printerr


def gen(frames, processing_benign):
    use_frames = [x for x in frames if x.is_unbound_set()]
    

    if len(use_frames) == 0:
        printerr('Could not find any unbound {0}-formed frames'.format('well' if processing_benign else 'ill'))
        return

    for num, frame in enumerate(use_frames):
        subgroup = frame.df.mean(frame.df.totaltime, binby=frame.df.htmlsize, shape=1024, selection=(not frame.df.error) and (not frame.df.timeout))        
        plt.plot(subgroup, '-', label=frame.get_nice_name())

    plt.title('Tool execution time vs webpage size on {0}-formed webpages'.format('well' if processing_benign else 'ill'))
    plt.xlabel('Webpage size (in bytes)')
    plt.ylabel('Execution times (in seconds)')
    # plt.minorticks_on()
    # plt.grid(b=True,which='both',axis='both')
    plt.legend(loc='upper left')
    # plt.axis([0, 35000000, 0, 7210])

    # plt.xscale('log')
    plt.yscale('log')

    plt.show()
