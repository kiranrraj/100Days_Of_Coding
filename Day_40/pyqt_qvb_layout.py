import sys

from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout Example")
        self.resize(270, 110)
        l_out = QVBoxLayout()
        l_out.addWidget(QPushButton("Top"))
        l_out.addWidget(QPushButton("Center"))
        l_out.addWidget(QPushButton("Bottom"))
        self.setLayout(l_out)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())