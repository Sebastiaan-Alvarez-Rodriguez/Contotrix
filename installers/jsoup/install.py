def install(location, fs):
    file = fs.join(fs.abspathfile(__file__), 'jsoup.jar')
    fs.cp(file, location)
    return True