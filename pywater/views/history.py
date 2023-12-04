from typing import Union

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QCalendarWidget,
    QGridLayout,
    QPushButton,
    QFrame,
)


class HistoryView(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None) -> None:
        super().__init__(parent)
        # layout
        ly = QGridLayout(self)
        self.setLayout(ly)

        # header
        header = QLabel("History Manager")
        header.setStyleSheet("border: 2px solid black;")
        ly.addWidget(header, 0, 0)

        # modify button
        ly.addWidget(QPushButton("Modify"), 1, 1)

        # calender
        self.calendar = QCalendarWidget(self)
        self.calendar.setMouseTracking(True)
        self.calendar.selectionChanged.connect(self.calendar_date)
        # self.calendar.setFixedSize(QSize(400, 400))
        self.calendar.setCursor(Qt.PointingHandCursor)
        ly.addWidget(self.calendar, 2, 0)

        # data
        ly.addWidget(QFrame(self), 2, 1)

        # save button
        self.btn_save = QPushButton("Save", self)
        ly.addWidget(self.btn_save, 3, 1)

    # def showDate(self, date):
    #    self.lbl.setText(date.toString())

    def calendar_date(self):
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate())

        self.lbl.setText("Date Is : " + date_in_string)
