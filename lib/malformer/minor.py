import os
import re
import random

import lib.fs as fs
from lib.settings import settings
from lib.ui.color import printerr, printc, Color

def generate_html_files(location):
    with os.scandir(location) as it:
        for entry in it:
            if entry.is_file() and entry.name.endswith('.html'):
                yield entry

def gen(tail):
    fs.mkdir(settings.mdir, exist_ok=True)

    try:
        amount = int(tail)
    except Exception as e:
        printerr('Given amount "{0}" is not a number!'.format(tail))
        return

    generated = 0
    for entry in generate_html_files(settings.ddir):
        if generated >= amount:
            printc('Successfully generated {0} malformed html files'.format(generated), Color.GRN)
            return
        try:
            with open(fs.join(settings.mdir, entry.name), 'w') as outfile:
                with open(entry, 'r') as file:
                    for line in file:
                        if '<!DOCTYPE html>' in line:
                            line = line.replace('<!DOCTYPE html>', '')
                        elif '<img' in line:
                            has_src = 'src=' in line 
                            has_alt = 'alt=' in line
                            if has_alt and has_src:
                                if bool(random.getrandbits(1)):
                                    line = re.sub('src=[\'"][a-zA-Z\\.+=0-9/\\,:;]*[\'"]', '',line)
                                else:
                                    line = re.sub('alt=[\'"][a-zA-Z\\.+=0-9/\\,:;]*[\'"]', '',line)
                            elif has_src:
                                line = re.sub('src=[\'"][a-zA-Z\\.+=0-9/\\,:;]*[\'"]', '',line)
                            elif has_alt:
                                line = re.sub('alt=[\'"][a-zA-Z\\.+=0-9/\\,:;]*[\'"]', '',line)
                        outfile.write(line)
            generated += 1
        except Exception as e:
            fs.rm(settings.mdir, entry.name)
    printc('Partial success! Generated {0} malformed html files before data directory was exhausted'.format(generated), Color.YEL)