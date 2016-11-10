from gpiozero import LineSensor, Motor
from signal import pause

motorL = Motor(9, 10)
motorR = Motor(7, 8)
line = LineSensor(25)

speed = 0.6

def pivotLeft():
    motorL.backward(speed)
    motorR.forward(speed)
    print("Pivoting for line...")
    line.wait_for_line
    print("Line found! stopping...")
    motorL.stop()
    motorR.stop()

def pivotRight():
    motorR.backward(speed)
    motorL.forward(speed)

def followLine():
    print("Line Detected!")
    motorL.forward(speed)
    motorR.forward(speed)
    print("Waiting for no line...")
    line.wait_for_no_line
    print("Line lost. stopping motors.")
    motorL.stop()
    motorR.stop()

def checkLine():
    motorL.stop()
    motorR.stop()
    pivotLeft()

line.when_line = followLine
line.when_no_line = pivotLeft
pause()
