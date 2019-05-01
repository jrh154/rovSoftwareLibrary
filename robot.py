from lib.controller_input import Controller
from devices import deviceList
from lib.maps import piMap

def __main__():

	hardware = piMap()
	controller_input = Controller()
	devices = deviceList()

	while 1:
		controller_input.read_state()
		print(controller_input.a_button)
		print(controller_input.b_button)
		print(controller_input.left_stick_y)

#Start the code
__main__()

