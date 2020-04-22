#!/usr/bin/env python
import matplotlib.pyplot as plt
from lib.ui.color import printerr

def gen(csvs, processing_benign):
    use_csvs = [x for x in csvs if x.is_benign_set()==processing_benign]
    use_csvs.sort()

    if len(use_csvs) == 0:
        printerr('There were no {0}-formed csvs'.format('well' if processing_benign else 'ill'))
        return

    # colors = ['bo', 'ro', 'co', 'yo']
    for num, csv in enumerate(use_csvs):
        times = [x.total_time if (not x.errors) and (not x.timeout) else -1000 for x in csv.lines]
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
