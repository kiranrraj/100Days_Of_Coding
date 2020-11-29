import sys

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Complex Layout")
        layout_1 = QVBoxLayout()
        layout_2 = QFormLayout()
        layout_2.addRow("Name:", QLineEdit())
        layout_2.addRow("Place:", QLineEdit())
        layout_2.addRow("Nationality:", QLineEdit())
        cb_layout = QVBoxLayout()
        cb_layout.addWidget(QCheckBox("Checkbox option 1"))
        cb_layout.addWidget(QCheckBox("Checkbox option 2"))
        cb_layout.addWidget(QCheckBox("Checkbox option 3"))
        layout_1.addLayout(layout_2)
        layout_1.addLayout(cb_layout)
        self.setLayout(layout_1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())