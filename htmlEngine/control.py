from PySide import QtGui
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
#load new html template
def newHtmlFile():
    filename,_= QtGui.QFileDialog().getOpenFileName(caption='Open file',filter="Html (*.html)")
    return filename

#build a StandItemModel for the new html template
def setStandardItemModel(file_path):
    import codecs
    f = codecs.open(file_path,'r','utf-8')
    parser = TheHTMLParser()
    parser.feed(f.read())
    print len(parser.tag)
    print len(parser.tagdata)



class TheHTMLParser(HTMLParser,object):
    def __init__(self):
        super(TheHTMLParser, self).__init__()
        self.tag = []
        self.tagdata = []
    def handle_starttag(self, tag, attrs):
        self.tag.append('start')
        self.tagdata.append([tag,attrs])

    def handle_endtag(self, tag):
        self.tag.append('end')
        self.tagdata.append(tag)

    def handle_data(self, data):
        self.tag.append('data')
        self.tagdata.append(data)
