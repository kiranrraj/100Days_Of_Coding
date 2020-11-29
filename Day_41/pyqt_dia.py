import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog Box")
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Email:", QLineEdit())
        btnBox = QDialogButtonBox()
        btnBox.setStandardButtons( QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        dlgLayout.addLayout(formLayout)
        dlgLayout.addWidget(btnBox)
        self.setLayout(dlgLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())