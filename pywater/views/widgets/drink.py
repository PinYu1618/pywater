from typing import Union

from PyQt5.QtCore import (
    QTimer,
    QPropertyAnimation,
    QEasingCurve,
    QRect,
)
from PyQt5.QtGui import QPainter, QColor, QPaintEvent
from PyQt5.QtWidgets import QWidget

GLASS_X = 210
GLASS_Y = 100
GLASS_W = 170
GLASS_H = 300
DURATION = 1500


class DrinkWaterAnim(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        self._waterLvl = 100

        self.water = QWidget(self)
        self.water.setStyleSheet("background-color:blue;")
        self.water.setGeometry(
            GLASS_X, GLASS_Y + GLASS_H - self._waterLvl, GLASS_W, self._waterLvl
        )

        self.anim = QPropertyAnimation(self.water, b"geometry")
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim.setEndValue(QRect(GLASS_X, GLASS_Y + GLASS_H - 200, GLASS_W, 200))
        self.anim.setDuration(DURATION)
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
        painter.drawRect(GLASS_X, GLASS_Y, GLASS_W, GLASS_H)

    def drawSmile(self, painter: QPainter):
        pass

    def drawUnhappy(self, painter: QPainter):
        pass
