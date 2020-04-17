import subprocess

import lib.fs as fs
import lib.settings as settings

from lib.ui.color import printc, printerr, Color

def crawl(args):
    if len(splitted) != 2:
        printerr('Need at least 2 arguments to execute: <begin url>, <amount>')
        return False, 0

    try:
        amount = int(splitted[1])
    except Exception as e:
        printerr('Cannot convert "{0}" to number'.format(splitted[1]))
        return False, 0

    if not fs.isfile(settings.root, 'lib', 'download', 'crawl', 'crawler'):
        print('In order to compile the crawler, you need a compiler with ', end='')
        printc('c-11 and c++11', Color.CAN, end=' ')
        print('support and ')
        printc('libcurl3-dev', Color.CAN, end=' ')
        print('or newer')

        if not standard_yesno('Continue?'):
            printerr('Crawler compilation cancelled')
            return False, 0

        try:
            subprocess.check_output(['make', 'fast'], cwd=fs.join(settings.root, 'lib', 'download', 'crawl'))
        except subprocess.CalledProcessError as e:
            printerr('Crawler compilation error')
            return False, 0
        except Exception as e:
            printerr('No GNU make available: Please install GNU Make first!')
            return False, 0
        printc('Crawler successfully compiled', Color.GRN)
    
    print('Crawling for ', end='')
    printc(str(amount), Color.PRP, end=' html pages\n')

    try:
        out = subprocess.check_output([fs.join(settings.root, 'lib', 'download','crawl', 'crawler'), splitted[0], settings.ddir, str(amount)])
    except subprocess.CalledProcessError as e:
        printerr('Unknown exception occured in crawler')
        print(e)
        return False, 0
    except Exception as e:
        printerr('Unknown exception occured in crawler')
        print(e)
        return False, 0

    downloaded = int(out.decode('utf-8'))
    return True, downloaded