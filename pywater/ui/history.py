from typing import Union

from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QCalendarWidget,
    QVBoxLayout,
    QGridLayout,
    QTableView,
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

        # model
        self.model = QSqlTableModel(self)
        self.model.setTable("records")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Date")
        self.model.setHeaderData(2, Qt.Horizontal, "Water")
        self.model.setHeaderData(3, Qt.Horizontal, "Weight")
        self.model.select()

        # view
        rbox = QVBoxLayout()
        self.lbl = QLabel("Unknown Date")
        self.lst = QTableView()
        self.lst.setModel(self.model)
        self.lst.resizeColumnsToContents()
        rbox.addWidget(self.lbl)
        rbox.addWidget(self.lst)

        grid.addLayout(lbox, 0, 0)
        grid.addLayout(rbox, 0, 1)

        self.setLayout(grid)

    # def showDate(self, date):
    #    self.lbl.setText(date.toString())

    def calendar_date(self):
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate())

        self.lbl.setText("Date Is : " + date_in_string)
