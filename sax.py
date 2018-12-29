#0.01
import xml.sax as sx
import time

class countHandler(sx.handler.ContentHandler):
    
    def __init__(self):
        self.tags = {}

    def startElement(self,name,attr):
        if not self.tags.get(name):
            self.tags[name]=0
        self.tags[name] += 1

start = time.clock()
parser = sx.make_parser()
handler = countHandler()
parser.setFeature(sx.handler.feature_external_ges, False)
parser.setContentHandler(handler)
parser.parse("file.xml")
end = time.clock()
print(handler.tags)
print(end-start)
