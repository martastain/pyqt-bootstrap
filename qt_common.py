import os
import sys

from nxtools import *

from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *

from app_settings import *

Signal = pyqtSignal
Slot = pyqtSlot
Property = pyqtProperty


if getattr(sys, 'frozen', False):
    APP_PATH = os.path.dirname(sys.executable)
else:
    APP_PATH = os.path.dirname(os.path.realpath(__file__))

#
# Logging
#

DEBUG     = 0
INFO      = 1
WARNING   = 2
ERROR     = 3
GOOD_NEWS = 4

logging.name = APP_COMMAND

#
# Skin
#

try:
    app_skin = open("skin.css").read()
except:
    app_skin = ""

#
# Settings
#

def app_settings():
    return QSettings(os.path.join(APP_PATH, "{}.conf".format(APP_COMMAND)), QSettings.IniFormat)

def get_pix(name):
    if not name:
        return None
    pixmap = QPixmap(":/images/{}.png".format(name))
    if not pixmap:
        pix_file = os.path.join("images", "{}.png".format(name))
        if os.path.exists(pix_file):
            return QPixmap(pix_file)
    return None


class Pixlib(dict):
    def __getitem__(self, key):
        if not key in self:
            self[key] = get_pix(key)
        return self.get(key, None)

pixlib = Pixlib()
