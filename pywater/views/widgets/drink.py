from typing import Union

from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect, pyqtSlot
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

        self._anim = QPropertyAnimation(self.water, b"geometry")
        self._anim.setEasingCurve(QEasingCurve.InOutCubic)
        self._anim.setEndValue(QRect(GLASS_X, GLASS_Y + GLASS_H - 200, GLASS_W, 200))
        self._anim.setDuration(DURATION)

    @pyqtSlot(float)
    def setup_animation(self, lvl: float):
        self._anim.stop()
        if lvl <= float(GLASS_H) and lvl >= 0.0:
            self._anim.setEndValue(
                QRect(GLASS_X, GLASS_Y + GLASS_H - lvl, GLASS_W, lvl)
            )
            self._anim.start()

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
