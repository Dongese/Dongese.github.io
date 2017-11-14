#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author: Dong Ren 
last edited: Nov 2017
"""

import sys
from PySide import QtGui,QtCore


class HtmlEngine(QtGui.QMainWindow):

    def __init__(self):
        super(HtmlEngine, self).__init__()
        self.actions = Action()
        self.mainWidgets()


    def mainWidgets(self):
        # statusbar
        self.statusBar()
        # menubar
        self._menuBar()
        #toobar
        self._toolBar()

        #Grid layout
        grid = QtGui.QGridLayout()
        grid.addWidget(self._treeView(),0,1)
        grid.addWidget(self._listView(),0,0)

        #main layout
        main_widget = QtGui.QWidget()
        main_widget.setLayout(grid)
        self.setCentralWidget(main_widget)

        #get/set the size of mainwindow.
        window_width, window_height = QtGui.QDesktopWidget().screenGeometry().width()/2, QtGui.QDesktopWidget().screenGeometry().height()/2
        self.setGeometry(300, 300, window_width, window_height)
        #set the title of window
        self.setWindowTitle('HtmlEngine')
        #let's play
        self.show()

    #set meanuBar
    def _menuBar(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(self.actions.exitAction(self))

    #set toolBar
    def _toolBar(self):
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(self.actions.exitAction(self))

    #set treeView
    def _treeView(self):
        treeView = QtGui.QTreeView()
        model = QtGui.QFileSystemModel()
        model.setRootPath(QtCore.QDir.currentPath())
        treeView.setModel(model)
        return treeView

    def _listView(self):
        listView = QtGui.QListView()
        model = QtGui.QStandardItemModel()
        listView.setModel(model)
        return listView


'''
The QStandartItemModel of ListView and TreeView will be generated 
by the class Model.
'''
class Model(object):
    def __init__(self):
        pass

    def listViewModel(self):
        pass







'''
I put all of Action here.
'''
class Action:
    def __int__(self):
        pass

    def exitAction(self,frame):
        exitAction = QtGui.QAction('Exit', frame)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(frame.close)
        return exitAction






def main():
    app = QtGui.QApplication(sys.argv)
    ex = HtmlEngine()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()