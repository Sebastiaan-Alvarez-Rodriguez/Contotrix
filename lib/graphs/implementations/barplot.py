import numpy as np
import matplotlib.pyplot as plt

from lib.ui.color import printerr
import lib.ui.menu as menu

def gen(csvs, processing_benign):
    # benign = menu.standard_yesno('Show benign stats (y) or malicious stats (n)?')
    bars = []
    names = []
    use_csvs = [x for x in csvs if x.is_benign_set()==processing_benign]
    if len(use_csvs) == 0:
        printerr('There were no {0} csvs'.format('benign' if processing_benign else 'purposefully incorrect'))
        return

    for x in use_csvs:
        bars.append((x.get_correct_total(), x.get_incorrect_total(), x.get_had_timeout_total(), x.get_had_error_total(),))
        names.append(x.name)

    # width of the bars
    barWidth = 0.2

    # The x position of bars
    bar_pos = []
    for itr, _ in enumerate(bars):
        if itr == 0:
            bar_pos.append(np.arange(len(bars[0])))
        else:
            bar_pos.append([x+barWidth*itr for x in bar_pos[0]])

    for name, pos, bar in zip(names, bar_pos, bars):
        plt.bar(pos, bar, width=barWidth, edgecolor='black', label=name)


    print([r + barWidth for r in range(len(bars[0]))])

    plt.xticks([r + barWidth for r in range(len(bars[0]))], ['correct', 'incorrect', 'timeout', 'error'])
    plt.title('Analysis outcome for tools on {0} {1} webpages'.format(csvs[0].get_amount(), 'benign' if benign else 'malicious'))
    plt.ylabel('amount')

    plt.legend(loc='upper {0}'.format('left' if benign else 'right'))

    x_positions = [*r1, *r2, *r3, *r4]
    for pos in bar_pos:
        x_positions.append(*pos)

    y_positions = []
    for bar in bars:
        y_positions.append(*bar)

    for x_pos, y_pos in zip(x_positions, y_positions):
        plt.text(x = x_pos-0.05, y = y_pos+0.5, s = y_pos, size = 8)

    plt.show()