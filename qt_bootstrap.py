#!/usr/bin/env python3

from qt_common import *

from app_main import MainWidget
from app_menu import app_menu
from app_toolbar import app_toolbar


class MainWindow(QMainWindow):
    def __init__(self, parent):
        super(MainWindow, self).__init__()
        logging.add_handler(self.log_handler)
        self.setWindowTitle(APP_NAME)
        self.setStyleSheet(app_skin)
        self.app = parent
        self.init_ui()
        self.restore_state()
        self.show()

    def init_ui(self):
        logging.debug("Initializing GUI")
        app_menu(self)
        app_toolbar(self)
        self.main_widget = MainWidget(self)
        self.setCentralWidget(self.main_widget)

    def save_state(self):
        settings = app_settings()
        settings.setValue("main_window/state", self.saveState())
        settings.setValue("main_window/geometry", self.saveGeometry())

    def restore_state(self):
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

    def log_handler(self, **kwargs):
        message_type = kwargs.get("message_type", INFO)
        message = kwargs.get("message", "")
        if not message:
            return
        if message_type == WARNING:
            QMessageBox.warning(self, "Warning", message)
        elif message_type== ERROR:
            QMessageBox.critical(self, "Error", message)
        else:
            self.statusBar().showMessage(message, 10000)

    def closeEvent(self, event):
        self.save_state()
        if hasattr(self.main_widget, "on_close"):
            self.main_widget.on_close()



class Application(QApplication):
    def __init__(self):
        super(Application, self).__init__(sys.argv)
        self.main_window = MainWindow(self)


if __name__ == "__main__":
    app = Application()
    app.exec_()
