from maps import xBox_map
from inputs import get_gamepad

class Controller():
	map = xBox_map()

	a_button = 0
	b_button = 0
	x_button = 0
	y_button = 0
	start_button = 0
	select_button = 0
	left_bumper = 0
	right_bumper = 0

	##The following can have values of 1 (up pressed), 0 (nothing pressed) or -1 (down pressed)
	y_hat = 0
	x_hat = 0

	##The following have values between 0 and 1023
	left_trigger = 0
	right_trigger = 0

	##The following have values between -32768 and 32767
	left_stick_y = 0
	left_stick_x = 0
	right_stick_y = 0
	right_stick_x = 0

	def read_state(self):
		events = get_gamepad()
		for event in events:
			if event.code == self.map.a_button:
				self.a_button = event.state
			elif event.code == self.map.b_button:
				self.b_button = event.state
			elif event.code == self.map.x_button:
				self.x_button = event.state
			elif event.code == self.map.y_button:
				self.y_button = event.state
			elif event.code == self.map.start_button:
				self.start_button == event.state
			elif event.code == self.map.select_button:
				self.select_button == event.state
			elif event.code == self.map.left_bumper:
				self.left_bumper = event.state
			elif event.code == self.map.right_bumper:
				self.right_bumper = event.state
			elif event.code == self.map.y_hat:
				self.y_hat = event.state
			elif event.code == self.map.x_hat:
				self.x_hat = event.state
			elif event.code == self.map.left_trigger:
				self.left_trigger = event.state
			elif event.code == self.map.right_trigger:
				self.right_trigger = event.state
			elif event.code == self.map.left_stick_y:
				self.left_stick_y = event.state
			elif event.code == self.map.left_stick_x:
				self.left_stick_x = event.state
			elif event.code == self.map.right_stick_y:
				self.right_stick_y = event.state
			elif event.code == self.map.right_stick_x:
				self.right_stick_x = event.state

## Returns value between 0 and 100 when given a trigger or stick value
def servoInput(input_value, input_type):
	input_type_list = ['trigger', 'stick', 'button', 'half_stick_pos', 'half_stick_neg']	

	if input_type not in input_type_list:
		raise ValueError("Input type %s is not a supported type. Check your spelling?" %input_type)

	if input_type == 'trigger':
		if input_value > 1023 or input_value < 0:
			raise ValueError("The input value is out of the expected range. Input value is %s" %str(input_value)) 
		else:
			output = input_value/1023.0*100

	elif input_type == 'stick':
		if input_value > 32768 or input_value < -37268:
			raise ValueError("The input value is out of the expected range. Input value is %s" %str(input_value)) 
		output = 100*(input_value/65536.0+0.50)

	elif input_type == 'half_stick_pos':
		if abs(input_value) > 32768:
			raise ValueError("The input value is out of the expected range. Input value is %s" %str(input_value)) 
		if input_value <= 0:
			output = 0
		else:
			output = input_value/32767.0*100

	elif input_type == 'half_stick_neg':
		if abs(input_value) > 32768:
			raise ValueError("The input value is out of the expected range. Input value is %s" %str(input_value)) 
		if input_value >= 0:
			output = 0
		else:
			output = -1*input_value/32768.0*100

	return output

##Returns motor output between -50 and 50 from stick input
def motorStickInput(input_value, inverted = False):
	if input_value < -37268 or input_value > 37268:
		raise ValueError("Input value is out of range. Input value is %s" %str(input_value))
	
	output = 50*input_value/32768.0

	if inverted:
		output = output * -1

	return output


