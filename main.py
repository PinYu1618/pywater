import time
import multiprocessing as mp

from pywater import app, notify

NOTIFY = True


def main():
    p = mp.Process(target=app.run)
    p.start()

    if NOTIFY:
        notify.setup()
        while True:
            time.sleep(10)  # 暫停10秒鐘
            print("程式執行中.....")


if __name__ == "__main__":
    main()
