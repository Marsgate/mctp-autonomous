# mctp-autonomous
This is a programming skills run library for minecraft turning point 
which can be found [here](https://github.com/OpenGGEngine/TurningPoint)

## Setup
1. Install [autohotkey](https://www.autohotkey.com/)
2. Install [python](https://www.python.org/downloads/)
3. Download the [latest mctp version](https://github.com/Marsgate/mctp-autonomous/releases)

## Creating an autonomous
All programming should be done inside of `main.py`.
Here is a simple example:
```
import mctp as robot

robot.init(robot.Launcher.PUNCHER)
robot.drive(1000)
robot.end()
```

* The mctp library is imported to give access to all movement functions
* The `robot.init()` function must be called with whatever type of launcher you intend to use.
* The `robot.drive()` function generates a forward movement measured in milliseconds.
* The `robot.end()` function is required to make sure the autohotkey script exits properly

After saving the code in your `main.py` run the file from terminal with the command `python main.py`. This will generate a file named `autonomous.ahk` which can be run by autohotkey. By double clicking on this file, the script should start and an autohotkey icon will appear in the windows task bar. Once the script has been started, you have to reload it after each change to your autonomous program. To do this, right click on the icon and select `Reload this script`

Once you are in game, press `ctrl + j` to start the autonomous program. While the program is active, mouse and keyboard movements will still register, so be careful not to move the mouse after starting the program.

## Supported functionality
The following autonomous movements are supported:

### robot.turn(amount)
* changes the angle of the robot
* positive numbers are left
* negative numbers are right
* amount is not measured in degrees and will change depending on mouse dpi

### robot.drive(distance)
* drive the robot 
* positive numbers are foward
* negative numbers are backward
* distance is measured in milliseconds

### robot.angle(amount)
* change angle of the launcher
* positive numbers are up
* negative numbers are down
* amount is not measured in degrees and will change depending on mouse dpi

### robot.shoot(drawBackTime = 1000)
* switch to the launcher and fire a projectile
* drawBackTime will be ignored by flywheels robots
* drawBackTime defaults to a full power bow shot

### robot.cap_clip()
* switch to the cap flipper and swing

### robot.cap_push()
* switch to open hand and swing
