import vaex
import matplotlib.pyplot as plt

import lib.fs as fs
from lib.settings import settings

from lib.ui.color import printerr


def gen(frames, processing_wellformed, print_large=False, show_output=False):
    use_frames = [x for x in frames if x.is_unbound_set()]
    

    if len(use_frames) == 0:
        printerr('Could not find any unbound {0}-formed frames'.format('well' if processing_wellformed else 'ill'))
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
    fig.set_size_inches(16,12) #dimensions in inches


    for num, frame in enumerate(use_frames):
        subgroup = frame.df.mean(frame.df.totaltime, binby=frame.df.htmlsize, shape=1024, selection=(not frame.df.error) and (not frame.df.timeout))        
        ax.plot(subgroup, 'o', label=frame.get_nice_name())

    ax.set_title('Unbound tool execution time on {0}-formed webpages'.format('well' if processing_wellformed else 'ill'))
    ax.set_xlabel('Webpage size (in bytes)')
    ax.set_ylabel('Execution times (in seconds)')
    # plt.minorticks_on()
    # plt.grid(b=True,which='both',axis='both')
    ax.legend(loc='upper left')
    # plt.axis([0, 35000000, 0, 7210])

    # plt.xscale('log')
    ax.set_yscale('log')

    if show_output:
        plt.show()

    fs.mkdir(settings.godir, exist_ok=True)
    
    
    fig.savefig(fs.join(settings.godir, 'sizetimeunbound_large.pdf' if print_large else 'sizetimeunbound.pdf'), format='pdf')

    if print_large:
        plt.rcdefaults()