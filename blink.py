import RPi.GPIO as GPIO
from time import sleep,time,ctime

GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

starttime = time()

def blink(n, color):
    GPIO.output(12,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)
    if color == "red":
        pin = 12
    elif color == "green":
        pin = 18
    for b in range(n):
        GPIO.output(pin,GPIO.HIGH)
        sleep(0.1)
        GPIO.output(pin,GPIO.LOW)
        sleep(0.1)