import sys

from PyQt5.QtWidgets import QApplication, QWidget


def main():
    print("Hello world.")
    app = QApplication([])
    win = QWidget()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
