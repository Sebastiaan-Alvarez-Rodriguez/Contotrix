import numpy as np

'''
Generate general stats (all text)
'''


def tab_head():
    print(f'''
\\begin{{table}}[tb]
    \\centering
    \\begin{{tabular}}{{|r|r|r||r|}}
        \\hline
        \\textbf{{Name}} & \\textbf{{mean time}} & \\textbf{{std. dev.}} & \\textbf{{links found}}\\\\ \\hline
''')


def tab_tail():
    print(f'''
    \\end{{tabular}}
    \\caption{{Time statistics and links found on dataset}}
    \\label{{tab:time_stats}}
\\end{{table}}''')


def time_mean_stddev(frame):
    subset = frame.df[frame.df.error+frame.df.timeout==2]
    mean = subset.mean(subset.totaltime)
    subset['subbed'] = (subset.totaltime-mean)**2
    stddev_mean = subset.mean(subset.subbed)
    return frame.get_nice_name(), mean, np.sqrt(stddev_mean)


# Main function
def gen(frames):
    wellformed = [x for x in frames if x.is_wellformed_set() and not x.is_unbound_set()]
    malformed = [x for x in frames if (not x.is_wellformed_set()) and not x.is_unbound_set()]

    tab_head()    
    for x in wellformed:
        name, mean, stddev = time_mean_stddev(x)
        subset = x.df[x.df.error+x.df.timeout==2]
        print(f'        {name} & {np.round(mean, 2)} & {np.round(stddev, 2)} & {np.round(subset.mean(subset.linksfound))}\\\\ \\hline')
    if len(wellformed) > 0 and len(malformed) > 0:
        print(f'        \\hline')
    for x in malformed:
        name, mean, stddev = time_mean_stddev(x)
        subset = x.df[x.df.error+x.df.timeout==2]
        print(f'        {name} & {np.round(mean, 2)} & {np.round(stddev, 2)} & {np.round(subset.mean(subset.linksfound))}\\\\ \\hline')
    tab_tail()


    # collected = wellformed[0].df[['htmlname','linksfound']]
    # for idx, x in enumerate(wellformed[1:]):
    #     collected = collected.join(x.df[['htmlname','linksfound']], on='htmlname', rsuffix=str(idx))
    #     collected.drop('htmlname'+str(idx), inplace=True)
    # print(collected)

    # collected.htmlname
    # collected['majority'] = collected.apply(most_common, arguments=[[collected.linksfound, collected.linksfound0, collected.linksfound1,collected.linksfound2,collected.linksfound3,collected.linksfound4,collected.linksfound5,collected.linksfound6,collected.linksfound7]])