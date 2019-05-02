import lib.controller_input as cip
from devices import deviceList
from lib.maps import piMap

def __main__():

	hardware = piMap()
	controller = cip.Controller()
	devices = deviceList()
	while 1:
		controller.read_state()
		### Write your robot code here (script or write other functions)


#Start the code
__main__()

