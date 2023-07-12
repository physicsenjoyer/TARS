import time
import TARS_Servo_Controller

def stepForward():
	TARS_Servo_Controller.neut_to_up()
	TARS_Servo_Controller.shift_neut_to_forward()
	time.sleep(1.5)
	TARS_Servo_Controller.up_to_down_fast()
	time.sleep(0.5)
	TARS_Servo_Controller.shift_forward_to_neut()
	time.sleep(0.1)
	TARS_Servo_Controller.down_to_neut()

def turnRight():
	TARS_Servo_Controller.neut_to_down()
	TARS_Servo_Controller.legsTurnRight()
	TARS_Servo_Controller.down_to_neut()
	TARS_Servo_Controller.legsFromRtoN()

def turnLeft():
	TARS_Servo_Controller.neut_to_down()
	TARS_Servo_Controller.legsTurnLeft()
	TARS_Servo_Controller.down_to_neut()
	TARS_Servo_Controller.legsFromLtoN()

def pose():
	TARS_Servo_Controller.neut_to_up()
	TARS_Servo_Controller.shift_neut_to_forward()
	TARS_Servo_Controller.up_to_down_fast()
	
def unPose():
	TARS_Servo_Controller.down_to_up_fast()
	TARS_Servo_Controller.shift_forward_to_midmod()
	TARS_Servo_Controller.up_to_down_fast()
	TARS_Servo_Controller.shift_midmod_to_neutral()
	TARS_Servo_Controller.down_to_neut()


