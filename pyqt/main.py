import sys
from PyQt5.QtWidgets import QApplication
from gui import GUI
from node import receive_data_from_memory_reader

def main():
    app = QApplication(sys.argv)

    gui = GUI()
    gui.show()

    # Start receiving data from the memory reader
    receive_data_from_memory_reader(gui.updateGraph, gui.updateTable)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()