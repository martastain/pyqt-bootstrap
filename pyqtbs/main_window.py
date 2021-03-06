from .common import *

DEFAULT_W = 800
DEFAULT_H = 600

class MainWindow(QMainWindow):
    def __init__(self, parent, MainWidgetClass):
        super(MainWindow, self).__init__()
        logging.add_handler(self.log_handler)
        self.setWindowTitle(app_settings["title"])
        self.setStyleSheet(app_skin)
        self.app = parent
        self.restore_state()
        self.main_widget = MainWidgetClass(self)
        self.setCentralWidget(self.main_widget)
        self.show()

    @property
    def app_state(self):
        return self.app.app_state

    @app_state.setter
    def app_state(self, value):
        self.app.app_state = value

    def save_state(self):
        state = get_app_state(self.app.app_state_path)
        state.setValue("main_window/state", self.saveState())
        state.setValue("main_window/geometry", self.saveGeometry())
        state.setValue("main_window/app", self.app_state)

    def restore_state(self):
        state = get_app_state(self.app.app_state_path)
        if "main_window/geometry" in state.allKeys():
            self.restoreGeometry(state.value("main_window/geometry"))
            self.restoreState(state.value("main_window/state"))
        else:
            self.resize(DEFAULT_W, DEFAULT_H)
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
        if "main_window/app" in state.allKeys():
            try:
                self.app_state = state.value("main_window/app")
            except Exception:
                log_traceback()

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
