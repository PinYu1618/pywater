from pywater import app, notify

NOTIFY = False


def main():
    # FIXME: this should be another process
    if NOTIFY:
        notify.setup()
    app.run()


if __name__ == "__main__":
    main()
