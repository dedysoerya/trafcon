from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QHBoxLayout, QSplitter, QFrame, QLineEdit, QListWidget, QTextBrowser
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.groupsList = QListWidget() 
        self.messagesList = QListWidget() 
        self.messageView = QTextBrowser()

        self.title = "TrafCon"
        self.top = 100
        self.left = 170
        self.width = 1280
        self.height = 720
        
        self.InitWindow()
        self.Splitter()
        self.CreateMenu()

        self.messageSplitter = QSplitter(Qt.Vertical)
        self.messageSplitter.addWidget(self.messagesList)
        self.messageSplitter.addWidget(self.messageView)
        self.mainSplitter = QSplitter(Qt.Horizontal)
        self.mainSplitter.addWidget(self.groupsList)
        self.mainSplitter.addWidget(self.messageSplitter)
        self.setCentralWidget(self.mainSplitter)

    def Splitter(self):
        hbox = QHBoxLayout()
        left = QFrame()
        left.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.setStyleSheet('background-color:red')
        lineedit = QLineEdit()
        lineedit.setStyleSheet('background-color:green')
        splitter1.addWidget(left)
        splitter1.addWidget(lineedit)
        splitter1.setSizes([200,200])
        spliiter2 = QSplitter(Qt.Vertical)
        spliiter2.addWidget(splitter1)
        spliiter2.addWidget(bottom)
        spliiter2.setStyleSheet('background-color:yellow')
        hbox.addWidget(spliiter2)
        self.setLayout(hbox)

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("File/dishub-png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def CreateMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')
        cameraAction = QAction(QIcon("File/camera-create@3x.png"), 'Create new camera', self)
        cameraAction.setShortcut("Ctrl+N")
        fileMenu.addAction(cameraAction)
        settingAction = QAction(QIcon("File/settings@3x.png"), 'Setting', self)
        settingAction.setShortcut("Ctrl+C")
        fileMenu.addAction(settingAction)
        gridAction = QAction(QIcon("File/blocks@3x.png"), 'Grid', self)
        gridAction.setShortcut("Ctrl+G")
        fileMenu.addAction(gridAction)
        refreshAction = QAction(QIcon("File/repeat@3x.png"), 'Refresh', self)
        refreshAction.setShortcut("Ctrl+R")
        fileMenu.addAction(refreshAction)
        helpAction = QAction(QIcon("File/help.png"), 'Help', self)
        helpAction.setShortcut("Ctrl+H")
        helpMenu.addAction(helpAction)
        exiteAction = QAction(QIcon("File/exit.png"), 'Exit', self)
        exiteAction.setShortcut("Ctrl+E")
        exiteAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exiteAction)

        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(cameraAction)
        self.toolbar.addAction(settingAction)
        self.toolbar.addAction(gridAction)
        self.toolbar.addAction(refreshAction)
        self.toolbar.addAction(helpAction)
        self.toolbar.addAction(exiteAction)

    def exitWindow(self):
        self.close()
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())