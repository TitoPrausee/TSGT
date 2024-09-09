import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from .graph_widget import GraphWidget
from .table_widget import TableWidget
from pyqt.graph_widget import GraphWidget

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Memory Hacking Tool')

        self.createCentralWidget()
        self.createMenu()

    def createCentralWidget(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.graph_widget = GraphWidget()
        layout.addWidget(self.graph_widget)

        self.table_widget = TableWidget()
        layout.addWidget(self.table_widget)

    def createMenu(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu('File')
        file_menu.addAction('Open', self.openFile)
        file_menu.addAction('Save', self.saveFile)

        view_menu = menubar.addMenu('View')
        view_menu.addAction('Refresh', self.refreshView)

    def openFile(self):
        # TO DO: implement file opening functionality
        pass

    def saveFile(self):
        # TO DO: implement file saving functionality
        pass

    def refreshView(self):
        # TO DO: implement view refreshing functionality
        pass

    def updateGraph(self, data):
        self.graph_widget.drawGraph(data)

    def updateTable(self, data):
        self.table_widget.updateTable(data)