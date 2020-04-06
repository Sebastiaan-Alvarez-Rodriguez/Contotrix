import subprocess
def install(location, fs):
    path = fs.join(fs.abspathfile(__file__), 'code')
    
    for item in fs.ls(path):
        fs.cp(fs.join(path, item), fs.join(location, item))

    try:
        subprocess.check_output(['bash', 'autogen.sh'], cwd=location)
    except subprocess.CalledProcessError as e:
        print('Autogen error')
        return False
    
    try:
        subprocess.check_output(['bash', 'configure'], cwd=location)
    except subprocess.CalledProcessError as e:
        print('Configure error')
        return False
        

    try:
        subprocess.check_output(['make', 'benchmark', '-j'], cwd=location)
    except subprocess.CalledProcessError as e:
        print('Compilation error')
        return False
    except Exception as e:
        print('No GNU make available: Please install GNU Make first!')
        return False
    return True