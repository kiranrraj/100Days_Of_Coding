# Title  : Pyqt5
# Author : Kiran Raj R.
# Date   : 23/11/2020

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")
        l_out = QGridLayout()
        l_out.addWidget(QPushButton("Row 1 : Column 1"), 0, 0)
        l_out.addWidget(QPushButton("Row 1 : Column 2"), 0, 1)
        l_out.addWidget(QPushButton("Row 1 : Column 3"), 0, 2)
        l_out.addWidget(QPushButton("Row 2 : Column 1"), 1, 0)
        l_out.addWidget(QPushButton("Row 2 : Column 2"), 1, 1)
        l_out.addWidget(QPushButton("Row 2 : Column 3"), 1, 2)
        l_out.addWidget(QPushButton("Row 3 : Column 1"), 2, 0)
        l_out.addWidget(QPushButton("Row 3 : Column 2"), 2, 1)
        l_out.addWidget(QPushButton("Row 3 : Column 3"), 2, 2)
        self.setLayout(l_out)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())