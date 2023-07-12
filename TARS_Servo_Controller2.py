''' 
TARS 2.1 Controller Program
6/24/2023
last update: 7/12/2023
Charlie Diaz

This program will facilitate the communication between TARS and an 8-Bit-Do Bluetooth 
controller. Notable changes to the TARS platform include the addition of two, triple jounted 
grippers, each consisting of two arm joints and a hand joint. One of the big goals for this
program is to concentrate the previous TARS operating system into a single, legible, simple 
file. There's really no reason to have three programs, and one program has the benefits of 
being 1) easier to run, 2) easier to read, 3) easier to work on.

8-Bit-Do Controller Commands:
Walking:
    Forward Arrow - Step Forward
    Backwards Arrow - Step Backwards
    Left Arrow - Turn Left (~30 degrees)
    Right Arrow - Turn Right (~30 degrees)
Grippers:
    Left Bumper - Activate Left Gripper
    Left Trigger - Deactivate Left Gripper
    Right Bumper - Activate Right Gripper
    Right Trigger - Deactivate Right Gripper
    


'''

# Walking lock-out --> prevents TARS from walking with stuff in its hand or with the arms deployed
# This is a provisional locking mechanism while I figure out how to get TARS to be able to walk with
# things in its grippers.  I'm thinking we do it so that it locks out the walking function if the 
# arms aren't either stowed or above a "safe" zone.  It's actually not going to be that easy, since 
# the things TARS picks up won't have zero mass... that includes the arms themselves, so we'll have 
# to do some kinematics to balance out TARS so it doesn't fall flat on its face when it tries to walk 
# with stuff. A possible solution could be to print the props with super light filament or foam and 
# packing weights into the back of TARS. That might actually work, but it'll be tricky.


from __future__ import division
import time
import Adafruit_PCA9685
import thread

pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

# Center Lift Servo (0) Values
upHeight = 220
neutralHeight = 260
downHeight = 360

# Port Drive Servo (1) Values
forwardPort = 485
neutralPort = 375
backPort = 265

# Starboard Drive Servo (2) Values
forwardStarboard = 250
neutralStarboard = 360
backStarboard = 470

# moves the torso from a neutral position upwards, allowing the torso to pivot forwards or backwards
def height_neutral_to_up():
	height = neutralHeight
	print('setting center servo (0) Neutral --> Up position')
	while (height > upHeight):
		height = height - 1
		pwm.set_pwm(0, 0, height)
		time.sleep(0.001)
		print('center servo (0) set to: Up position\n ')

# rotates the torso outwards, enough so that when TARS pivots and lands, the bottom of the torso is 
# flush with the ground. Making the torso flush with the ground is an intentional improvement from
# previous programs, where TARS would land and then slide a little on smooth surfaces, which while
# allowing for a simple walking program, inhibited TARS' ability to walk on surfaces with different 
# coefficients of friction
def torso_neutral_to_forwards():
	port = neutralPort
	starboard = neutralStarboard
	print('setting port and starboard servos (1)(2) Neutral --> Forward')
	while (port < forwardPort):
		port = port + 1
		starboard = starboard - 1
		pwm.set_pwm(1, 1, port)
		pwm.set_pwm(2, 2, starboard)
		time.sleep(0.0001)
	print('port and starboard servos (1)(2) set to: Forward position\n ')
	
# rapidly shifts the torso height from UP --> DOWN and then returns --> UP, which should cause TARS 
# to pivot and land on it's torso
def torso_bump():
	height = upHeight
	print('performing a torso bump\nsetting center servo (0) Up --> Down position FAST')
	while (height < downHeight):
		height = height + 1
		pwm.set_pwm(0, 0, height)
		time.sleep(0.00001)
	print('setting center servo (0) Down --> Up position FAST')
	while (height > upHeight):
		height = height - 1
		pwm.set_pwm(0, 0, height)
		time.sleep(0.00001)
	print('center servo (0) returned to Up position\n')
	
# returns the torso's vertical height and rotation to centered values from up height and forward 
# rotation. Activates two external functions so movement in both axes can occur in parallel.
def torso_return():
	thread.start_new_thread(torso_return_rotation, ())
	thread.start_new_thread(torso_return_vertical, ())

# returns torso's rotation to neutral from forward
def torso_return_rotation():
	port = forwardPort
	starboard = forwardStarboard
	print('setting port and starboard servos (1)(2) Forward --> Neutral position')
	while (port > neutralPort):
		port = port - 1
		starboard = starboard + 1
		pwm.set_pwm(1, 1, port)
		pwm.set_pwm(2, 2, starboard)
		time.sleep(0.0001)
	print('port and starboard servos (1)(2) set to: Neutral position\n ')

# returns torso's vertical to neutral from up	
def torso_return_vertical():
	height = upHeight
	print('setting center servo (0) Up --> Down position')
	# moving the torso down to create clearance for the rotation of the legs
	while (height < downHeight):
		height = height + 1
		pwm.set_pwm(0, 0, height)
		time.sleep(0.001)
	# moving the torso up from down to neutral
	while (height > neutralHeight):
		height = height - 1
		pwm.set_pwm(0, 0, height)
		time.sleep(0.001)
	print('center servo (0) set to: Neutral position\n ')

