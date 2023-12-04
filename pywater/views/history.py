from typing import Union

from PyQt5.QtCore import Qt
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

        # modify button
        ly.addWidget(QPushButton("Modify"), 1, 1)

        # calender
        self.calendar = QCalendarWidget(self)
        self.calendar.setMouseTracking(True)
        self.calendar.setCursor(Qt.PointingHandCursor)
        ly.addWidget(self.calendar, 2, 0)

        # data
        fr = QFrame(self)
        form = QFormLayout()
        ly.addWidget(fr, 2, 1)
        fr.setLayout(form)
        self._lb_date = QLabel("Date: ???", fr)
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

    # def showDate(self, date):
    #    self.lbl.setText(date.toString())

    def input_water(self) -> str:
        return self._i_water.text()

    def input_height(self) -> str:
        return self._i_height.text()

    def input_weight(self) -> str:
        return self._i_weight.text()

    def set_water(self, water: int):
        self._i_water.setText(str(water))

    def set_height(self, height: int):
        self._i_height.setText(str(height))

    def set_weight(self, weight: int):
        self._i_weight.setText(str(weight))

    def selected_date(self) -> str:
        dateselected = self.calendar.selectedDate()
        return str(dateselected.toPyDate())
