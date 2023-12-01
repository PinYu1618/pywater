import typing
from apscheduler.schedulers.blocking import BlockingScheduler
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon, QFont, QPainter, QColor, QPen, QBrush
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QMainWindow,
    QTabWidget,
    QHBoxLayout,
    QStatusBar,
    QCalendarWidget,
    QVBoxLayout,
    QDial,
    QSizePolicy,
)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300


class _Bar(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

    def sizeHint(self):
        return QtCore.QSize(40, 120)

    def paintEvent(self, e):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor("black"))
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        # Get current state.
        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        pen = painter.pen()
        pen.setColor(QColor("red"))
        painter.setPen(pen)

        font = painter.font()
        font.setFamily("Times")
        font.setPointSize(18)
        painter.setFont(font)

        painter.drawText(25, 25, "{}-->{}<--{}".format(vmin, value, vmax))
        painter.end()

    def _trigger_refresh(self):
        self.update()


class VolumeBox(QWidget):
    """
    Custom Qt Widget to show a volume bar and dial.
    Intended to be used for water drinking volume control.
    """

    def __init__(self, steps=5) -> None:
        super(VolumeBox, self).__init__()
        layout = QVBoxLayout()
        self._bar = _Bar()
        layout.addWidget(self._bar)

        self._dial = QDial()
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        layout.addWidget(self._dial)

        self.setLayout(layout)

    def setBarPadding(self, i):
        self._bar._padding = int(i)
        self._bar.update()


class Home(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.vol = VolumeBox()
        layout.addWidget(self.vol)

        self.setLayout(layout)

    def sliderMoved(self):
        print("Dial value = %i" % (self.dial.value()))


class Analysis(QWidget):
    def __init__(self):
        super().__init__()


class Settings(QWidget):
    def __init__(self):
        super().__init__()


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

    def drawGlass(self, painter: QPainter):
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


class History(QWidget):
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


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyWater")
        # self.setWindowIcon(QIcon('./assets/icon.png'))
        self.setGeometry(300, 300, WINDOW_WIDTH, WINDOW_HEIGHT)

        # main contents
        tabs = QTabWidget()
        tabs.addTab(Home(), "Home")
        tabs.addTab(History(), "History")
        tabs.addTab(Analysis(), "Analysis")
        tabs.addTab(Settings(), "Settings")
        self.setCentralWidget(tabs)

        # status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("PyWater v1.0")

    def onclick(self):
        print("Clicked!")
