#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from qt_common import *
from app_main import MainWidget

class MainWindow(QMainWindow):
    def __init__(self, parent):
        super(MainWindow, self).__init__()
        self.setWindowTitle(APP_NAME)
        self.setStyleSheet(base_css)
        self.app = parent
        self.init_ui()

        settings = app_settings()
        if "main_window/geometry" in settings.allKeys():
            self.restoreGeometry(settings.value("main_window/geometry"))
            self.restoreState(settings.value("main_window/state"))
        else:
            self.resize(DEFAULT_W, DEFAULT_H)
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())

        self.show()

    def closeEvent(self, event):
        settings = app_settings() 
        settings.setValue("main_window/state", self.saveState())
        settings.setValue("main_window/geometry", self.saveGeometry())

        if hasattr(self.main_widget, "on_close"):
            self.main_widget.on_close()

    def init_ui(self):
        self.main_widget = MainWidget(self)
        self.setCentralWidget(self.main_widget)

    def status(self, message, message_type=1):
        print (message)
        if message_type > 0:
            self.statusBar().showMessage(message)


class Application(QApplication):
    def __init__(self):
        super(Application, self).__init__(sys.argv)
        self.main_window = MainWindow(self)


if __name__ == "__main__":
    app = Application()
    app.exec_()