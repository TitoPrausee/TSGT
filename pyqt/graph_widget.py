import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QBrush

class GraphWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Memory Graph')

        self.graphScene = QGraphicsScene()
        self.graphView = QGraphicsView(self.graphScene)
        self.graphView.setRenderHint(QPainter.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(self.graphView)
        self.setLayout(layout)

    def drawGraph(self, data):
        self.graphScene.clear()

        pen = QPen(Qt.black, 2)
        brush = QBrush(Qt.NoBrush)

        for i, point in enumerate(data):
            x = i * 10
            y = 200 - point.value
            self.graphScene.addEllipse(x, y, 5, 5, pen, brush)

        self.graphView.update()

class GraphNode:
    def __init__(self, value):
        self.value = value