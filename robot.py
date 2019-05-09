import lib.controller_input as cip
from devices import deviceList
from lib.maps import piMap

def __main__():

	hardware = piMap()
	controller = cip.Controller()
	devices = deviceList()
	deadband = 3
	while 1:
		controller.read_state()
		### Write your robot code here (script or write other functions)
		servo_setpoint = cip.servoInput(controller.right_trigger, "trigger")
		print("Servo Setpoint: %s" %servo_setpoint)
		devices.testServo.set_position(servo_setpoint)

		motor_setpoint = cip.motorStickInput(controller.left_stick_y, True)

		if motor_setpoint > deadband or motor_setpoint < -1*deadband:
			motor_setpoint = motor_setpoint
		else:
			motor_setpoint = 0

		print("Motor Setpoint: %s" %motor_setpoint)
		devices.testDualEsc.set_speed(motor_setpoint)


#Start the code
__main__()

