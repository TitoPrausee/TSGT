import sys
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt

class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(['Address', 'Value', 'Operation'])
        self.horizontalHeader().setStretchLastSection(True)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def updateTable(self, data):
        self.setRowCount(len(data))
        for i, item in enumerate(data):
            address_item = QTableWidgetItem(hex(item.address))
            value_item = QTableWidgetItem(str(item.value))
            operation_item = QTableWidgetItem(item.operation)

            self.setItem(i, 0, address_item)
            self.setItem(i, 1, value_item)
            self.setItem(i, 2, operation_item)

    def resizeColumnsToContents(self):
        for i in range(self.columnCount()):
            self.resizeColumnToContents(i)