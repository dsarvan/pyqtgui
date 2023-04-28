#!/usr/bin/env python
# File: script.py
# Name: D.Saravanan
# Date: 28/04/2023

import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets

# Subclass QMainWindow to customize application's main window
class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Application Title")

		# Set the central widget of the window
		button = QtWidgets.QPushButton("Press Me!")
		self.setCentralWidget(button)

		# Set the size parameters (width, height) pixels
		self.setFixedSize(QtCore.QSize(400, 300))



def main():
	"""Need one (and only one) QApplication instance per application.
    Pass in sys.argv to allow command line arguments for the application.
    If no command line arguments then QApplication([]) is required."""

	app = QtWidgets.QApplication(sys.argv)

	window = MainWindow()  # Create a subclass of QMainWindow
	window.show()  # Windows are hidden by default

	app.exec()  # Start the event loop

if __name__ == "__main__":
	main()
