from typing import Union

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTabWidget

from .home import HomeView
from .history import HistoryView

# from .analysis import AnalysisView


class View(QTabWidget):
    def __init__(self, parent: Union[QWidget, None] = None) -> None:
        super().__init__(parent)
        self.setStyleSheet("font-size: 20px;")
        self.home = HomeView(self)
        self.addTab(self.home, "Home")
        self.history = HistoryView(self)
        self.addTab(self.history, "History")


#       self.analysis = AnalysisView(self)
#      self.addTab(self.analysis, "Analysis")
