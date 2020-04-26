import xml.etree.ElementTree as tree

class Config(object):
    '''
    Object to read configs of installers, which contain install requirements
    '''
    def __init__(self, path):
        self.path = path
        t = tree.parse(path)
        self.sections = dict()
        for child in t.getroot():
            self.sections[child.tag] = child

    # Return XML elements with given name
    def get(self, name):
        sources = []
        for source in self.sections[name]:
            sources.append(source)
        return sources     
    
    # Return dependencies, as a list of tuples. 
    # A tuple contains the dependency description, 
    #  as well as a boolean indicating whether 
    # we have a minimal dependency (aka if a higher version is okay)
    def get_dependencies(self):
        l = []
        for source in self.sections['deps']:
            l.append((source.text, 'type' in source.attrib and source.attrib['type'] == 'minimum',))
        return l

    # Basic function to get child attributes for all tags with a given name
    def getChildAttributes(self, name):
        attributes = []
        for source in self.sections[name]:
            attributes.append(source.attrib)
        return attributes