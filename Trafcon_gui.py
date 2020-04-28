from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
import sys
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "TrafCon"
        self.top = 100
        self.left = 170
        self.width = 1280
        self.height = 720
        self.InitWindow()
        self.CreateMenu()

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