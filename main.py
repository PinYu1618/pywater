import time
import multiprocessing as mp
from argparse import ArgumentParser

from pywater import app, notify


def get_parser() -> ArgumentParser:
    p = ArgumentParser(description="pywater cli")
    p.add_argument("-n", "--notify", default=1, type=int)
    p.add_argument("-i", "--interval", default=20, type=int)
    return p


def main():
    parser = get_parser()
    args = parser.parse_args()

    p = mp.Process(target=app.run)
    p.start()

    if args.notify:
        secs = args.interval
        notify.setup(secs)
        while True:
            time.sleep(10)  # 暫停10秒鐘
            print("程式執行中.....")


if __name__ == "__main__":
    main()
