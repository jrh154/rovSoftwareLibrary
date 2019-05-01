from lib.controller_input import Controller
from devices import deviceList
from lib.maps import piMap

def __main__():

	hardware = piMap()
	controller_input = Controller()
	devices = deviceList()

	while 1:
		controller_input.read_state()
		### Write your robot code here (script or write other functions)


#Start the code
__main__()

