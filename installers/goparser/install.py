import subprocess

def install(location, fs):
    file = fs.join(fs.abspathfile(__file__), 'parse.go')
    fs.cp(file, location)
    try:
        subprocess.check_output(['go', 'build', 'parse.go'], cwd=location)
    except subprocess.CalledProcessError as e:
        print('Compilation error')
        return False
    except Exception as e:
        print('No go available: Please install go first!')
        return False
    return True