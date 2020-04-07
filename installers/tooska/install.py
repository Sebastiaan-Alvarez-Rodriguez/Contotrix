import subprocess

def install(location, fs):
    path = fs.join(fs.abspathfile(__file__), 'code')
    
    for item in fs.ls(path):
        fs.cp(fs.join(path, item), fs.join(location, item))

    library_location = fs.join(location, 'library')
    try:
        subprocess.check_output(['cmake', '.'], cwd=library_location)
    except subprocess.CalledProcessError as e:
        print('Compilation error')
        return False
    except Exception as e:
        print('No CMake available: Please install CMake first!')
        return False

    try:
        subprocess.check_output(['make', 'tooska', '-j'], cwd=library_location)
    except subprocess.CalledProcessError as e:
        print('Compilation error')
        return False
    except Exception as e:
        print('No make available: Please install GNU Make first!')
        return False

    return True