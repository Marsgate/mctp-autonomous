from enum import Enum
import os

global f
global slot
global sens

class Launcher(Enum):
    NONE = 0
    PUNCHER = 1
    FLYWHEEL = 2

launcher_type = Launcher.NONE

# change angle of the robot
# positive numbers are left
# negative numbers are right
def turn(amount):
    amount *= sens
    f.write("DllCall(\"mouse_event\", uint, 1, int, %d, int, 0)\n" % -amount)
    f.write("sleep, 100\n")

# drive the robot
# positive numbers are foward
# negative numbers are backward
def drive(amount):
    key = 'w'
    if(amount < 0):
        key = 's'
        amount = -amount

    f.write("Send {%c down}\n" % key)
    f.write("Sleep, %d\n" % amount)
    f.write("Send {%c up}\n" % key)

# change angle of the launcher
# positive numbers are up
# negative numbers are down
def angle(amount):
    amount *= sens
    f.write("DllCall(\"mouse_event\", uint, 1, int, 0, int, %d)\n" % -amount)
    f.write("sleep, 100\n")

# switch to the launcher and fire a projectile
def shoot(drawBackTime = 1000):
    global slot
    if (slot != 2):
        f.write("send {2}\n")
        f.write("sleep 300\n")
        slot = 2
    
    if(launcher_type == Launcher.PUNCHER):
        f.write("Click Down Right\n")
        f.write("sleep %d\n" % drawBackTime)
        f.write("Click Up Right\n")
        f.write("sleep, 100\n")  
    elif(launcher_type == Launcher.FLYWHEEL):
        f.write("Click Down Right\n")
        f.write("sleep 100\n")
        f.write("Click Up Right\n")
        f.write("sleep, 100\n")

# switch to the cap pusher and swing
def cap_flip():
    global slot
    if (slot != 3):
        f.write("send {3}\n")
        f.write("sleep 300\n")
        slot = 3

    f.write("Click Left\n")
    f.write("sleep 100\n")

# switch to open hand and swing
def cap_punch():
    global slot
    if (slot != 9):
        f.write("send {9}\n")
        f.write("sleep 300\n")
        slot = 9

    f.write("Click Left\n")
    f.write("sleep 100\n")


def init(L, scaling = 1):
    #initialize dpi
    global sens
    sens = 6.67175 * scaling

    #initialize starting slot
    global slot
    slot = 0

    #initialize the launcher type
    global launcher_type
    launcher_type = L

    # remove old file
    if os.path.exists("autonomous.ahk"):
        os.remove("autonomous.ahk")

    # create new file
    global f
    f = open("autonomous.ahk", "w")

    #write initial config
    f.write("#NoEnv\nSendMode Input\nSetWorkingDir %A_ScriptDir%\n^j::\n")

def end():
    f.write("Return")
    f.close()