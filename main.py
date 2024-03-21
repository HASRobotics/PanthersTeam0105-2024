#!/usr/bin/python3
import os, sys
sys.path.append("/usr/lib")
import _kipr as k
def moveForward(dist):  
    print('Moving forward', dist, 'in')
    
    k.motor(3, 100)
    k.motor(0, 100)
    k.msleep(130*dist)
    k.ao()
	#msleep(1000)


def turnLeft(deg):
    k.printf("Turning left", deg, "degrees")
    k.motor(0, 100)
    time = int(165 * deg / 9)
    k.msleep(time)
    k.ao()

def turnRight(deg):
    k.printf("Turning right", deg, "degrees")
    k.motor(3, 100)
    k.msleep(int(165 * deg/9))
    k.ao()

def armUp(servoNum):
    print('Moving servo')
    k.enable_servo(servoNum)
    k.set_servo_position(servoNum, 1000)
    k.msleep(1000)
    #k.disable_servo(servoNum)
    
def armDown(servoNum):
    print('Moving servo arm down')
    k.enable_servo(servoNum)
    k.set_servo_position(servoNum, 0)
    k.msleep(1000)
    #k.disable_servo(servoNum)

def main():
    #moveForward(12)
    #turnLeft(90)
    
    armUp(0)
    armDown(0)
    print("Drive over") 

main()




