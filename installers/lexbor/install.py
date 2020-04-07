import subprocess

def install(location, fs):
    path = fs.join(fs.abspathfile(__file__), 'code')
    
    for item in fs.ls(path):
        fs.cp(fs.join(path, item), fs.join(location, item))

    library_location = fs.join(location, 'library')
    try:
        subprocess.check_output(['cmake', '.', '-DLEXBOR_BUILD_TESTS=OFF', '-DLEXBOR_BUILD_EXAMPLES=ON', '-DLEXBOR_BUILD_SEPARATELY=ON'], cwd=library_location)
    except subprocess.CalledProcessError as e:
        print('Compilation error')
        return False
    except Exception as e:
        print('No CMake available: Please install CMake first!')
        return False

    try:
        subprocess.check_output(['make', 'lexbor-html', '-j'], cwd=library_location)
    except subprocess.CalledProcessError as e:
        print('Compilation error')
        return False
    except Exception as e:
        print('No make available: Please install GNU Make first!')
        return False

    try:
        subprocess.check_output(['make', 'fast'], cwd=location)
    except subprocess.CalledProcessError as e:
        print('Compilation error')
        return False
    except Exception as e:
        print('No make available: Please install GNU Make first!')
        return False
    return True