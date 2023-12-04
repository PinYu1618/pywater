from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QStatusBar

from .views.home import HomeView
from .views.history import HistoryView
from .views.analysis import AnalysisView
from .views.settings import SettingsView
from .presenters.home import HomePresenter
from .models.encourage import encourage

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyWater")
        # self.setWindowIcon(QIcon('./assets/icon.png'))
        self.setGeometry(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setFixedSize(QSize(WINDOW_WIDTH, WINDOW_HEIGHT))

        # main contents
        tabs = QTabWidget(self)
        v_home = HomeView(tabs)
        v_history = HistoryView(tabs)
        v_analysis = AnalysisView(tabs)
        v_settings = SettingsView(tabs)
        tabs.addTab(v_home, "Home")
        tabs.addTab(v_history, "History")
        tabs.addTab(v_analysis, "Analysis")
        tabs.addTab(v_settings, "Settings")
        self.home = HomePresenter(v_home, encourage)
        self.setCentralWidget(tabs)

        # status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("PyWater v1.0")

    def onclick(self):
        print("Clicked!")
