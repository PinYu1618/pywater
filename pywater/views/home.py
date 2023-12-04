from typing import Union

from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QPushButton,
)

from .widgets.volume import VolumeCtrl
from .widgets.glass import Glass


class HomeView(QWidget):
    """
    Home page of the application, planned to be a fancy dashboard or panel
    """

    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
        self._grid = QGridLayout()
        self.setLayout(self._grid)
        self.setStyleSheet("QFrame{border: 2px solid black;}")
        self.addBottle()
        self.addFire()
        self.addRecord()
        self.addVolCtrl()
        self.addBMI()
        self.addWords()

    def addBottle(self):
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
