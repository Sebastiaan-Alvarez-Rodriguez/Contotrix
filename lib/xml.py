import xml.etree.ElementTree as tree

# https://docs.python.org/3.8/library/xml.etree.elementtree.html
class Config(object):
    def __init__(self, path):
        self.path = path
        t = tree.parse(path)
        self.sections = dict()
        for child in t.getroot():
            print('Child: {0}....{1}'.format(child, child.tag))
            self.sections[child.tag] = child

    def get(self, name):
        sources = []
        for source in self.sections[name]:
            sources.append(source)
        return sources     
    
    def get_dependencies(self):
        l = []
        for source in self.sections['deps']:
            l.append((source.text, 'type' in source.attrib and source.attrib['type'] == 'minimum',))
        return l

    def getChildAttributes(self, name):
        attributes = []
        for source in self.sections[name]:
            attributes.append(source.attrib)
        return attributes