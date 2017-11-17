from PySide import QtGui
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
#load new html template
def newHtmlFile():
    filename,_= QtGui.QFileDialog().getOpenFileName(caption='Open file',filter="Html (*.html)")
    return filename


def treeDictionary(tree_dict,tag_list,data_list):
    if len(tag_list) != 0 and len(data_list)!= 0:
        tag,data= tag_list.pop(),data_list.pop()
        if tag == 'start':
            tree_dict[data] = {}
            treeDictionary(tree_dict[tag],tag_list,data_list)
        else:
            




#build a StandItemModel for the new html template
def setStandardItemModel(file_path):
    import codecs
    f = codecs.open(file_path,'r','utf-8')
    parser = TheHTMLParser()
    parser.feed(f.read())
    test = {}
    tag,tagdata = parser.tag,parser.tagdata
    treeDictionary(test,tag,tagdata)
    print test



    # model = QtGui.QStandardItemModel()
    # parentItem = model.invisibleRootItem()
    # for tag,data in zip(parser.tag,parser.tagdata):
    # 	item = QtGui.QStandardItem(data)
    # 	if tag != "data":




    # for i in range(4):
    #     item = QtGui.QStandardItem("item %d" % i)
    #     parentItem.appendRow(item)
    #     parentItem = item
    # return model


class TheHTMLParser(HTMLParser,object):
    def __init__(self):
        super(TheHTMLParser, self).__init__()
        self.tag = []
        self.tagdata = []
    def handle_starttag(self, tag, attrs):
        self.tag.append('start')
        self.tagdata.append(tag)

    def handle_endtag(self, tag):
        self.tag.append('end')
        self.tagdata.append(tag)

    def handle_data(self, data):
        self.tag.append('data')
        self.tagdata.append(data)
