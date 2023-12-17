from typing import Union

from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QPushButton,
    QLineEdit,
    QRadioButton,
    QFormLayout,
)

from .widgets.volume import VolumeCtrl
from .widgets.glass import Glass

# styles
BOX = "border: 2px solid black;"
MSG_LBL = "font-size: 24px; padding: 4px;" + BOX
WATER_LBL = "text-align: center; font-size: 20px; padding: 6px;" + BOX


class HomeView(QWidget):
    """
    Home page of the application, planned to be a fancy dashboard or panel
    """

    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        self._grid = QGridLayout()
        self.setLayout(self._grid)
        self.setStyleSheet("QFrame{border: 2px solid black;}")
        self._create_glass()
        self._create_water()
        self._create_form()
        self._create_volume()
        self._create_bmi()
        self._create_msg()

    def height_text(self) -> str:
        return self._i_height.text()

    def weight_text(self) -> str:
        return self._i_weight.text()

    def set_height(self, h: float):
        self._i_height.setText(str(h))

    def set_weight(self, w: float):
        self._i_weight.setText(str(w))

    def show_water_label(self, cur: float, mx: float) -> None:
        self._lbl_water.setText(
            "Water: " + str(round(cur)) + "/" + str(round(mx)) + " (ml)"
        )

    def print_msg(self, msg: str):
        """print out message to message box"""
        self._msg.setText(msg)

    def _create_glass(self):
        # outer box
        fr = QFrame(self)
        fr_ly = QVBoxLayout(fr)
        fr.setLayout(fr_ly)

        self.glass = Glass(fr)
        fr_ly.addWidget(self.glass)

        btns_ly = QHBoxLayout()
        self.btnsub = QPushButton("-100ml")
        self.btn100 = QPushButton("+100ml")
        self.btn200 = QPushButton("+200ml")
        self.btn500 = QPushButton("+500ml")
        btns_ly.addWidget(self.btnsub)
        btns_ly.addWidget(self.btn100)
        btns_ly.addWidget(self.btn200)
        btns_ly.addWidget(self.btn500)

        fr_ly.addLayout(btns_ly)

        self._grid.addWidget(fr, 1, 0, 7, 3)

    def _create_water(self):
        self._lbl_water = QLabel("Water: ?/?")
        self._lbl_water.setStyleSheet(WATER_LBL)
        self._grid.addWidget(self._lbl_water, 1, 3, 2, 2)

    def _create_volume(self):
        # add volume control box
        vol = VolumeCtrl(self)
        vol.setStyleSheet("border: 2px solid black;")
        self._grid.addWidget(vol, 1, 5, 6, 1)

    def _create_form(self):
        # add form for input height and weight
        fr = QFrame(self)
        ly = QFormLayout()
        ly.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapAllRows)
        fr.setLayout(ly)
        self._i_height = QLineEdit(fr)
        self._i_weight = QLineEdit(fr)
        self.btn_bmi = QPushButton("Submit", fr)
        ly.addRow(QLabel("Height:"), self._i_height)
        ly.addRow(QLabel("Weight:"), self._i_weight)
        ly.addRow(self.btn_bmi)
        self._grid.addWidget(fr, 3, 3, 4, 2)

    def _create_bmi(self):
        # add bmi status display
        fr = QFrame(self)
        ly = QHBoxLayout()
        fr.setLayout(ly)
        ly.addWidget(QLabel("BMI", self))
        ly.addStretch(2)
        self._r_underweight = QRadioButton(self)
        ly.addWidget(self._r_underweight)
        ly.addStretch(1)
        self._r_normal = QRadioButton(self)
        self._r_normal.setChecked(True)
        ly.addWidget(self._r_normal)
        ly.addStretch(1)
        self._r_overweight = QRadioButton(self)
        ly.addWidget(self._r_overweight)
        ly.addStretch(1)
        self._grid.addWidget(fr, 7, 3, 1, 3)

    def _create_msg(self):
        # add message box
        self._msg = QLabel()
        self._msg.setStyleSheet(MSG_LBL)
        self._grid.addWidget(self._msg, 8, 0, 1, 6)
