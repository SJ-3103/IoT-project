from time import ctime
from gpiozero import MotionSensor
from blink import blink

from camera import camera_fun
from mail import sendmail


# GPIO pin 4
pir = MotionSensor(4)

def motion():
    # while True:
    # pir.wait_for_motion()
    
    image_name = camera_fun()    # Taking the picture of the detected motion
    
    blink(3,"red")
    file_name1 = image_name
    
    print("[INFO] Motion Detected")
    print("[INFO] Image Saved" .format(image_name))
    
    subject = "Motion Detected {}" .format(image_name)
    path_name = "/home/pi/Desktop/IoT-project/Photos/{}" .format(image_name)
    body_message = "\n Check the attachment below for the Image"

    print(subject,file_name1,path_name,body_message)
    sendmail(subject, file_name1, path_name, body_message)
    
    # pir.wait_for_no_motion()
