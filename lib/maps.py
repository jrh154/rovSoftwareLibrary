class piMap():
	##List the motor/controller pins here
	testServo_pin = 12
	testMotorDualESC_fpin = 14
	testMotorDualESC_rpin = 16



##Do not change this map
class xBox_map():
	##The following can have values of 1 (pressed) or 0 (not pressed)
	a_button = "BTN_SOUTH"
	b_button = "BTN_EAST"
	x_button = "BTN_NORTH"
	y_button = "BTN_WEST"
	start_button = "BTN_START"
	select_button = "BTN_SELECT"
	left_bumper = "BTN_TL"
	right_bumper = "BTN_TR"

	##The following can have values of 1 (up pressed), 0 (nothing pressed) or -1 (down pressed)
	y_hat = "ABS_HAT0Y"
	x_hat = "ABS_HAT0X"

	##The following have values between 0 and 1023
	left_trigger = "ABS_Z"
	right_trigger = "ABS_RZ"

	##The following have values between -32768 and 32767
	left_stick_y = "ABS_Y"
	left_stick_x = "ABS_X"
	right_stick_y = "ABS_RY"
	right_stick_x = "ABS_RX"
