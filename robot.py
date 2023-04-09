import time
from gpiozero import Servo
from approxeng.input.selectbinder import ControllerResource
from devices import rovMotor

'''
Set pin values and initialize motors
'''

#Define motor pins
VM1_PIN1 = 7
VM1_PIN2 = 4

VM2_PIN1 = 5
VM2_PIN2 = 6

XM_PIN1 = 9
XM_PIN2 = 8

YM_PIN1 = 2
YM_PIN2 = 10

#Define servo pins
S1_PIN = 3

#Initiate motors
v_motor1 = rovMotor(VM1_PIN1, VM1_PIN2)
v_motor2 = rovMotor(VM2_PIN1, VM2_PIN2)
x_motor = rovMotor(XM_PIN1, XM_PIN2)
y_motor = rovMotor(YM_PIN1, YM_PIN2)

#Initiate servo
servo1 = Servo(S1_PIN)

'''
Functioning robot code
'''
while True:
    try:
        #joystick found, run code
        with ControllerResource() as joystick:
            print("Joystick Found")
            while joystick.connected:
                #Get motor setpoint values
                v_speed = -1*joystick['ry'] #-1 de-inverts controls (up on stick is forward)
                x_speed = joystick['lx']
                y_speed = -1*joystick['ly'] #-1 de-inverts controls (up on stick is forward)
                
                #Get servo setpoint values
                servo_setpoint = joystick['lt'] - joystick['rt']
                
                #Set motor speed values
                v_motor1.setSpeed(v_speed)
                v_motor2.setSpeed(-1*v_speed) #Opposite direction due to opposite prop pitch
                x_motor.setSpeed(x_speed)
                y_motor.setSpeed(y_speed)
                
                #Set Servo value
                servo1.value = servo_setpoint
                
            print("Joystick Connection Lost!")
    except IOError:
        # No joystick found, wait for a bit
        print("Unable to find any joysticks")
        time.sleep(1.0)
