import typing
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QCalendarWidget,
)

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300


class CalenderTab(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.selectionChanged.connect(self.calendar_date)

        self.label = QLabel("Hello")
        self.label.setFont(QFont("Sanserif", 15))
        self.label.setStyleSheet("color:red")

        hbox.addWidget(self.calendar)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def calendar_date(self):
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate())

        self.label.setText("Date Is : " + date_in_string)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyWater")
        # self.setWindowIcon(QIcon('./assets/icon.png'))
        self.setGeometry(300, 300, WINDOW_WIDTH, WINDOW_HEIGHT)

        tab1 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, "Tab1")
        tabs.addTab(CalenderTab(), "History")

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        # self.btn = QPushButton("+100ml")
        # self.setCentralWidget(self.btn)

    def onclick(self):
        print("Clicked!")


class App:
    def __init__(self, window: Window):
        self.win = window
        self.count = 0
        self.connect_signals()

    def connect_signals(self):
        self.win.btn.clicked.connect(self.win.onclick)

    def inc(self):
        self.count += 1
        self.win.onclick()


def main():
    import sys

    qt = QApplication([])
    win = Window()
    win.show()
    # App(win)
    sys.exit(qt.exec_())


if __name__ == "__main__":
    main()
