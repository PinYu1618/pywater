from typing import Union

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, Qt, QSize
from PyQt5.QtGui import QPainter, QColor, QBrush, QPalette
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDial, QGridLayout, QLabel, QFrame


class Home(QWidget):
    """
    Home page of the application, planned to be a fancy dashboard or panel
    """

    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        self._grid = QGridLayout()
        self.setLayout(self._grid)
        self.addBottle()
        self.addFire()
        self.addRecord()
        self.addVolCtrl()
        self.addBMI()
        self.addWords()

    def addBottle(self):
        anim = DrinkWaterAnim(self)
        anim.setMouseTracking(True)
        anim.setCursor(Qt.PointingHandCursor)
        self._grid.addWidget(anim, 1, 0, 7, 3)

    def addFire(self):
        fire = QLabel("(fire icon) 30 days")
        fire.setStyleSheet("border: 2px solid black;")
        self._grid.addWidget(fire, 1, 3, 2, 2)

    def addRecord(self):
        record = QLabel()
        record.setStyleSheet("border: 2px solid black;")
        self._grid.addWidget(record, 3, 3, 4, 2)

    def addVolCtrl(self):
        vol = VolumeCtrl(self)
        self._grid.addWidget(vol, 1, 5, 6, 1)

    def addBMI(self):
        bmi = QLabel("BMI: ???")
        bmi.setStyleSheet("border: 2px solid black;")
        self._grid.addWidget(bmi, 7, 3, 1, 3)

    def addWords(self):
        words = QLabel("Hello world.")
        words.setStyleSheet("border: 2px solid black;")
        self._grid.addWidget(words, 8, 0, 1, 6)


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class DrinkWaterAnim(QFrame):
    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        self.setStyleSheet("border: 2px solid black;")
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
        self.setFixedHeight(200)

    def paintEvent(self, e):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor("black"))
        brush.setStyle(Qt.SolidPattern)
        # FIXME: sizing
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

        pc = (value - vmin) / (vmax - vmin)
        n_steps_to_draw = int(pc * 5)
        padding = 5.0

        # Define our canvas.
        d_height = self.height() - (padding * 2)
        d_width = self.width() - (padding * 2)

        # Draw the bars.
        step_size = d_height / 5
        bar_height = step_size * 0.6
        bar_spacer = step_size * 0.4 / 2

        brush.setColor(QColor("red"))

        for n in range(n_steps_to_draw):
            rect = QtCore.QRectF(
                padding,
                padding + d_height - ((n + 1) * step_size) + bar_spacer,
                d_width,
                bar_height,
            )
        painter.fillRect(rect, brush)

        painter.end()

    def _trigger_refresh(self):
        self.update()


class VolumeCtrl(QFrame):
    """
    Custom Qt Widget to show a volume bar and dial.
    Intended to be used for water drinking volume control.
    """

    def __init__(self, parent=None, steps=5) -> None:
        super(VolumeCtrl, self).__init__(parent)
        self.setStyleSheet("border: 2px solid black;")
        layout = QVBoxLayout()
        self.setLayout(layout)

        # setup vbar
        self._bar = _Bar()
        layout.addWidget(self._bar)

        # setup dial
        self._dial = QDial()
        self._dial.setFixedSize(QSize(150, 150))
        self._dial.setMouseTracking(True)
        self._dial.setCursor(Qt.PointingHandCursor)
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        layout.addWidget(self._dial)

    def setBarPadding(self, i):
        self._bar._padding = int(i)
        self._bar.update()
