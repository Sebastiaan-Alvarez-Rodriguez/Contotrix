import re
import random

import lib.fs as fs
from lib.settings import settings
from lib.ui.color import printerr

def gen(tail):
    fs.mkdir(settings.mdir, exist_ok=True)

    try:
        amount = int(tail)
    except Exception as e:
        printerr('Given amount "{0}" is not a number!')
        return

    with os.scandir(settings.ddir) as it:
        for entry in it:
            if amount <= 0:
                return
            if entry.is_file() and entry.name.endswith('.html'):
                lines = ''
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
                amount -= 1
