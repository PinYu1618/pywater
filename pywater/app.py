from apscheduler.schedulers.background import BackgroundScheduler
from PyQt5.QtWidgets import QApplication

from .window import Window
from .db import createDB
from .notify import setup_notify


NOTIFY = True


def run():
    import sys

    # FIXME: this should be another process
    if NOTIFY:
        setup_notify()
    createDB()
    # show main app window
    qt = QApplication([])
    win = Window()
    win.show()
    sys.exit(qt.exec_())
