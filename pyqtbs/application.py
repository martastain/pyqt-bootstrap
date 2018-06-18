from .common import *

class Application(QApplication):
    def __init__(self, **kwargs):
        super(Application, self).__init__(sys.argv)
        self.setStyleSheet(app_skin)
        self.app_state = {}
        app_settings.update(kwargs)
