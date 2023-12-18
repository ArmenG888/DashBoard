import sys,time,requests
import threading
from PySide2 import QtCore, QtGui, QtWidgets
from ui_porschedashboard import Ui_MainWindow

url = "http://192.168.1.2:8000/items/"

class Main(QtWidgets.QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.info_thread = threading.Thread(target=self.updateInfo, daemon=True)
		self.info_thread.start()
		self.show()
	def updateInfo(self):
		gear = 'N'
		speed,lap,fuel = 0,0,30
		tire_pressures = [0,0,0,0]
		last_update_time = 0
		update_interval = 0.1

		while True:
			current_time = time.time()
			if current_time - last_update_time > update_interval:
				try:
					response = requests.get(url)
					if response.status_code == 200:
						data = response.json()
						if data.get('gear') is not None and data.get('gear') != gear:
							gear = data.get('gear') - 1
							if gear == 0:
								gear = 'N'
							elif gear == -1:
								gear = 'R'
						if data.get('speed') is not None and data.get('speed') != speed:
							speed = round(data.get('speed')) 
							self.ui.speed.setText(str(speed))
						if data.get('tiresPressures') is not None and data.get('tiresPressures') != tire_pressures:
							tire_pressures = data.get('tiresPressures')
							self.ui.front_left.setText(f"{tire_pressures[0]:.0f} psi")
							self.ui.front_right.setText(f"{tire_pressures[1]:.0f} psi")
							self.ui.rear_left.setText(f"{tire_pressures[2]:.0f} psi")
							self.ui.rear_right.setText(f"{tire_pressures[3]:.0f} psi")
						if data.get('lap') is not None and data.get('lap') != lap:
							lap = data.get('lap')
							self.ui.lap.setText(str(lap))
						
						
						self.ui.gear.setText(gear)
						self.ui.speed.setText(str(speed))
						


					last_update_time = current_time
				except requests.RequestException as e:
					print(f"Network error: {e}")
			time.sleep(0.01) 
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Main()
	sys.exit(app.exec_())
