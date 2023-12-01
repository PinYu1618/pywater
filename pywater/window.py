from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QStatusBar

from .ui.home import Home
from .ui.history import History
from .ui.analysis import Analysis
from .ui.settings import Settings

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyWater")
        # self.setWindowIcon(QIcon('./assets/icon.png'))
        self.setGeometry(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        # self.setFixedSize(QSize(WINDOW_WIDTH, WINDOW_HEIGHT))

        # main contents
        self.tabs = QTabWidget()
        self.tabs.addTab(Home(self.tabs), "Home")
        self.tabs.addTab(History(self.tabs), "History")
        self.tabs.addTab(Analysis(self.tabs), "Analysis")
        self.tabs.addTab(Settings(self.tabs), "Settings")
        self.setCentralWidget(self.tabs)

        # status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("PyWater v1.0")

    def onclick(self):
        print("Clicked!")
