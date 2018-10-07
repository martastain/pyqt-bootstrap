from .common import *

class Application(QApplication):
    def __init__(self, **kwargs):
        super(Application, self).__init__(sys.argv)
        self.setStyleSheet(app_skin)
        self.app_state_path = kwargs.get(
                    "app_state_path",
                    os.path.join(app_dir, "{}.appstate".format(app_settings["name"]))
                )
        self.app_state = {}
        app_settings.update(kwargs)
