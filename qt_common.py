from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *

from app_settings import *

Signal = pyqtSignal
Slot = pyqtSlot
Property = pyqtProperty 

try:
    base_css = open("skin.css").read()
except:
    base_css = ""


def app_settings():
    return QSettings(".app_settings", QSettings.IniFormat)