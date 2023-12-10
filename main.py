import sys
import threading
import time
from PySide2 import QtCore, QtGui, QtWidgets
from ui_dashboard import Ui_MainWindow
import requests

url = "http://192.168.1.2:8000/items/"

class Main(QtWidgets.QMainWindow):
	update_throttle_progress_bar = QtCore.Signal(float)
	update_brake_progress_bar = QtCore.Signal(float)

	def __init__(self):
		super(Main, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.showFullScreen()

		self.update_throttle_progress_bar.connect(self.setThrottleProgressBarValue)
		self.update_brake_progress_bar.connect(self.setBrakeProgressBarValue)

		self.info_thread = threading.Thread(target=self.updateInfo, daemon=True)
		self.info_thread.start()

		self.show()

	def setThrottleProgressBarValue(self, value):
		self.ui.progressBar_3.setValue(value)

	def setBrakeProgressBarValue(self, value):
		self.ui.progressBar_4.setValue(value)  # Assuming progressBar_4 is for the brake

	def updateInfo(self):
		gear = 'N'
		speed,rpm = 0,0
		tires_temp,tire_pressures = [0,0,0,0],[0,0,0,0]
		last_update_time = 0
		update_interval = 0.1

		while True:
			current_time = time.time()
			if current_time - last_update_time > update_interval:
				try:
					response = requests.get(url)
					if response.status_code == 200:
						data = response.json()
						try:
							throttle = float(data.get('throttle', 0)) * 100
							brake = float(data.get('brake', 0)) * 100
							self.update_throttle_progress_bar.emit(throttle)
							self.update_brake_progress_bar.emit(brake)                       
						except ValueError:
							pass
						if data.get('gear') is not None and data.get('gear') != gear:
							gear = data.get('gear') - 1
							if gear == 0:
								gear = 'N'
							elif gear == -1:
								gear = 'R'
						if data.get('speed') is not None and data.get('speed') != speed:
							speed = data.get('speed')
						if data.get('rpm') is not None and data.get('rpm') != rpm:
							rpm = data.get('rpm')
						if data.get('tiresTemp') is not None and data.get('tiresTemp') != tires_temp:
							tiresTemp = data.get('tiresTemp')
							self.ui.frontLeftTemp.setText(f"{tiresTemp[0]:.0f}°C")
							self.ui.frontRightTemp.setText(f"{tiresTemp[1]:.0f}°C")
							self.ui.rearLeftTemp.setText(f"{tiresTemp[2]:.0f}°C")
							self.ui.rearRightTemp.setText(f"{tiresTemp[3]:.0f}°C")
						if data.get('tiresPressures') is not None and data.get('tiresPressures') != tire_pressures:
							tire_pressures = data.get('tiresPressures')
							self.ui.frontLeftPressure.setText(f"{tire_pressures[0]:.0f} psi")
							self.ui.frontRightPressure.setText(f"{tire_pressures[1]:.0f} psi")
							self.ui.rearLeftPressure.setText(f"{tire_pressures[2]:.0f} psi")
							self.ui.rearRightPressure.setText(f"{tire_pressures[3]:.0f} psi")
						self.ui.gear.setText(str(gear))
						self.ui.speed.setText(f"{speed:.0f}")
						self.ui.rpm.setText(f"{rpm:.0f}")

					last_update_time = current_time
				except requests.RequestException as e:
					print(f"Network error: {e}")
			time.sleep(0.01) 

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Main()
	sys.exit(app.exec_())
