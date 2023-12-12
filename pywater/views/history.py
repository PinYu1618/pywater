from typing import Union

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QCalendarWidget,
    QGridLayout,
    QPushButton,
    QFrame,
    QFormLayout,
    QLineEdit,
)

from ..models.stat import Record


class HistoryView(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None) -> None:
        super().__init__(parent)
        # layout
        ly = QGridLayout(self)
        self.setLayout(ly)

        # header
        header = QLabel("History Manager")
        header.setStyleSheet("border: 2px solid black; font: bold 24px; padding: 6px;")
        ly.addWidget(header, 0, 0, 1, 2)

        # calender
        today = QDate().currentDate()
        self.calendar = QCalendarWidget(self)
        self.calendar.setMouseTracking(True)
        self.calendar.setCursor(Qt.PointingHandCursor)
        self.calendar.setSelectedDate(today)
        ly.addWidget(self.calendar, 2, 0, 2, 1)

        # data
        fr = QFrame(self)
        form = QFormLayout()
        ly.addWidget(fr, 2, 1)
        fr.setLayout(form)
        self._lb_date = QLabel("Date: ???", fr)
        self.show_date(today)
        self._i_water = QLineEdit(fr)
        self._i_height = QLineEdit(fr)
        self._i_weight = QLineEdit(fr)
        form.addRow(self._lb_date)
        form.addRow(QLabel("", fr))
        form.addRow(QLabel("Water (ml):"), self._i_water)
        form.addRow(QLabel("Height (cm):"), self._i_height)
        form.addRow(QLabel("Weight (kg):"), self._i_weight)

        # save button
        self.btn_save = QPushButton("Save", self)
        ly.addWidget(self.btn_save, 3, 1)

        # status
        self.lbl_status = QLabel("", self)
        ly.addWidget(self.lbl_status, 4, 0)

    def input_water(self) -> str:
        return self._i_water.text()

    def input_height(self) -> str:
        return self._i_height.text()

    def input_weight(self) -> str:
        return self._i_weight.text()

    def selected_date(self):
        dateselected = self.calendar.selectedDate()
        return dateselected.toPyDate()

    def show_date(self, date: QDate):
        self._lb_date.setText("Date: " + date.toString())

    def show_record(self, record: Record):
        self._i_height.setText(str(record.height))
        self._i_weight.setText(str(record.weight))
        self._i_water.setText(str(record.water))
