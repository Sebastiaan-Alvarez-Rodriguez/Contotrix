def install(location, fs):
    file = fs.join(fs.abspathfile(__file__), 'hpar.jar')
    fs.cp(file, location)
    return True