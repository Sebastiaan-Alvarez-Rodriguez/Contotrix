import os
import shutil
import sys

def abspath(path):
    return os.path.abspath(path)

# Returns absolute path for a given file
def abspathfile(file):
    return os.path.abspath(os.path.dirname(file))

def basename(path):
    return os.path.basename(path)

def cp(path_src, path_dst):
    if isfile(path_src):
        shutil.copy2(path_src, path_dst)
    else:
        shutil.copytree(path_src, path_dst)

def cwd():
    return os.getcwd()

def dirname(path):
    return os.path.dirname(path)

def exists(path, *args):
    return os.path.exists(join(path,*args))

def isdir(path, *args):
    return os.path.isdir(join(path,*args))

def isemptydir(path, *args):
    try:
        next(ls(path, *args))
        return False
    except StopIteration as e:
        return True

def isfile(path, *args):
    return os.path.isfile(join(path,*args))

def join(directory, *args):
    returnstring = directory
    for arg in args:
        returnstring = os.path.join(returnstring, str(arg))
    return returnstring

def ls(directory, *args):
    with os.scandir(directory) as it:
        for entry in it:
            yield entry.name

def lsonlydir(directory, full_paths=False):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                if not full_paths:
                    yield entry.name
                else:
                    yield [join(directory, entry.name)]

def mkdir(path, exist_ok=False):
    os.makedirs(path, exist_ok=exist_ok)

def mkdir(path, *args, exist_ok=False):
    os.makedirs(join(path, *args), exist_ok=exist_ok)

def mv(path_src, path_dst):
    shutil.move(path_src, path_dst)

def rm(directory, *args, ignore_errors=False):
    path = join(directory, *args)
    if isdir(path):
        shutil.rmtree(path, ignore_errors=ignore_errors)
    else:
        os.remove(path)

def sep():
    return os.sep

# Return size of file in bytes
def sizeof(directory, *args):
    path = join(directory, *args)
    if not isfile(path):
        raise RuntimeError('Error: "{0}" is no path to a file'.format(path))
    return os.path.getsize(path)

def split(path):
    return path.split(os.sep)