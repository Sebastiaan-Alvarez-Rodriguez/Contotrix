import xml.etree.ElementTree as tree

# https://docs.python.org/3.8/library/xml.etree.elementtree.html
class Config(object):
    def __init__(self, path):
        self.path = path
        tree = tree.parse(path)
        self.sections = dict()
        for child in tree.getRoot():
            self.sections.update({child.tag, child})

    def getSources(self):
        sources = []
        for source in self.sections['sources']:
            sources.append(source)
        return  sources     
        