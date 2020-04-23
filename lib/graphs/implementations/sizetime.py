#!/usr/bin/env python
import vaex
from numpy import linspace

import matplotlib.pyplot as plt
from lib.ui.color import printerr

def gen_old(frames, processing_benign):
    use_frames = [x for x in frames if x.is_benign_set()==processing_benign]
    use_frames.sort()

    if len(use_frames) == 0:
        printerr('There were no {0}-formed frames'.format('well' if processing_benign else 'ill'))
        return

    # colors = ['bo', 'ro', 'co', 'yo']
    for num, frame in enumerate(use_frames):
        times = [x.total_time if (not x.error) and (not x.timeout) else -1000 for x in csv.lines]
        sizes = [x.html_size  for x in csv.lines]
        plt.plot(sizes, times, ',', label=csv.get_nice_name())
    plt.title('Tool execution time on {0}-formed apks in dataset'.format('well' if processing_benign else 'ill'))
    plt.xlabel('Webpage size (in bytes)')
    plt.ylabel('Execution times (in seconds)')
    # plt.minorticks_on()
    # plt.grid(b=True,which='both',axis='both')
    plt.legend(loc='upper left')
    # plt.axis([0, 35000000, 0, 7210])

    plt.xscale('log')
    plt.yscale('log')

    plt.show()

def gen(frames, processing_benign):
    use_frames = [x for x in frames if x.is_benign_set()==processing_benign]
    use_frames.sort()

    if len(use_frames) == 0:
        printerr('There were no {0}-formed frames'.format('well' if processing_benign else 'ill'))
        return

    # TODO: Try to generate s.t. we get an average speed per size
    for num, frame in enumerate(use_frames):
        subgroup = frame.df.mean(frame.df.totaltime, binby=frame.df.htmlsize, shape=1024, selection=(not frame.df.error) and (not frame.df.timeout))
        print(subgroup)
        
        plt.plot(subgroup, '-', label=frame.get_nice_name())
    plt.title('Tool execution time on {0}-formed apks in dataset'.format('well' if processing_benign else 'ill'))
    plt.xlabel('Webpage size (in bytes)')
    plt.ylabel('Execution times (in seconds)')
    # plt.minorticks_on()
    # plt.grid(b=True,which='both',axis='both')
    plt.legend(loc='upper left')
    # plt.axis([0, 35000000, 0, 7210])

    # plt.xscale('log')
    plt.yscale('log')

    plt.show()
