#!/usr/bin/env python
import vaex
from numpy import linspace

import matplotlib.pyplot as plt
from lib.ui.color import printerr

def gen(frames, processing_benign):
    use_frames = [x for x in frames if x.is_benign_set()==processing_benign]
    use_frames.sort()

    if len(use_frames) == 0:
        printerr('There were no {0}-formed frames'.format('well' if processing_benign else 'ill'))
        return

    for num, frame in enumerate(use_frames):
        subgroup = frame.df.mean(frame.df.maxmem, binby=frame.df.totaltime, limits=[0,10],shape=1024, selection=(not frame.df.error) and (not frame.df.timeout))
        plt.plot(linspace(0,10,1024),subgroup, '-', label=frame.get_nice_name())
    plt.title('Tool execution time vs max memory usage on {0}-formed webpages'.format('well' if processing_benign else 'ill'))
    plt.xlabel('Execution times (in seconds)')
    plt.ylabel('Max memory footprints (in bytes)')
    # plt.minorticks_on()
    # plt.grid(b=True,which='both',axis='both')
    plt.legend(loc='upper left')
    # plt.axis([0, 35000000, 0, 7210])

    # plt.xscale('log')
    plt.yscale('log')

    plt.show()
