from controller_input import Controller
from time import sleep

class twoButtonServo():
	def __init__(self, button1, button2, refresh_rate = 0.1):
		self.button1 = button1
		self.button2 = button2
		self.refresh_rate = refresh_rate

	def read_state(self, button1, button2):
		self.button1 = button1
		self.button2 = button2

	def set_output(self):		
		if self.button1 == 1:
			if self.output < 50:
				self.output += 1
			#sleep(self.refresh_rate)
		elif self.button2 == 1:
			if self.output > -50:			
				self.output += -1
			#sleep(self.refresh_rate)
	output = 0

cont = Controller()
test = twoButtonServo(cont.a_button, cont.b_button)

while 1:
	cont.read_state()
	print(cont.a_button)
	#test.read_state(cont.a_button, cont.b_button)
	#test.set_output()
	#print(test.output)
	
