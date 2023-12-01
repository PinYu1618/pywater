from typing import Union

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QCalendarWidget,
    QVBoxLayout,
    QGridLayout,
    QLineEdit,
    QPlainTextEdit,
    QFormLayout,
)


class History(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        hbox = QGridLayout()

        lbox = QVBoxLayout()
        self.calendar = QCalendarWidget(self)
        self.calendar.setMouseTracking(True)
        self.calendar.selectionChanged.connect(self.calendar_date)
        self.calendar.setFixedSize(QSize(400, 300))
        self.calendar.setCursor(Qt.PointingHandCursor)
        lbox.addWidget(self.calendar)

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

        hbox.addLayout(lbox, 0, 0)
        hbox.addLayout(rbox, 0, 1)

        self.setLayout(hbox)

    # def showDate(self, date):
    #    self.lbl.setText(date.toString())

    def calendar_date(self):
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate())

        self.label.setText("Date Is : " + date_in_string)
