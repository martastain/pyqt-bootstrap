import os
import sys
import subprocess

from app_settings import *

try:
    import cx_Freeze
except ImportError:
    print ("ERROR: cx_freeze is not installed")
    sys.exit(-1)

executables = [cx_Freeze.Executable(
        "qt_bootstrap.py",
        targetName="{}.exe".format(APP_COMMAND)
        )]

freezer = cx_Freeze.Freezer(executables,
    copyDependentFiles=True,
    createLibraryZip=False,
    appendScriptToExe=True,
    icon=APP_ICON,
    silent=False
    )

freezer.Freeze()