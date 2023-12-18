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
		speed,lap,fuel,bb,abs,tc = 0,0,0,0,0,0
		tire_pressures = [0,0,0,0]
		last_update_time = 0
		update_interval = 0.1
		max_fuel = 0
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
							self.ui.gear.setText(str(gear))
						if data.get('speed') is not None and data.get('speed') != speed:
							speed = round(data.get('speed')) 
							self.ui.speed.setText(str(speed))
						if data.get('tiresPressures') is not None and data.get('tiresPressures') != tire_pressures:
							tire_pressures = data.get('tiresPressures')
							self.ui.front_left.setText(f"{tire_pressures[0]:.00f} psi")
							self.ui.front_right.setText(f"{tire_pressures[1]:.00f} psi")
							self.ui.rear_left.setText(f"{tire_pressures[2]:.00f} psi")
							self.ui.rear_right.setText(f"{tire_pressures[3]:.00f} psi")
						if data.get('lap') is not None and data.get('lap') != lap:
							lap = data.get('lap')
							self.ui.lap.setText(str(lap))
						if data.get('fuel') is not None and data.get('fuel') != fuel:
							fuel = round(data.get('fuel'),1)
							if fuel > max_fuel:
								max_fuel = fuel
							self.ui.fuel_level.setText(str(fuel))
							fuel_used = round(max_fuel - fuel,1)
							self.ui.fuel_used.setText(str(fuel_used))
						if data.get('brakeBias') is not None and data.get('brakeBias') != bb:
							bb = round(data.get('brakeBias')*100,1)
							self.ui.brake_bias.setText(str(bb)+"%")
						if data.get('tc') is not None and data.get('tc') != tc:
							tc = round(data.get('tc'),1)
							self.ui.tc.setText("TC-LA " + str(tc))
						if data.get('abs') is not None and data.get('abs') != abs:
							abs = round(data.get('abs'),1)
							self.ui.abs.setText("ABS " + str(abs))
						if data.get('currentTime') is not None:
							current_laptime = data.get('currentTime')[:-1]
							self.ui.current_laptime.setText(str(current_laptime))
						
						self.ui.speed.setText(str(speed))
						


					last_update_time = current_time
				except requests.RequestException as e:
					print(f"Network error: {e}")
			time.sleep(0.01) 
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Main()
	sys.exit(app.exec_())
