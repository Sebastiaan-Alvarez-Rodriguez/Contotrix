import subprocess
import requests
import gzip
import shutil

import lib.fs as fs
import lib.settings as settings

from lib.ui.color import printc, printerr, Color


def gz_extract(inp, outp):
    with gzip.open(inp, 'rb') as f_in:
        with open(outp, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def crawl(args):
    if len(splitted) != 3:
        printerr('Need at least 2 arguments to execute: <amount>, <year> <month>')
        return False, 0

    try:
        amount = int(splitted[0])
        year = int(splitted[1])
        month = int(splitted[2])
    except Exception as e:
        printerr('Cannot convert "{0}", "{1}" or "{2}" to number'.format(splitted[0], splitted[1], splitted[2]))
        return False, 0

    if not fs.isfile(settings.root, 'lib', 'download', 'commoncrawl', 'extractor'):
        print('In order to compile the page extractor, you need a compiler with ', end='')
        printc('c++11', Color.CAN, end=' ')
        print('support or newer')

        if not standard_yesno('Continue?'):
            printerr('Extractor compilation cancelled')
            return False, 0

        try:
            subprocess.check_output(['make', 'fast'], cwd=fs.join(settings.root, 'lib', 'download', 'commoncrawl'))
        except subprocess.CalledProcessError as e:
            printerr('Extractor compilation error')
            return False, 0
        except Exception as e:
            printerr('No GNU make available: Please install GNU Make first!')
            return False, 0
        printc('Extractor successfully compiled', Color.GRN)
    
    print('Downloading and extracting ', end='')
    printc(str(amount), Color.PRP, end=' html pages\n')

    dlpath = fs.join(settings.ddir, 'tmp')
    fs.mkdir(dlpath)
    extracted = 0

    while extracted < amount:
        full_dl_path = fs.join(dlpath, url.split('/')[-1])
        full_out_path = fs.join(dlpath, url.split('/')[-1]+'.out')
        # Download .gz file
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(full_dl_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=4096): 
                    if chunk:
                        f.write(chunk)
        # Extract .gz file to .gz.out
        gz_extract(full_dl_path, full_out_path)
        # Remove .gz file
        fs.rm(full_dl_path)
        try:
            out = subprocess.check_output([fs.join(settings.root, 'lib', 'download','commoncrawl', 'extractor'), full_out_path, settings.ddir])
        except subprocess.CalledProcessError as e:
            printerr('Unknown exception occured in crawler')
            print(e)
            return False, 0
        except Exception as e:
            printerr('Unknown exception occured in crawler')
            print(e)
            return False, 0
        fs.rm(full_out_path)
        fs.rm(dlpath)
        extracted += int(out.decode('utf-8'))

    return True, extracted