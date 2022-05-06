#Dependencies so far:
## Webcam Streaming Service
### Option 1: Motion
Using the motion package. Link to install tutorial:

(Motion)[https://www.circuitbasics.com/how-to-make-a-webcam-server-using-the-raspberry-pi-camera/]

Key here: need to ensure streamrate and framerate are low latency.

Port for streaming is 8081 (so address is <IP.ADD.RE.SS:8081)

### Option 2: fswebcam
Havne't looked into this too much, but package is installed. May be used only to capture images rather than stream the signal.

## Image processing
Using the OpenCV package to enable on-board image processing. 

`sudo pip3 install opencv-python`

## Arduino-Python Communication
*current solution*
Looking at using (PyFirmata)[https://github.com/tino/pyFirmata] as communication profile. But may be limited in ability to use I2C, Serial comms, servos, etc. 

`sudo pip3 install pyfirmata`

Should continue to look at other possible solutions for this problem.

## USB over Ethernet (VirtualHere)
-install server on driver station computer
(Windows Server Link)[https://virtualhere.com/sites/default/files/usbclient/vhui64.exe]

### New Client
The free version of VirtualHere only supports one device and will only connect through GUI.
This means we will need to run VNCViewer (or similar) to connect to PI (which may not be worst anyways)

*KEY NOTE* XboxOne controllers do not run on VirtualHere. 

(Link to Client Download)[https://virtualhere.com/usb_client_software]


### Depricated
-install client on raspberry pi/underwater computer
`curl https://virtualhere.com/sites/default/files/usbclient/vhclientarmhf`
`sudo chmod +x vhclientarmhf`
^download client then make executable

## Xbox Controller-Python

###Current version
[Approximate Engineering Input Documentation]{https://approxeng.github.io/approxeng.input/index.html}
`pip3 install approxeng.input`
Installs the library

Quite possibly will need to make a new profile for the controller if off-brand. Note that Xbox One controllers do not work here :(

### Depricated (works for xbox 360 controller, python2 only?) 
`sudo apt-get install xboxdrv`
Install the xboxdrv drvier

`git clone https://github.com/martinohanlon/XboxController`
Clone/import the XboxController class wrapper thi

`python3 -m pip install pygame`
Install the pygame library

##arduino-cli
`curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh`
install arduino-cli

`#alias arduino-cli='./home/<usr>/pi/bin/arduino-cli'`
add arduino-cli to command

`arduino-cli core install arduino:avr` 
Install 