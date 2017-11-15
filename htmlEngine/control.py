from PySide import QtGui
from HTMLParser import HTMLParser
#load new html template
def newHtmlFile():
    filename,_= QtGui.QFileDialog().getOpenFileName(caption='Open file',filter="Html (*.html)")
    return filename


def setStandardItemModel(file_path):
	