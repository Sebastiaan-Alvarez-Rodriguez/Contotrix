import vaex
from numpy import linspace
import matplotlib.pyplot as plt

import lib.fs as fs
from lib.settings import settings
from lib.ui.color import printerr

'''
Generate time vs. memory footprint plot
'''

# Main function
def gen(frames, processing_wellformed, print_large=False, show_output=False):
    use_frames = [x for x in frames if x.is_wellformed_set()==processing_wellformed and not x.is_unbound_set()]
    use_frames.sort()

    if len(use_frames) == 0:
        printerr('There were no {0}-formed frames'.format('well' if processing_wellformed else 'ill'))
        return

    if print_large:
        font = {
            'family' : 'DejaVu Sans',
            'weight' : 'bold',
            'size'   : 16
        }
        plt.rc('font', **font)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    fig.set_size_inches(9,6) #dimensions in inches


    for num, frame in enumerate(use_frames):
        frame.df.select(frame.df.error==1 and frame.df.timeout==1, mode='replace', name='timemem')
        subgroup = frame.df.mean(frame.df.maxmem, binby=frame.df.totaltime, shape=256, selection='timemem')
        times = frame.df.first(frame.df.totaltime, frame.df.totaltime, binby=frame.df.totaltime, shape=256, selection='timemem')
        plt.plot(times, subgroup, '-', label=frame.get_nice_name())
    plt.title('Tool execution time vs max memory usage on {0}-formed webpages'.format('well' if processing_wellformed else 'ill'))
    plt.xlabel('Execution times (in seconds)')
    plt.ylabel('Max memory footprints (in bytes)')
    # plt.minorticks_on()
    # plt.grid(b=True,which='both',axis='both')
    plt.legend(loc='upper left')
    # plt.axis([0, 35000000, 0, 7210])

    # plt.xscale('log')
    plt.yscale('log')

    fig.tight_layout()

    if show_output:
        plt.show()

    fs.mkdir(settings.godir, exist_ok=True)


    fig.savefig(fs.join(settings.godir, 'timemem_large.pdf' if print_large else 'timemem.pdf'), format='pdf')

    if print_large:
        plt.rcdefaults()