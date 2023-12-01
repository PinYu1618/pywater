import typing
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon, QFont, QPainter, QColor, QPen
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


class DrinkingWaterAnimation(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initAnimation()

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Drinking Water Animation")
        self.show()

    def initAnimation(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)  # Adjust the speed of animation by changing the interval

        self.waterLevel = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawGlass(painter)
        self.drawWater(painter)
        self.drawFace(painter)

    def drawGlass(self, painter):
        # Draw a simple glass cup
        painter.setRenderHint(QPainter.Antialiasing)
        pen = painter.pen()
        pen.setColor(QColor(0, 0, 0))  # Black color
        pen.setWidth(2)
        painter.setPen(pen)

        brush = painter.brush()
        # brush.setStyle(Qt.NoBrush)
        painter.setBrush(brush)

        painter.drawEllipse(150, 200, 100, 30)
        painter.drawLine(150, 215, 100, 300)
        painter.drawLine(250, 215, 300, 300)
        painter.drawLine(100, 300, 300, 300)

    def drawWater(self, painter):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 119, 190))  # Adjust color as needed

        # Calculate the water level within the glass
        waterHeight = 300 - self.waterLevel
        if waterHeight > 0:
            painter.drawRect(160, 300 - self.waterLevel, 80, self.waterLevel)

        # Draw a face based on water level
        self.drawFace(painter)

        # Increase the water level
        self.waterLevel += 5
        if self.waterLevel > 300:
            self.waterLevel = 0

    def drawFace(self, painter):
        # Draw a smiley face or an unhappy face based on water level
        if self.waterLevel > 200:  # Sufficient water, draw a smiley face
            painter.setRenderHint(QPainter.Antialiasing)
            pen = painter.pen()
            pen.setColor(QColor(0, 0, 0))  # Black color
            painter.setPen(pen)

            font = QFont("Arial", 16, QFont.Bold)
            painter.setFont(font)
            painter.drawText(185, 250, "😊")  # Smiley face emoji
        else:  # Low water level, draw an unhappy face
            painter.setRenderHint(QPainter.Antialiasing)
            pen = painter.pen()
            pen.setColor(QColor(0, 0, 0))  # Black color
            painter.setPen(pen)

            font = QFont("Arial", 16, QFont.Bold)
            painter.setFont(font)
            painter.drawText(185, 250, "☹️")  # Unhappy face emoji


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

    # def showDate(self, date):
    #    self.lbl.setText(date.toString())

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
        tab3 = QWidget()
        tab4 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, "Tab1")
        tabs.addTab(CalenderTab(), "History")
        tabs.addTab(tab3, "Analysis")
        tabs.addTab(tab4, "Settings")

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
    # win = Window()
    # win.show()
    anim = DrinkingWaterAnimation()
    # App(win)
    sys.exit(qt.exec_())


if __name__ == "__main__":
    main()
