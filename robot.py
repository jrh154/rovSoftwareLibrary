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
		servo_setpoint = cip.servoInput(controller.right_trigger, "trigger")
		print("Servo Setpoint: %s" %servo_setpoint)
		devices.testServo.set_position(servo_setpoint)

		motor_setpoint = cip.stickMotorInput(controller.left_stick_y, True)
		print("Motor Setpoint: %s" %motor_setpoint)
		devices.testDualESC.set_position(motor_setpoint)


#Start the code
__main__()

