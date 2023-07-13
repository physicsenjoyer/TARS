import time
import TARS_Servo_Controller
import TARS_Runner

toggleState = TARS_Runner.toggleState()

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
	
def starMain():
	if toggleState == True:
		TARS_Servo_Controller.plusStarMain()
	elif toggleState == False:
		TARS_Servo_Controller.minusStarMain()

def portMain():
	if toggleState == True:
		TARS_Servo_Controller.plusPortMain()
	elif toggleState == False:
		TARS_Servo_Controller.minusPortMain()

def starForarm():
	if toggleState == True:
		TARS_Servo_Controller.plusStarForarm()
	elif toggleState == False:
		TARS_Servo_Controller.minusStarForarm()

def portForarm():
	if toggleState == True:
		TARS_Servo_Controller.plusPortForarm()
	elif toggleState == False:
		TARS_Servo_Controller.minusPortForarm()

def starHand():
	if toggleState == True:
		TARS_Servo_Controller.plusStarHand()
	elif toggleState == False:
		TARS_Servo_Controller.minusStarHand()

def portHand():
	if toggleState == True:
		TARS_Servo_Controller.plusPortHand()
	elif toggleState == False:
		TARS_Servo_Controller.minusPortHand()