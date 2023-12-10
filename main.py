import sys
import threading
import time
from PySide2 import QtCore, QtGui, QtWidgets
from ui_dashboard import Ui_MainWindow
import requests

url = "http://192.168.1.2:8000/items/"

class Main(QtWidgets.QMainWindow):
	update_progress_bar = QtCore.Signal(float)

	def __init__(self):
		super(Main, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.showFullScreen()

		self.update_progress_bar.connect(self.setProgressBarValue)

		self.info_thread = threading.Thread(target=self.updateInfo, daemon=True)
		self.info_thread.start()

		self.show()

	def setProgressBarValue(self, value):
		self.ui.progressBar_3.setValue(value)

	def updateInfo(self):
		last_update_time = 0
		update_interval = 0.1  # Update every 0.1 seconds

		while True:
			current_time = time.time()
			if current_time - last_update_time > update_interval:
				try:
					response = requests.get(url)
					if response.status_code == 200:
						try:
							value = float(response.json().get('thorttle', 0)) * 100
						except:
							pass
						self.update_progress_bar.emit(value)
					last_update_time = current_time
				except requests.RequestException as e:
					print(f"Network error: {e}")
			time.sleep(0.01)  # Short sleep to prevent high CPU usage

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Main()
	sys.exit(app.exec_())
