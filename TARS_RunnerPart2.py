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

