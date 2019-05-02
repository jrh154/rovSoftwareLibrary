# Overview

RovSoftware is a Python resource that can be used to program controls of an ROV robot using a USB controller. The program currently supports X-box controllers but may be easily adapted to other controllers as needed.

The software consists of three main files:
  *robot.py
  *devices.py
  *maps.py

Users will modify these three files as needed to program their robot. The file structure for this library is as follows:
```python
  /main
    -Robot.py
    -devices.py
    /lib
      -device_list.py
      -maps.py
```

## Supported Devices
The RovSoftware library is currently equipped to support the following devices:
  *Brushed motors using an H-bridge controller
  *Servos
  *Unidirectional brushless motor using an unidirectional electronic speed controllers
  *Bidirectional brushless motor control using two unidirectional electronic speed controllers.

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

When we make a ```rovServo``` object we pass the value of the pin the servo is connected to. By having this mapped previously we eliminate the need to change a lot of our code by simply using the maps.py file.

## Programming the Servo
To summarize, so far we have assigned one of the GPIO pins to our servo in the maps.py file and used this info initialize a rovServo object. It is now time to write some code that will help us control this Servo in the robot.py file.

To start, open the robot.py file and go the following lines in the ```__main__()``` function.

```python
while 1:
  cip_input.read_state()
  ### Write your robot code here (script or write other functions)
```

We will add code that will move the servo using the right trigger of our controller. DO NOT MODIFY THE ```cip.read_state()``` COMMAND.

Add the following code to the robot.py file:

```python
while 1:
  cip_input.read_state()
  ### Write your robot code here (script or write other functions)
  servo_position = servoInput(cip.right_trigger, "trigger")
  devices.tests_servo.set_position(servo_position)

```

Now, as you pull the trigger the servo will move from the minimum position to the maximum position.

## Running Your Code
To run your code you will begin by opening up a terminal window. Once open, navigate to the directory containing your robot code.

Once there, simply type:

```python robot.py```

This will begin your program and your robot should be operational.

To stop the code, simply type ```Ctrl-Z```

# Controller_Input.py File Objects and Functions

This may be expanded to include other usb controllers, but for now will only enumerate the values for the Xbox Elite Controller (generalizes to other x-box one controllers)

## Accessing Raw Input Values
The ```Controller()``` object in controller_input.py stores the raw input values from the controller.

In the Robot.py code, the controller object is created as ```cip```. To read the current value of the controller input use the following code:

```python
controller_object.*input button*
```

where *input button* is the variable for the controller button/stick/trigger. For example, the following code will read the value of the Right Trigger and print the value:

```python
value = controller_object.right_trigger
print(value)
```

In the above example the code will print 0 if the trigger is not pressed and 1023 if the trigger is fully pressed.

## Converted Input Functions
The following functions can be used to convert raw input into a number that can be read by an ROV device.

To return a value between 0 and 100 (typically used for a servo or single direction brushless motor) use the following function:

```python
servoInput(input_value, input_type)
```

input_value is the value to be converted. Typically called using the Controller object (i.e., ```controller.a_button```).

input_type is one of four values, either ```"trigger"```, ```"stick"```, ```"half_stick_pos"```, or ```"half_stick_pos"```. Note that all ```input_type``` values are ```type string```.

Using ```"trigger"``` will convert the raw input from one of the trigger values.

Using ```"stick"``` will convert the raw input from one of the stick input axes, using the full range of the stick (all the way down = 0 and all the way up = 1)

Using ```"half_stick_pos"``` or ```"half_stick_neg"``` will only take input from half a stick's range. Note that positive is down for the y-axis and negative is up for the y-axis.

#### Example:
The following code will return a value of 0 if the right stick is in the neutral position or pushed to the left and a value between 0 and 100 if the right stick is pushed to the right:

```python
t = servoInput(controller.right_stick_x, 'half_stick_pos')
print(t)
```

## XboxOne Controller
### Buttons:
Buttons return values of 1 (pressed) or 0 (not pressed)

**Button Variables**

A button = a_button

B button = b_button

X button = x_button

Y button = y_button
Start = start_button

Select = select_button

Left Bumper = left_bumper

Right Bumper = right_bumper

### D-Pad:
The d-pad has only two components, x and y. Each can return one of three values, -1, 0, 1.

There can be 9 total directions to read from the d-pad (including neutral)

**D-pad variables**

D-pad up and down = y_hat

D-pad left and right = x_hat

### Triggers
The triggers return raw values between 0 and 1023.
Left Trigger = left_trigger
Right Trigger = right_trigger

### Sticks
Sticks return values between -32768 (up/left) and 32767 (down, right)

**Stick Variables**

Left Stick, up/down = left_stick_y

Left Stick, left/right = left_stick_x

Right Stick, up/down = right_stick_y

Right Stick, left/right = right_stick_x

# Device Library
This section covers the APIs for the various device objects in the rovSoftware library. Each object has a number of functions which can be used to modify the object or set the device speed/position.

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
.stop()
```
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

```python
.stop()```

stops the motor (useful for emergency stop situations)

## rovBrushed

call with:
```python
rovBrushed(pin1, pin2)```

pin1 = pin connected to the H-bridge forward port

pin2 = pin connected to the H-bridge reverse port


```python
.set_speed(value)```

value = a number between -50 and 50. 50 corresponds to full forward, -50 full reverse, and 0 to stop

```
.stop()
```
stops the motor (useful for emergency stop situations)
