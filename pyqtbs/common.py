import os
import sys

from nxtools import *

from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *

Signal = pyqtSignal
Slot = pyqtSlot
Property = pyqtProperty

#
# Settings
#

app_dir = os.getcwd()

class AppSettings():
    def __init__(self):
        self.data = {
                "name" : "qtapp"
            }

    def get(self, key, default=False):
        return self.data.get(key, default)

    def update(self, data):
        return self.data.update(data)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        if key == "title":
            return self.get(key, self.data["name"])
        return self.data[key]

app_settings = AppSettings()


def get_app_state():
    return QSettings(os.path.join(app_dir, "{}.appstate".format(app_settings["name"])), QSettings.IniFormat)

#
# Logging
#

DEBUG     = 0
INFO      = 1
WARNING   = 2
ERROR     = 3
GOOD_NEWS = 4

logging.name = app_settings["name"]

#
# Skin
#

app_skin = ""
skin_path = os.path.join(app_dir, "skin.css")
if os.path.exists(skin_path):
    try:
        app_skin = open(skin_path).read()
    except:
        log_traceback("Unable to read stylesheet")

#
# pix library
#

def get_pix(name):
    if not name:
        return None
    pixmap = QPixmap(":/images/{}.png".format(name))
    if not pixmap.width():
        pix_file = os.path.join(app_dir, "images", "{}.png".format(name))
        if os.path.exists(pix_file):
            return QPixmap(pix_file)
    return None

class Pixlib(dict):
    def __getitem__(self, key):
        if not key in self:
            self[key] = get_pix(key)
        return self.get(key, None)

pixlib = Pixlib()
