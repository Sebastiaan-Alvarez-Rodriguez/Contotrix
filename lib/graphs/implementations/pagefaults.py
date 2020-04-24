import numpy as np
import matplotlib.pyplot as plt

import lib.fs as fs
from lib.settings import settings

from lib.ui.color import printerr

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
    plt.rcParams["figure.figsize"] = (16,12) #dimensions in inches

    bars = []
    names = []
    for x in use_frames:
        item = (x.get_soft_pagefaults_total(), x.get_hard_pagefaults_total(),)
        bars.append(item)
        names.append(x.get_nice_name())

    tags = ['soft pagefaults', 'hard pagefaults']

    # width of the bars
    barWidth = 0.9/len(use_frames)

    # The x position of bars
    bar_pos = []
    for itr, _ in enumerate(bars):
        if itr == 0:
            bar_pos.append(np.arange(len(bars[0])))
        else:
            bar_pos.append([x+barWidth*itr for x in bar_pos[0]])

    for name, pos, bar in zip(names, bar_pos, bars):
        plt.bar(pos, bar, width=barWidth, edgecolor='black', label=name)


    plt.xticks([r + barWidth for r in range(len(bars[0]))], tags)
    plt.title('Analysis outcome for tools on {0} {1}-formed webpages'.format(frames[0].get_amount(), 'well' if processing_wellformed else 'ill'))
    plt.ylabel('amount')

    plt.legend(loc='upper right')

    x_positions = []
    for pos in bar_pos:
        x_positions.extend(pos)

    y_positions = []
    for bar in bars:
        y_positions.extend(bar)

    for x_pos, y_pos in zip(x_positions, y_positions):
        plt.text(x = x_pos*0.95, y = y_pos*1.05, s = y_pos, size = 8)

    plt.yscale('log')

    if show_output:
        plt.show()

    fs.mkdir(settings.godir, exist_ok=True)
    fig = plt.gcf()
    fig.set_size_inches(16,12) #dimensions in inches
    fig.savefig(fs.join(settings.godir, 'pagefaults_large.pdf' if print_large else 'pagefaults.pdf'), format='eps')

    if print_large:
        plt.rcdefaults()