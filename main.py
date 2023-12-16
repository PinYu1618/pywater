import time
from pywater import app, notify

NOTIFY = False


def main():
    # TODO: change this to fork
    if NOTIFY:
        notify.setup()
        while True:
            time.sleep(10)  # 暫停10秒鐘
            print("程式執行中.....")
    else:
        app.run()


if __name__ == "__main__":
    main()
