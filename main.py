from store import *


def main():
    app = QApplication([])
    window = Store()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()