from gpiozero import Servo, Motor

##rovServo, needs pin as input when initializing
class rovServo(Servo):
	def __init__(self, pin):
		self = Servo.__init__.self(pin)

	##Sets servo to a given position, takes input between 0 and 100
	def set_position(self, setpoint):
		if setpoint < 0 or setpoint > 100:
			raise ValueError("Value must be between 0 and 100")
		servo_setpoint = (1/50.0)*setpoint-1
		self.value = servo_setpoint

	##Resets servo value to neutral (0) position
	def reset(self):
		self.value = 0

##rovBrushless, needs pin when initializing
class rovBrushless(Servo):
	def __init__(self, pin):
		self = Servo.__init__.self(pin)

	##Sets the motor speed to either -1 (no speed) or 1 (full speed)
	##Takes input between 0 and 100
	def set_speed(self, setpoint):
		if setpoint < 0 or setpoint > 100:
			raise ValueError("Value must be between 0 and 100")
		servo_setpoint = (1/50.0)*setpoint-1
		self.value = servo_setpoint

	##Stops motor
	def stop(self):
		self.value = -1


##Following classes require input between -50 and 50
class rovBrushlessDualEsc(Servo):
	def __init__(self, pin1, pin2):
		self.forward_esc = Servo.__init__(pin1)
		self.reverse_esc = Servo.__init__(pin2)

	##Requires input between -50 (full reverse) and 50 (full forward)
	def set_speed(self, setpoint):
		if setpoint < -50 or setpoint > 50:
			raise ValueError("Value must be between -50 and 50")
		elif setpoint >= 0:
			servo_setpoint = setpoint/25.0-1
			self.forward_esc.value = sevro_setpoint
			self.reverse_esc.value = 0
		elif setpoint < 0:
			servo_setpoint = -1*setpoint/25.0-1
			self.forward_esc.value = 0
			self.reverse_esc.value = servo_setpoint

	##Stops motor
	def stop(self):
		self.forward_esc.value = -1
		self.reverse_esc.value = -1

##Takes value between -50 and 50
class rovBrushed(Motor):
	def __init__(self, pin1, pin2):
		self = Motor.__init__(pin1, pin2)

	def set_speed(self, setpoint):
		if setpoint < -50 or setpoint > 50:
			raise ValueError("Value must be between -50 and 50")
		elif setpoint >= 0:
			motor_setpoint = setpoint/50.0
			self.forward(motor_setpoint)
		elif setpoint < 0:
			motor_setpoint = -1*setpoint/50.0
			self.forward(motor_setpoint)

	def stop(self):
		self.forward(0)

