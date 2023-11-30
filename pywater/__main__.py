from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyWater")


def main():
    import sys

    qt = QApplication([])
    win = Window()
    win.show()
    sys.exit(qt.exec_())


if __name__ == "__main__":
    main()
