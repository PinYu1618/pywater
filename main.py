from PyQt5.QtWidgets import QApplication

from pywater import app
from pywater.app import App
from pywater.window import Window


def main():
    import sys

    qt = QApplication([])
    win = Window()
    win.show()
    App(win)
    sys.exit(qt.exec_())


if __name__ == "__main__":
    app.run()
