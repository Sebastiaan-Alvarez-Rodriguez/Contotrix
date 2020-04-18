import subprocess
import requests
import gzip
import shutil

import lib.fs as fs
from lib.settings import settings
from lib.ui.menu import standard_yesno

from lib.ui.color import printc, printerr, Color

def download(url, output):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(output, 'wb') as f:
            for chunk in r.iter_content(chunk_size=4096): 
                if chunk:
                    f.write(chunk)

def gz_extract(inp, outp):
    with gzip.open(inp, 'rb') as f_in:
        with open(outp, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def crawl(args):
    splitted = args.split(' ')
    if len(splitted) != 3:
        printerr('Need at least 2 arguments to execute: <amount>, <year> <magicnumber>')
        return False, 0

    try:
        amount = int(splitted[0])
        year = int(splitted[1])
        magicnumber = int(splitted[2])
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
    

    print('Downloading package manifest')

    dlpath = fs.join(settings.ddir, 'tmp')
    manifest_dl_loc = fs.join(dlpath, 'manifest.gz')
    fs.mkdir(dlpath)
    download('https://commoncrawl.s3.amazonaws.com/crawl-data/CC-MAIN-{0}-{1}/warc.paths.gz'.format(year, magicnumber), manifest_dl_loc)

    print('Downloading and extracting (at least) ', end='')
    printc(str(amount), Color.PRP, end=' html pages\n')

    extracted = 0
    with gzip.open(manifest_dl_loc, 'rt') as file:
        while extracted < amount:
            url = 'https://commoncrawl.s3.amazonaws.com/'+file.readline()[:-1]
            full_dl_path = fs.join(dlpath, url.split('/')[-1])
            full_out_path = fs.join(dlpath, url.split('/')[-1]+'.out')
            # Download .gz file
            print('Downloading '+url)
            download(url, full_dl_path)
            # Extract .gz file to .gz.out
            print('Extracting... ')
            gz_extract(full_dl_path, full_out_path)
            # Remove .gz file
            print('Deleting archive...')
            fs.rm(full_dl_path)
            print('Processing WARC file...')
            try:
                out = subprocess.check_output([fs.join(settings.root, 'lib', 'download','commoncrawl', 'extractor'), full_out_path, settings.ddir, str(amount-extracted)])
            except subprocess.CalledProcessError as e:
                printerr('Unknown exception occured in crawler')
                print(e)
                fs.rm(dlpath)
                return False, 0
            except Exception as e:
                printerr('Unknown exception occured in crawler')
                print(e)
                fs.rm(dlpath)
                return False, 0
            local_extracted = int(out.decode('utf-8'))
            extracted += local_extracted
            print('Extracted {0} html files ({1} total)'.format(local_extracted, extracted))
            print('Deleting WARC file...')
            fs.rm(full_out_path)
    print('Enough html files extracted. Deleting temporary directory...')
    fs.rm(dlpath)
    return True, extracted