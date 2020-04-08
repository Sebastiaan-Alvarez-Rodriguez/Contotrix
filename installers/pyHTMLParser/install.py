def install(location, fs):
    file = fs.join(fs.abspathfile(__file__), 'parse.py')
    fs.cp(file, location)
    return True