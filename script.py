#!/usr/bin/env python
# File: script.py
# Name: D.Saravanan
# Date: 28/04/2023

import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Need one (and only one) QApplication instance per application
# Pass in sys.argv to allow command line arguments for the application
# If no command line arguments then QApplication([]) is required
app = QApplication(sys.argv)

window = QWidget()  # Create a Qt widget, which will be the window
window.show()  # Windows are hidden by default

app.exec()  # Start the event loop
