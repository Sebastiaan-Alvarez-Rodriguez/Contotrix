import random

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
                            if '<head>' in line:
                                line = line.replace('<head>', '')

                            elif '</html>' in line:
                                line = line.replace('</html>', '')
                            else:
                                if random.randrange(5) == 0:
                                    if bool(random.getrandbits(1)):
                                        line += '<insertedopen>'
                                    else:
                                        line += '</insertedclose>'
                            outfile.write(line)
                amount -= 1