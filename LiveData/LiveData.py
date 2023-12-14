import sys
import threading
import ac
import acsys 
import os
import json

l_lapcount=0
lapcount=0

        

def acMain(ac_version):
	global l_lapcount

	appWindow = ac.newApp("appName")
	ac.setSize(appWindow, 200, 200)

	ac.log("Hello, Assetto Corsa application world!")
	ac.console("Hello, Assetto Corsa console!")

	l_lapcount = ac.addLabel(appWindow, "Laps: 0")
	ac.setPosition(l_lapcount, 3, 30)

	return "appName"



        
def acUpdate(deltaT):
	global l_lapcount, lapcount
	gas = ac.getCarState(0, acsys.CS.Gas)
	brake = ac.getCarState(0, acsys.CS.Brake)


	ac.setText(l_lapcount, "Gas: {}\nBrake: {}".format(gas,brake))
	data = {
		'throttle':gas,
		'brake':brake,
		'rpm':ac.getCarState(0, acsys.CS.RPM),
		'gear':ac.getCarState(0, acsys.CS.Gear),
		'speed':ac.getCarState(0, acsys.CS.SpeedKMH),
		'tiresTemp':ac.getCarState(0, acsys.CS.CurrentTyresCoreTemp),
		'tiresPressures':ac.getCarState(0, acsys.CS.DynamicPressure),
		
	}
	w = open("C:/Users/armen/Documents/Github/DashBoard/test.txt", "w+")
	json.dump(data,w)