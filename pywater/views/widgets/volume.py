from typing import Union

from PyQt5.QtCore import Qt, QSize, QRect, QRectF
from PyQt5.QtGui import QPainter, QColor, QBrush, QPaintEvent
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QDial,
    QFrame,
)

BAR_HEIGHT = 200


class VolumeCtrl(QFrame):
    """
    Custom Qt Widget to show a volume bar and dial.
    Intended to be used for water drinking volume control.
    """

    def __init__(self, parent: Union[QWidget, None] = None, steps: int = 5) -> None:
        super(VolumeCtrl, self).__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        # setup vbar
        self._bar = _Bar(steps, self)
        layout.addWidget(self._bar)

        # setup dial
        self._dial = QDial(self)
        self._dial.setFixedSize(QSize(150, 150))
        self._dial.setMouseTracking(True)
        self._dial.setCursor(Qt.PointingHandCursor)  # type: ignore
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        layout.addWidget(self._dial)


class _Bar(QWidget):
    def __init__(self, steps: int, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        self._steps = steps
        self.setFixedHeight(BAR_HEIGHT)

    def paintEvent(self, e: QPaintEvent):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor("black"))
        brush.setStyle(Qt.SolidPattern)  # type: ignore
        rect = QRect(0, 0, self.width(), self.height())
        painter.fillRect(rect, brush)

        # Get current state.
        dial = self.parent()._dial
        vmin, vmax = dial.minimum(), dial.maximum()
        value = dial.value()

        pen = painter.pen()
        pen.setColor(QColor("#60a5fa"))
        painter.setPen(pen)

        pc = (value - vmin) / (vmax - vmin)
        steps = int(pc * self._steps)
        pad = 5.0

        # Define our canvas.
        d_h = self.height() - (pad * 2)
        d_w = self.width() - (pad * 2)

        # Draw the bars.
        step_h = d_h / float(self._steps)
        bar_h = step_h * 0.6
        bar_spacer = step_h * 0.4 / 2.0

        brush.setColor(QColor("#60a5fa"))

        for n in range(steps):
            rect = QRectF(
                pad,
                pad + d_h - ((n + 1) * step_h) + bar_spacer,
                d_w,
                bar_h,
            )
            painter.fillRect(rect, brush)

        painter.end()

    def _trigger_refresh(self):
        self.update()
