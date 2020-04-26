import numpy as np
import matplotlib.pyplot as plt

import lib.fs as fs
from lib.settings import settings
from lib.ui.color import printerr


'''
Generate main barplot, containing parsed, timeout, error bars
'''

# Main function
def gen(frames, processing_wellformed, print_large=False, show_output=False):
    use_frames = [x for x in frames if x.is_wellformed_set()==processing_wellformed and not x.is_unbound_set()]
    use_frames.sort()

    if len(use_frames) == 0:
        printerr('There were no {0}-formed frames'.format('well' if processing_wellformed else 'ill'))
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


    bars = []
    names = []
    for x in use_frames:
        item = (x.get_had_succes_total(), x.get_had_timeout_total(), x.get_had_error_total(),)
        bars.append(item)
        names.append(x.get_nice_name())

    tags = ['parsed', 'timeout', 'error']

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
    plt.title('Outcome for tools on {0} {1}-formed webpages'.format(frames[0].get_amount(), 'well' if processing_wellformed else 'ill'))
    plt.ylabel('amount')

    plt.legend(loc='lower left')

    x_positions = []
    for pos in bar_pos:
        x_positions.extend(pos)

    y_positions = []
    for bar in bars:
        y_positions.extend(bar)

    y_seen = []
    for x_pos, y_pos in zip(x_positions, y_positions):
        seen = False
        for val in y_seen:
            if y_pos*0.94 <= val <= y_pos*1.06 or y_pos == 0:
                seen = True
                break
        if seen:
            continue
        plt.text(x=x_pos-0.05, y=y_pos+0.9, s=y_pos, size=fontsize)
        y_seen.append(y_pos)

    plt.yscale('log')
    fig.tight_layout()

    if show_output:
        plt.show()

    fs.mkdir(settings.godir, exist_ok=True)


    fig.savefig(fs.join(settings.godir, 'barplot_large.pdf' if print_large else 'barplot.pdf'), format='pdf')

    if print_large:
        plt.rcdefaults()

    plt.close()

    print(f'''
\\begin{{table}}[tb]
    \\centering
    \\begin{{tabular}}{{|r|r|r|r|}}
        \\hline
        \\textbf{{Name}} & \\textbf{{Parsed}} & \\textbf{{timeout}} & \\textbf{{error}} \\\\ \\hline
''')
    for name, pos, bar in zip(names, bar_pos, bars):
        print(f'''{name} & {bar[0]} & {bar[1]} & {bar[2]} \\\\ \\hline''')

    print(f'''
    \\end{{tabular}}
    \\caption{{Outcome on {frames[0].get_amount()} {"well" if processing_wellformed else "ill"}-formed webpages}}
    \\label{{tab:general_stats}}
\\end{{table}}''')