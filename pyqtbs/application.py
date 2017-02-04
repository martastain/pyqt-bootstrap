from .common import *

class Application(QApplication):
    def __init__(self, **kwargs):
        super(Application, self).__init__(sys.argv)
        self.setStyleSheet(app_skin)
        app_settings.update(kwargs)
