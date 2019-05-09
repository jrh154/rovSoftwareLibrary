import lib.device_library as dl
from lib.maps import piMap

class deviceList():
	m = piMap()
	
	## Initialize your devices (motors, sensors, etc) here. For example, start a motor here
	testServo = dl.rovServo(m.testServo_pin)
	testDualEsc = dl.rovBrushlessDualESC(m.testMotorDualESC_fpin, m.testMotorDualESC_rpin)
