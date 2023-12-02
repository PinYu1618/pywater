from plyer import notification
from apscheduler.schedulers.background import BackgroundScheduler
from PyQt5.QtWidgets import QApplication

from .window import Window


class App:
    def __init__(self, view: Window):
        self.view = view


TITLE = "Time to drink water!"
# TODO: also use the good words generater here!
MSG = "(Some good words here)"


def notify():
    notification.notify(title=TITLE, message=MSG, app_icon=None, timeout=3, toast=False)


def run():
    import sys

    # FIXME: this should be another process
    # setup notification background scheduler
    sched = BackgroundScheduler(timezone="Asia/Taipei")
    sched.add_job(notify, "interval", seconds=5)  # change this to hour in dist
    sched.start()
    print("Schedule started...")

    # show main app window
    qt = QApplication([])
    win = Window()
    win.show()
    App(win)
    sys.exit(qt.exec_())
