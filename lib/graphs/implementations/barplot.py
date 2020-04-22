import numpy as np
import matplotlib.pyplot as plt

from lib.ui.color import printerr

def gen(csvs, processing_benign):
    use_csvs = [x for x in csvs if x.is_benign_set()==processing_benign]
    use_csvs.sort()

    if len(use_csvs) == 0:
        printerr('There were no {0}-formed csvs'.format('well' if processing_benign else 'ill'))
        return

    bars = []
    names = []
    for x in use_csvs:
        bars.append((x.get_parsed_ok_total(), x.get_had_timeout_total(), x.get_had_error_total(),))
        names.append(x.get_nice_name())

    tags = ['parsed', 'timeout', 'error']

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

    plt.xticks([r + barWidth for r in range(len(bars[0]))], tags)
    plt.title('Analysis outcome for tools on {0} {1}-formed webpages'.format(csvs[0].get_amount(), 'well' if processing_benign else 'ill'))
    plt.ylabel('amount')

    plt.legend(loc='upper right')

    x_positions = []
    for pos in bar_pos:
        x_positions.extend(pos)

    y_positions = []
    for bar in bars:
        y_positions.extend(bar)

    for x_pos, y_pos in zip(x_positions, y_positions):
        plt.text(x = x_pos-0.05, y = y_pos+0.9, s = y_pos, size = 8)

    plt.show()