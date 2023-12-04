from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QStatusBar

from .views import View
from .models.encourage import encourage
from .models.bmi import BMI
from .models.stat import Stat
from .models.db import DbHandler
from .presenter import Presenter

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
DB = "history.csv"


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyWater")
        # self.setWindowIcon(QIcon('./assets/icon.png'))
        self.setGeometry(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setFixedSize(QSize(WINDOW_WIDTH, WINDOW_HEIGHT))

        # main contents
        view = View(self)
        self.presenter = Presenter(view, Stat(water=100), DbHandler(DB), encourage, BMI)
        self.setCentralWidget(view)

        # status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("PyWater v1.0")


def run():
    import sys

    # show main app window
    qt = QApplication([])
    win = App()
    win.show()
    sys.exit(qt.exec_())
