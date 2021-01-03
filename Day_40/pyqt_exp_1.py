# Title  : Pyqt5
# Author : Kiran Raj R.
# Date   : 23/11/2020

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt HQBox LAyout")
        layout = QHBoxLayout()
        layout.addWidget(QPushButton("Left"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Right"))
        self.setLayout(layout)
        print(self.children())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())