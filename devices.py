import lib.device_library as dl
from lib.maps import piMap

class deviceList():
	map = piMap()
	
	## Initialize your devices (motors, sensors, etc) here. For example, start a motor here
	testServo = dl.rovServo(testServo_pin)
	testDualEsc = dl.rovBrushlessDualESC(testMotorDualESC_fpin, testMotorDualESC_rpin)
