import vaex
import matplotlib.pyplot as plt

import lib.fs as fs
from lib.settings import settings

from lib.ui.color import printerr

'''
Generate unbound size vs time plot using dots instead of lines to cope with variance
'''

# Main function
def gen(frames, processing_wellformed, print_large=False, show_output=False):
    use_frames = [x for x in frames if x.is_unbound_set()]
    

    if len(use_frames) == 0:
        printerr('Could not find any unbound {0}-formed frames'.format('well' if processing_wellformed else 'ill'))
        return

    fontsize = 8
    if print_large:
        fontsize = 16
        font = {
            'family' : 'DejaVu Sans',
            'weight' : 'bold',
            'size'   : fontsize
        }
        plt.rc('font', **font)
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    fig.set_size_inches(9,6) #dimensions in inches

    for num, frame in enumerate(use_frames):
        frame.df.select(frame.df.error==1 and frame.df.timeout==1, mode='replace', name='sizetimeunbound')
        subgroup = frame.df.mean(frame.df.totaltime, binby=frame.df.htmlsize, shape=256, selection='sizetimeunbound')
        sizes = frame.df.first(frame.df.htmlsize, frame.df.htmlsize, binby=frame.df.htmlsize, shape=256, selection='sizetimeunbound')

        # subgroup = frame.df.mean(frame.df.totaltime, binby=frame.df.htmlsize, shape=1024, selection=frame.df.error==1 and frame.df.timeout==1)
        ax.plot(sizes, subgroup, 'o', label=frame.get_nice_name())

    plt.title('Unbound tool execution time on {0}-formed webpages'.format('well' if processing_wellformed else 'ill'))
    plt.xlabel('Webpage size (in bytes)')
    plt.ylabel('Execution times (in seconds)')
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
    
    
    fig.savefig(fs.join(settings.godir, 'sizetimeunbound_large.pdf' if print_large else 'sizetimeunbound.pdf'), format='pdf')

    if print_large:
        plt.rcdefaults()

    plt.close()

    t = use_frames[0]
    subgroup = t.df[t.df.totaltime>10.0]
    print(f'We found {(len(subgroup)/len(t.df))*100}% of all measurements took longer than 10 seconds')
    print(subgroup)
    print(subgroup.totaltime)
    print(subgroup.sum(subgroup.totaltime))
    print(f'A total of {subgroup.sum(subgroup.totaltime)} seconds ({(subgroup.sum(subgroup.totaltime)/t.df.sum(t.df.totaltime))*100}%) were spent on the measurements >10s')