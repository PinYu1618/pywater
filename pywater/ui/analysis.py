from typing import Union

from PyQt5.QtWidgets import QWidget


class Analysis(QWidget):
    def __init__(self, parent: Union[QWidget, None] = None):
        super().__init__(parent)
