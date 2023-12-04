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
        self.water_level = 100

        self._water = QWidget(self)
        self._water.setStyleSheet("background-color:blue;")
        self._water.setGeometry(X, Y + H - self.water_level, W, self.water_level)

        self._anim = QPropertyAnimation(self._water, b"geometry")
        self._anim.setEasingCurve(QEasingCurve.InOutCubic)
        self._anim.setEndValue(QRect(X, Y + H - 200, W, 200))
        self._anim.setDuration(DURATION)

    def update_water(self, lvl: int):
        self._anim.stop()
        if lvl <= H and lvl >= 0:
            self.water_level = lvl
            self._anim.setEndValue(QRect(X, Y + H - lvl, W, lvl))
            self._anim.start()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        self._draw_glass(painter)

    def drawSmile(self, painter: QPainter):
        pass

    def drawUnhappy(self, painter: QPainter):
        pass

    def _draw_glass(self, painter: QPainter):
        # Draw a simple glass cup
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(240, 240, 240))
        painter.drawRect(X, Y, W, H)
