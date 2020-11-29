import sys

from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QLabel,
    QLineEdit,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Q Form")
        self.resize(270, 110)
        layout = QFormLayout()
        layout.addRow("First Name:", QLineEdit())
        layout.addRow("Last Name:", QLineEdit())
        emailLabel = QLabel("Email:")
        layout.addRow(emailLabel, QLineEdit())
        layout.addRow("Place:", QLineEdit())
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())