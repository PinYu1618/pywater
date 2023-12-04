from typing import Union

from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect
from PyQt5.QtGui import QPainter, QColor, QPaintEvent
from PyQt5.QtWidgets import QWidget

X = 210
Y = 100
W = 170
H = 300
DURATION = 1500


class Glass(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        self._waterLvl = 100

        self.water = QWidget(self)
        self.water.setStyleSheet("background-color:blue;")
        self.water.setGeometry(X, Y + H - self._waterLvl, W, self._waterLvl)

        self._anim = QPropertyAnimation(self.water, b"geometry")
        self._anim.setEasingCurve(QEasingCurve.InOutCubic)
        self._anim.setEndValue(QRect(X, Y + H - 200, W, 200))
        self._anim.setDuration(DURATION)

    def setup_animation(self, lvl: int):
        self._anim.stop()
        if lvl <= H and lvl >= 0:
            self._anim.setEndValue(QRect(X, Y + H - lvl, W, lvl))
            self._anim.start()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        self.drawGlass(painter)

    def drawGlass(self, painter: QPainter):
        # Draw a simple glass cup
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(240, 240, 240))
        painter.drawRect(X, Y, W, H)

    def drawSmile(self, painter: QPainter):
        pass

    def drawUnhappy(self, painter: QPainter):
        pass
