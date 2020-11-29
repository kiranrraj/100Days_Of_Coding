import sys

from PyQt5.QtWidgets import QApplication, QCheckBox, QFormLayout, QLineEdit, QTabWidget, QVBoxLayout, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Q Tab")
        self.resize(270, 110)
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.generalTabUI(), "Primary")
        tabs.addTab(self.networkTabUI(), "Secondary")
        layout.addWidget(tabs)

    def generalTabUI(self):
        generalTab = QWidget()
        layout_1 = QFormLayout()
        layout_1.addRow("Name:", QLineEdit())
        layout_1.addRow("Position:", QLineEdit())
        layout_1.addRow("Email:", QLineEdit())
        layout = QVBoxLayout()
        layout.addLayout(layout_1)
        layout.addWidget(QCheckBox("Admin"))
        layout.addWidget(QCheckBox("DB Admin"))
        generalTab.setLayout(layout)
        return generalTab

    def networkTabUI(self):
        networkTab = QWidget()
        layout = QVBoxLayout()
        layout_1 = QFormLayout()
        layout_1.addRow("Nick Name:", QLineEdit())
        layout_1.addRow("Nationality:", QLineEdit())
        layout_1.addRow("State:", QLineEdit())
        layout.addLayout(layout_1)
        layout.addWidget(QCheckBox("On site"))
        layout.addWidget(QCheckBox("Contract"))
        networkTab.setLayout(layout)
        return networkTab

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())