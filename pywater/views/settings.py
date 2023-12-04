from typing import Union

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QFormLayout,
)


class SettingsView(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        rbox = QFormLayout()
        self.label = QLabel("Hello")
        self.input1 = QLineEdit(self)
        self.lbl2 = QLabel("Hello")
        self.input2 = QLineEdit(self)
        self.label3 = QLabel("CCC")
        self.input3 = QPlainTextEdit(self)
        rbox.addRow(self.label, self.input1)
        rbox.addRow(self.lbl2, self.input2)
        rbox.addRow(self.label3, self.input3)
        rbox.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.setLayout(rbox)
