from typing import Union

from PyQt5 import QtCore
from PyQt5.QtCore import (
    QTimer,
    Qt,
    QSize,
    QPropertyAnimation,
    QPoint,
    QEasingCurve,
    QRect,
)
from PyQt5.QtGui import QPainter, QColor, QBrush, QPaintEvent
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QDial,
    QGridLayout,
    QLabel,
    QFrame,
    QPushButton,
)


class HomeView(QWidget):
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
        # outer box
        fr = QFrame(self)
        fr.setStyleSheet("QFrame{border: 2px solid black;}")
        fr_ly = QVBoxLayout(fr)
        fr.setLayout(fr_ly)

        glass = DrinkWaterAnim(fr)
        fr_ly.addWidget(glass)

        btns_ly = QHBoxLayout()
        btns_ly.addWidget(QPushButton("-100ml"))
        btns_ly.addWidget(QPushButton("+100ml"))
        btns_ly.addWidget(QPushButton("+200ml"))
        btns_ly.addWidget(QPushButton("+500ml"))

        fr_ly.addLayout(btns_ly)

        self._grid.addWidget(fr, 1, 0, 7, 3)

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
        vol.setStyleSheet("border: 2px solid black;")
        self._grid.addWidget(vol, 1, 5, 6, 1)

    def addBMI(self):
        bmi = QLabel("BMI: ???")
        bmi.setStyleSheet("border: 2px solid black;")
        self._grid.addWidget(bmi, 7, 3, 1, 3)

    def addWords(self):
        words = QLabel("Hello world.")
        words.setStyleSheet("border: 2px solid black;")
        self._grid.addWidget(words, 8, 0, 1, 6)


class DrinkWaterAnim(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        self._waterLvl = 100

        self.water = QWidget(self)
        self.water.setStyleSheet("background-color:blue;")
        self.water.setGeometry(210, 100 + 300 - self._waterLvl, 170, self._waterLvl)

        self.anim = QPropertyAnimation(self.water, b"geometry")
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim.setEndValue(QRect(210, 100 + 300 - 200, 170, 200))
        self.anim.setDuration(1500)
        self.anim.start()

    def initAnimation(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(100)  # Adjust the speed of animation by changing the interval

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        self.drawGlass(painter)

    def drawGlass(self, painter: QPainter):
        # Draw a simple glass cup
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(240, 240, 240))
        painter.drawRect(210, 100, 170, 300)

    def drawSmile(self, painter: QPainter):
        pass

    def drawUnhappy(self, painter: QPainter):
        pass


class VolumeCtrl(QFrame):
    """
    Custom Qt Widget to show a volume bar and dial.
    Intended to be used for water drinking volume control.
    """

    def __init__(self, parent: Union[QWidget, None] = None, steps=5) -> None:
        super(VolumeCtrl, self).__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        # setup vbar
        self._bar = _Bar(self)
        layout.addWidget(self._bar)

        # setup dial
        self._dial = QDial(self)
        self._dial.setFixedSize(QSize(150, 150))
        self._dial.setMouseTracking(True)
        self._dial.setCursor(Qt.PointingHandCursor)
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        layout.addWidget(self._dial)

    def setBarPadding(self, i):
        self._bar._padding = int(i)
        self._bar.update()


class _Bar(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        self.setFixedHeight(200)

    def paintEvent(self, e):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor("black"))
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, self.width(), self.height())
        painter.fillRect(rect, brush)

        # Get current state.
        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        pen = painter.pen()
        pen.setColor(QColor("red"))
        painter.setPen(pen)

        pc = (value - vmin) / (vmax - vmin)
        n_steps_to_draw = int(pc * 5)
        padding = 5.0

        # Define our canvas.
        d_height = self.height() - (padding * 2)
        d_width = self.width() - (padding * 2)

        # Draw the bars.
        step_size = d_height / 5.0
        bar_height = step_size * 0.6
        bar_spacer = step_size * 0.4 / 2.0

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
