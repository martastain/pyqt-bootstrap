#!/usr/bin/env python3

from pyqtbs import *

class MainWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        label = QLabel("Hello world")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = Application(
            name="qtdemo",
            title="Cute demo"
        )

    window = MainWindow(app, MainWidget)
    app.exec_()
