import os
import sys
import logging

from app_settings import *

from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *

Signal = pyqtSignal
Slot = pyqtSlot
Property = pyqtProperty 


if getattr(sys, 'frozen', False):
    log_level = logging.INFO
    APP_PATH = os.path.dirname(sys.executable)
else:
    log_level = logging.DEBUG
    APP_PATH = os.path.dirname(os.path.realpath(__file__))

##########################################################################
## Logging

logging.basicConfig(
    level=log_level
    )

log = logging.getLogger(APP_COMMAND)


## Logging
##########################################################################

try:
    app_skin = open("skin.css").read()
except:
    app_skin = ""

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