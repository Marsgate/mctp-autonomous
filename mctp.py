from enum import Enum
import os

global f

class Launcher(Enum):
    NONE = 0
    PUNCHER = 1
    FLYWHEEL = 2

launcher_type = Launcher.NONE

# change angle of the robot
# positive numbers are left
# negative numbers are right
def turn(amount):
    f.write("DllCall(\"mouse_event\", uint, 1, int, %d, int, 0)\n" % amount)
    f.write("sleep, 100\n")

# drive the robot
# positive numbers are foward
# negative numbers are backward
def drive(amount):
    key = 'w'
    if(amount < 0):
        key = 's'

    f.write("Send {%c down}\n" % key)
    f.write("Sleep, %d\n" % amount)
    f.write("Send {%c up}\n" % key)

# change angle of the launcher
# positive numbers are up
# negative numbers are down
def angle(amount):
    f.write("DllCall(\"mouse_event\", uint, 1, int, 0, int, %d)\n" % amount)
    f.write("sleep, 100\n")

# switch to the launcher and fire a projectile
def shoot(drawBackTime = 1000):
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

# switch to the cap flipper and swing
def cap_flip():
    print("wap")


def init(L):
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