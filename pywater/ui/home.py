from typing import Union

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont, QPainter, QColor, QBrush, QPalette
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDial, QGridLayout


class Home(QWidget):
    """
    Home page of the application, planned to be a fancy dashboard or panel
    """

    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        grid = QGridLayout()

        anim = DrinkWaterAnim()
        anim.setMouseTracking(True)
        anim.setCursor(Qt.PointingHandCursor)
        words = Color("green")
        dt = Color("blue")
        fire = Color("yellow")
        vol = VolumeBox()
        bmi = Color("purple")

        grid.addWidget(anim, 1, 0, 7, 3)
        grid.addWidget(words, 8, 0, 1, 6)
        grid.addWidget(dt, 1, 3, 2, 2)
        grid.addWidget(fire, 3, 3, 4, 2)
        grid.addWidget(vol, 1, 5, 6, 1)
        grid.addWidget(bmi, 7, 3, 1, 3)

        self.setLayout(grid)

    def sliderMoved(self):
        print("Dial value = %i" % (self.dial.value()))


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class DrinkWaterAnim(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        self.waterLevel = 0
        # self.initAnimation()

    def initAnimation(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)  # Adjust the speed of animation by changing the interval

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawGlass(painter)
        self.drawWater(painter)

    def drawGlass(self, painter: QPainter):
        # Draw a simple glass cup
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(250, 250, 250))
        painter.drawRect(180, 70, 170, 400)

    def drawWater(self, painter: QPainter):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 119, 190))  # Adjust color as needed

        # Calculate the water level within the glass
        waterHeight = 300 - self.waterLevel
        if waterHeight > 0:
            painter.drawRect(160, 300 - self.waterLevel, 80, self.waterLevel)

        # Increase the water level
        self.waterLevel += 5
        if self.waterLevel > 300:
            self.waterLevel = 0

    def drawSmile(self, painter: QPainter):
        pass

    def drawUnhappy(self, painter: QPainter):
        pass


class _Bar(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
