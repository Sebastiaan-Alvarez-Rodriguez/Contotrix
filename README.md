# Current ideas
 1. DONE - Get code of parsers to work
 2. DONE - Use python framework to run code using subprocesses
 3. DONE - Use psutil.memory_percent() for avg mem usage and psutil.cpu_percent() for avg cpu usage . See [here](https://psutil.readthedocs.io/en/latest/)

# Currently working
In C:
 1. Haut
 2. Gumbo
 3. Lexbor
 4. Tooska (but gives errors/warnings for no reason)
In Python:
 1. html.parser (pyTHMLParser)
 2. beautifulsoup (pyBeautifulSoup)
 3. lxml (pylxml)
In Java:
TODO: Get Java parsers
 1. [hpar](https://github.com/zhijia/HPar)
 2. [mozilla wrapper (2008-old)](http://mozillaparser.sourceforge.net/)
 3. [perhaps raw firefox](https://www.google.com/search?client=ubuntu&channel=fs&q=firefox+html+parser&ie=utf-8&oe=utf-8)

# Datasets
 Some large ones:
 1. [Mine for more datasets](https://www.researchgate.net/post/Where_can_I_find_the_web_pages_dataset_for_information_extraction)
 2. Go collecting myself? I could take from multiple sources, storing by doing md5/sha2 to prevent collisions
 3. Collect from [commoncrawl](https://commoncrawl.org/the-data/get-started/)
<!-- https://commoncrawl.org/2020/04/march-april-2020-crawl-archive-now-available/ -->

# Fix slowness
 Maybe perform measurements not using resource package
 1. [make something yourself](https://medium.com/the-andela-way/machine-monitoring-tool-using-python-from-scratch-8d10411782fd)

## HTML parsers for Python
[here](https://stackoverflow.com/questions/11709079/parsing-html-using-python)