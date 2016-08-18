#!/usr/bin/env python3

from qt_common import *

class MainWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)


if __name__ == "__main__":
    from qt_bootstrap import Application
    app = Application()
    app.exec_()
