from __future__ import division
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
servo_neutral = 375

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

#Neutral Height GOOD
servo0Neutral = 400

#Down Height
servo0Down = 500

#Up Height
servo0Up = 360

#Neutral Rotation GOOD
servo1Neutral = 375
servo2Neutral = 360

#Forward Rotation
servo1Forward = 485
servo2Forward = 240

#Back Rotation
servo1Back = 265
servo2Back = 440

mid1 = 370
mid2 = servo2Neutral - (mid1 - servo1Neutral)

mid1i = servo1Neutral - (mid1 - servo1Neutral)
mid2i = abs(servo2Neutral - mid2) + servo2Neutral

def neutralHeight():
	pwm.set_pwm(0, 0, servo0Neutral)
	
def neutralRotation():
	pwm.set_pwm(1, 1, servo1Neutral)
	pwm.set_pwm(2, 2, servo2Neutral)

def neut_to_down():
	servo0 = servo0Neutral
	
	while (servo0 < servo0Down):
		servo0 = servo0 + 1
		pwm.set_pwm(0, 0, servo0)
		print('Setting servos to: Servo 0: ', servo0)
		time.sleep(0.001)
		
def down_to_neut():
	servo0 = servo0Down
	
	while (servo0 > servo0Neutral):
		servo0 = servo0 - 1
		pwm.set_pwm(0, 0, servo0)
		print('Setting servos to: Servo 0: ', servo0)
		time.sleep(0.001)
		
def neut_to_up():
	servo0 = servo0Neutral
	
	while (servo0 > servo0Up):
		servo0 = servo0 - 1
		pwm.set_pwm(0, 0, servo0)
		print('Setting servos to: Servo 0: ', servo0)
		time.sleep(0.001)

def up_to_neut():
	servo0 = servo0Up
	
	while (servo0 < servo0Neutral):
		servo0 = servo0 + 1
		pwm.set_pwm(0, 0, servo0)
		print('Setting servos to: Servo 0: ', servo0)
		time.sleep(0.01)
		
def up_to_down_fast():
	servo0 = servo0Up
	
	while (servo0 < servo0Down):
		servo0 = servo0 + 15
		pwm.set_pwm(0, 0, servo0)
		print('Setting servos to: Servo 0: ', servo0)
		time.sleep(0.0001)
		
def down_to_up_fast():
	servo0 = servo0Down
	
	while (servo0 > servo0Up):
		servo0 = servo0 - 1
		pwm.set_pwm(0, 0, servo0)
		print('Setting servos to: Servo 0: ', servo0)
		time.sleep(0.001)
		
def shift_neut_to_forward():
	servo1 = servo1Neutral
	servo2 = servo2Neutral
	
	while (servo1 < servo1Forward):
		servo1 = servo1 + 1
		servo2 = servo2 - 1
		pwm.set_pwm(1, 1, servo1)
		pwm.set_pwm(2, 2, servo2)
		print('Setting servos to: Servo 1: ', servo1, ' and Servo 2: ', servo2)
		time.sleep(0.000001)
		
def shift_forward_to_back():
	servo1 = servo1Forward
	servo2 = servo2Forward
	
	while (servo1 > servo1Back):
		servo1 = servo1 - 2
		servo2 = servo2 + 2
		pwm.set_pwm(1, 1, servo1)
		pwm.set_pwm(2, 2, servo2)
		print('Setting servos to: Servo 1: ', servo1, ' and Servo 2: ', servo2)
		time.sleep(0.005)
		
def shift_forward_to_neut():
	servo1 = servo1Forward
	servo2 = servo2Forward
	
	while (servo1 > servo1Neutral):
		servo1 = servo1 - 2
		servo2 = servo2 + 2
		pwm.set_pwm(1, 1, servo1)
		pwm.set_pwm(2, 2, servo2)
		print('Setting servos to: Servo 1: ', servo1, ' and Servo 2: ', servo2)
		time.sleep(0.001)
		
def shift_forward_to_neut_slow():
	servo1 = servo1Forward
	servo2 = servo2Forward
	
	while (servo1 > servo1Neutral):
		servo1 = servo1 - 2
		servo2 = servo2 + 2
		pwm.set_pwm(1, 1, servo1)
		pwm.set_pwm(2, 2, servo2)
		print('Setting servos to: Servo 1: ', servo1, ' and Servo 2: ', servo2)
		time.sleep(0.05)

modifier = -30

def shift_forward_to_midmod():
	servo1 = servo1Forward
	servo2 = servo2Forward
	
	while (servo1 > mid1-modifier):
		servo1 = servo1 - 1
		servo2 = servo2 + 1
		pwm.set_pwm(1, 1, servo1)
		pwm.set_pwm(2, 2, servo2)
		print('Setting servos to: Servo 1: ', servo1, ' and Servo 2: ', servo2)
		time.sleep(0.01)

def shift_midmod_to_neutral():
	servo1 = mid1-modifier
	servo2 = mid2+modifier
	
	while (servo1 > servo1Neutral):
		servo1 = servo1 - 1
		servo2 = servo2 + 1
		pwm.set_pwm(1, 1, servo1)
		pwm.set_pwm(2, 2, servo2)
		print('Setting servos to: Servo 1: ', servo1, ' and Servo 2: ', servo2)
		time.sleep(0.01)


def shift_back_to_mid():
	servo1 = servo1Back
	servo2 = servo2Back
	
	while (servo1 < mid1):
		servo1 = servo1 + 1
		servo2 = servo2 - 1
		pwm.set_pwm(1, 1, servo1)
		pwm.set_pwm(2, 2, servo2)
		print('Setting servos to: Servo 1: ', servo1, ' and Servo 2: ', servo2)
		time.sleep(0.01)
	
def shift_mid_to_neut():
	servo1 = mid1
	servo2 = mid2
	
	while (servo1 < servo1Neutral):
		servo1 = servo1 + 1
		servo2 = servo2 - 1
		pwm.set_pwm(1, 1, servo1)
		pwm.set_pwm(2, 2, servo2)
		print('Setting servos to: Servo 1: ', servo1, ' and Servo 2: ', servo2)
		time.sleep(0.01)
	
def legsTurnRight():
	servo1 = servo1Neutral
	servo2 = servo2Neutral
	
	while (servo1 < mid1):
		servo1 = servo1 + 1
		servo2 = servo2 + 1
		pwm.set_pwm(1, 1, servo1)
		pwm.set_pwm(2, 2, servo2)
		time.sleep(0.001)
		
def legsTurnLeft():
	servo1 = servo1Neutral
	servo2 = servo2Neutral
	
	while (servo1 > mid1i):
		servo1 = servo1 - 1
		servo2 = servo2 - 1
		pwm.set_pwm(1, 1, servo1)
		pwm.set_pwm(2, 2, servo2)
		time.sleep(0.001)

def legsFromRtoN():
	servo1 = mid1
	servo2 = mid2i
	
	while (servo1 > servo1Neutral):
		servo1 = servo1 - 1
		servo2 = servo2 - 1
		pwm.set_pwm(1, 1, servo1)
		pwm.set_pwm(2, 2, servo2)
		time.sleep(0.05)

def legsFromLtoN():
	servo1 = mid1i
	servo2 = mid2
	
	while (servo1 < servo1Neutral):
		servo1 = servo1 + 1
		servo2 = servo2 + 1
		pwm.set_pwm(1, 1, servo1)
		pwm.set_pwm(2, 2, servo2)
		time.sleep(0.05)
		
def holdPose():
	pwm.set_pwm(0, 0, servo0Down)
	pwm.set_pwm(1, 1, servo1Forward)
	pwm.set_pwm(2, 2, servo2Forward)
