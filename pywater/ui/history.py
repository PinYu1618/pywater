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
        grid = QGridLayout(self)

        lbox = QVBoxLayout()
        self.calendar = QCalendarWidget(self)
        self.calendar.setMouseTracking(True)
        self.calendar.selectionChanged.connect(self.calendar_date)
        self.calendar.setFixedSize(QSize(400, 300))
        self.calendar.setCursor(Qt.PointingHandCursor)
        lbox.addWidget(self.calendar)

        rbox = QFormLayout()
        lbl_water = QLabel("Water (ml)")
        self.e_water = QLineEdit(self)
        self.e_water.setReadOnly(True)
        lbl_weight = QLabel("Weight (kg)")
        self.input2 = QLineEdit(self)
        lbl_memo = QLabel("Memo")
        self.input3 = QPlainTextEdit(self)
        rbox.addRow(lbl_water, self.e_water)
        rbox.addRow(lbl_weight, self.input2)
        rbox.addRow(lbl_memo, self.input3)
        rbox.setRowWrapPolicy(QFormLayout.WrapAllRows)

        grid.addLayout(lbox, 0, 0)
        grid.addLayout(rbox, 0, 1)

        self.setLayout(grid)

    # def showDate(self, date):
    #    self.lbl.setText(date.toString())

    def calendar_date(self):
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate())

        self.label.setText("Date Is : " + date_in_string)
