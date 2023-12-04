from plyer import notification
from apscheduler.schedulers.background import BackgroundScheduler

from .models.encourage import encourage

TITLE = "Time to drink water!"


def setup_notify():
    # setup notification background scheduler
    sched = BackgroundScheduler(timezone="Asia/Taipei")
    sched.add_job(_notify, "interval", seconds=5)  # change this to hour in dist
    sched.start()
    print("Schedule started...")


def _notify():
    notification.notify(
        title=TITLE, message=encourage(), app_icon=None, timeout=3, toast=False
    )
