from typing import Union

from PyQt5 import QtCore
from PyQt5.QtCore import (
    Qt,
    QSize,
)
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QDial,
    QFrame,
)


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
