from apscheduler.schedulers.blocking import BlockingScheduler

from .window import Window


class App:
    def __init__(self, view: Window):
        self.view = view


def notify():
    print("Go to drink water!")


def notifier():
    sched = BlockingScheduler(timezone="Asia/Taipei")
    sched.add_job(notify, "interval", seconds=2)
    sched.start()
