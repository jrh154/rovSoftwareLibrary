# Overview

RovSoftware is a Python resource that can be used to program controls of an ROV robot using a USB controller. The program currently supports X-box controllers but may be easily adapted to other controllers as needed.

The software consists of three main files:
  -robot.py
  -devices.py
  -maps.py

Users will modify these three files as needed to program their robot. The file structure for this library is as follows:
  /main
    -Robot.py
    -devices.py
    /lib
      -device_list.py
      -maps.py

## Supported Devices
The RovSoftware library is currently equipped to support the following devices:
  -Brushed motors using an H-bridge controller
  -Servos
  -Unidirectional brushless motor using an unidirectional electronic speed controllers
  -Bidirectional brushless motor control using two unidirectional electronic speed controllers.

More devices may be supported in future versions and users are welcome and encouraged to contribute to the project as their needs arise.


# Tutorial Example - Controlling a Servo
The following tutorial will explain how to program your robot to control a servo using the RovSoftware library. It is assumed that users know the appropriate wiring already.

## Mapping the Servo
The first step in the process is to modify the maps.py file to include the pin the Servo is connected to.

To start, open up the file maps.py (located in the lib directory)

Now modify the piMap() class by deleting the ```pass``` command and adding a variable for the pin the servo is connected to:

```python
class piMap():
	##List the motor/controller pins here
	test_servo_pin = 11
```

Here, the servo is connected to pin 11. We have assigned the variable ```test_servo_pin``` to contain this information.

## Initiating a Device
Now that we have recorded the GPIO pin, we must make an Servo object to call in our code. To start, open up the file devices.py.

```python
class deviceList():
  map = piMap()
	## Initialize your devices (motors, sensors, etc) here. For example, start a motor here
	pass
```

Delete the ```pass``` command and replace it with the following code:

```python
class deviceList():
  map = piMap()
	## Initialize your devices (motors, sensors, etc) here. For example, start a motor here

	test_servo = rovServo(map.test_servo_pin)

```

Here, when we make a ```rovServo``` object we pass the value of the pin the servo is connected to. By having this mapped previously we eliminate the need to change a lot of our code by simply using the maps.py file.

## Programming the Servo
To summarize, so far we have assigned one of the GPIO pins to our servo in the maps.py file and used this info initialize a rovServo object. It is now time to write some code that will help us control this Servo in the robot.py file.

To start, open the robot.py file and go the following lines in the ```__main__()``` function.

```python
while 1:
  controller_input.read_state()
  ### Write your robot code here (script or write other functions)
```

We will add code that will move the servo using the right trigger of our controller. DO NOT MODIFY THE ```controller_input.read_state()``` COMMAND.

**THIS STILL NEEDS MODIFICATION**

# Controller Buttons
This may be expanded to include other usb controllers, but for now will only enumerate the values for the Xbox Elite Controller (generalizes to other x-box one controllers)

## XboxOne Controller
### Buttons:
Buttons return values of 1 (pressed) or 0 (not pressed)
A button = a_button
B button = b_button
X button = x_button
Y button = y_button
Start = start_button
Select = select_button
Left Bumper = left_bumper
Right Bumper = right_bumper

### D-Pad:
The d-pad has only two components, x and y. Each can return one of three values, -1, 0, 1. In this way there can be 0 total directions to read from the d-pad (including neutral)
D-pad up and down = y_hat
D-pad left and right = x_hat

### Triggers
The triggers return raw values between 0 and 1023.
Left Trigger = left_trigger
Right Trigger = right_trigger

### Sticks
Sticks return values between -32768 (up/left) and 32767 (down, right)
Left Stick, up/down = left_stick_y
Left Stick, left/right = left_stick_x
Right Stick, up/down = right_stick_y
Right Stick, left/right = right_stick_x

# Device Library
Here is an overview of the different functions in each device call:

## rovServo
This object allows you to

call with:
```rovServo = (pin)```

pin = GPIO pin number the servo is connected to
```python 
set_position(value)```

value = a number between 0 and 100. 50 corresponds to the middle position

```python 
reset()```

sets the servo to the neutral (mmiddle) position.

## rovBrushless

call with:
```
rovBrushless = (pin)
```
 
pin = GPIO pin number the ESC is connected to
 
```python 
.set_speed(value)```
value = a number between 0 and 100. 0 corresponds to off and 100 corresponds to full speed.

```python
.stop()```

Stops the motor from rotating (useful for emergency stop situations)

## rovBrushlessDualEsc

call with:
```python 
rovBrushlessDualEsc(pin1, pin2)```
pin1 = pin the forward ESC is connected to

pin2 = pin the reverse ESC is connected to

```python 
.set_speed(value)```

value = a number between -50 and 50. 50 corresponds to full forward, -50 full reverse, and 0 to stop

```.stop()``` stops the motor (useful for emergency stop situations)

## rovBrushed

call with:
```rovBrushed(pin1, pin2)
pin1 = pin connected to the H-bridge forward port
pin2 = pin connected to the H-bridge reverse port

```.set_speed(value)```
value = a number between -50 and 50. 50 corresponds to full forward, -50 full reverse, and 0 to stop

```.stop()```
stops the motor (useful for emergency stop situations)

