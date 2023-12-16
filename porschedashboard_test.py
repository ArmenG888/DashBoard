import sys
import threading
import time
from PySide2 import QtCore, QtGui, QtWidgets
from ui_porschedashboard import Ui_MainWindow
import requests

url = "http://192.168.1.2:8000/items/"

class Main(QtWidgets.QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Main()
	sys.exit(app.exec_())
