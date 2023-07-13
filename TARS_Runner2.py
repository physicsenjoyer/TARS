import evdev
import time
import TARS_Servo_Abstractor
import TARS_Servo_Controller
import Final_Countdown

from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event3')

lTrg = 37
rTrg = 50
upBtn = 46
downBtn = 32
lBtn = 18
rBtn = 33
xBtn = 35
yBtn = 23
aBtn = 34
bBtn = 36
minusBtn = 49
plusBtn = 24

print(gamepad)

pose = False
toggle = True

def toggleState():
    return toggle

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == minusBtn:
                toggle = False
            if event.code == plusBtn:
                toggle = True

            if event.code == lTrg:
                print("Left Trigger")
                TARS_Servo_Abstractor.portMain()
            elif event.code == rTrg:
                print("Right Trigger")
                TARS_Servo_Abstractor.starMain()

            elif event.code == upBtn:
                print("Up - Step Forward")
                TARS_Servo_Abstractor.stepForward()
            elif event.code == downBtn:
                print("Down")
            elif event.code == lBtn:
                print("Left - Turn Left")
                TARS_Servo_Abstractor.turnLeft()
            elif event.code == rBtn:
                print("Right - Turn Right")
                TARS_Servo_Abstractor.turnRight()
            elif event.code == xBtn:
                print("X")
                TARS_Servo_Abstractor.starForarm()
            elif event.code == yBtn:
                print("Y")
                TARS_Servo_Abstractor.portForarm()
            elif event.code == aBtn:
                print("A")
                TARS_Servo_Abstractor.starHand()
            elif event.code == bBtn:
                print("B")
                TARS_Servo_Abstractor.portHand()
            elif event.code == plusBtn:
                print("+")
            elif event.code == minusBtn:
                print("-")
        elif event.value == 0:
            print("Stop")