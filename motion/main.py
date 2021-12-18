from time import sleep,ctime
from gpiozero import MotionSensor

from camera.main import camera
from main import blink
from main.main import sendmail

pir=MotionSensor(17)

def motion():
    if pir.motion_detected:
        timestamp = ctime().replace(" ","-").replace(":","")
        
        image_name = "image-{}.png" .format(timestamp)
        camera.capture('/home/pi/Pictures/Stranger/{}' .format(image_name))    # Taking the picture of the detected motion
        
        blink(3,"red")
        file_name1 = image_name
        
        print("[INFO] Motion Detected")
        print("[INFO] Image Saved" .format(image_name))
        
        subject = "Motion Detected {}" .format(image_name)
        path_name = "/home/pi/Pictures/Stranger/{}" .format(image_name)
        body_message = "\n Check the attachment below for the Image \n Image Source: {} at /home/pi/Pictures/Stranger/" .format(image_name)

        sendmail(subject, file_name1, path_name, body_message)
        sleep(0.5) 
    else:
        return
    
    sleep(0.5)