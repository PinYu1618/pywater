import time
from plyer import notification
from apscheduler.schedulers.background import BackgroundScheduler
from PyQt5.QtWidgets import QApplication

from .window import Window


class App:
    def __init__(self, view: Window):
        self.view = view


def notify():
    notification.notify(
        title="Hello", message="world.", app_icon=None, timeout=3, toast=False
    )


# FIXME
def run():
    import sys

    # setup notification background scheduler
    sched = BackgroundScheduler(timezone="Asia/Taipei")
    sched.add_job(notify, "interval", seconds=5)
    sched.start()
    print("Schedule started...")

    # show app window
    qt = QApplication([])
    win = Window()
    App(win)
    sys.exit(qt.exec_())
