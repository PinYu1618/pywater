from typing import Union

from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect
from PyQt5.QtGui import QPainter, QColor, QPaintEvent
from PyQt5.QtWidgets import QWidget

X = 210
Y = 100
W = 170
H = 300
DURATION = 1300


class Glass(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        self._water = QWidget(self)
        self._water.setStyleSheet("background-color:#60a5fa;")
        self._water.setGeometry(X, Y + H, W, 0)

        self._anim = QPropertyAnimation(self._water, b"geometry")
        self._anim.setEasingCurve(QEasingCurve.InOutCubic)
        self._anim.setEndValue(QRect(X, Y + H - 200, W, 200))
        self._anim.setDuration(DURATION)

    def draw_water(self, pc: float):
        self._anim.stop()
        # clamp pc to 0~1
        pc = max(0.0, pc)
        pc = min(1.0, pc)
        lvl = round(float(H) * pc)
        self._anim.setEndValue(QRect(X, Y + H - lvl, W, lvl))
        self._anim.start()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        self._draw_glass(painter)

    # def drawSmile(self, painter: QPainter):
    #    pass

    def _draw_glass(self, painter: QPainter):
        # Draw a simple glass cup
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(240, 240, 240))
        painter.drawRect(X, Y, W, H)
