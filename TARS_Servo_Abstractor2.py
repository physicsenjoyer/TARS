import time
import TARS_Servo_Controller

def stepForward():
	TARS_Servo_Controller.height_neutral_to_up()
	TARS_Servo_Controller.torso_neutral_to_forwards()
	TARS_Servo_Controller.torso_bump()
	TARS_Servo_Controller.torso_return()
	
def turnRight():
	TARS_Servo_Controller.neutral_to_down()
	TARS_Servo_Controller.turn_right()
	TARS_Servo_Controller.down_to_neutral()
	TARS_Servo_Controller.neutral_from_right()

def turnLeft():
	TARS_Servo_Controller.neutral_to_down()
	TARS_Servo_Controller.turn_left()
	TARS_Servo_Controller.down_to_neutral()
	TARS_Servo_Controller.neutral_from_left()
