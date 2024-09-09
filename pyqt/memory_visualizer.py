import sys
from PyQt5.QtWidgets import QApplication
from gui import GUI
from node import receive_data_from_memory_reader

class MemoryVisualizer:
    def __init__(self):
        self.gui = GUI()
        self.gui.show()

    def start_visualization(self):
        receive_data_from_memory_reader(self.gui.updateGraph, self.gui.updateTable)

def main():
    app = QApplication(sys.argv)
    visualizer = MemoryVisualizer()
    visualizer.start_visualization()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()