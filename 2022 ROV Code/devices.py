from gpiozero import Motor, Servo

class rovMotor(Motor):
    def __init__(self, forward, backward):
        Motor.__init__(self, forward,backward)
    
    def setSpeed(self, setpoint):
        try:
            if setpoint > 0.05:
                self.forward(setpoint)
            elif setpoint < -0.05:
                self.backward(-1*setpoint)
            else:
                self.forward(0)
        except ValueError:
            print("setpoint needs to be between -1 and 1")
            
m = rovMotor(12, 14)
m.setSpeed(0.3)
m.setSpeed(0.1)
    