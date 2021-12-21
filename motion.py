from time import ctime
from gpiozero import MotionSensor
from main import blink

# from camera import camera
# from mail import sendmail


# GPIO pin 26
pir = MotionSensor(26)

def motion():
    while True:
        pir.wait_for_motion()
        
        timestamp = ctime().replace(" ","-").replace(":","_")
            
        image_name = "image-{}.png" .format(timestamp)
        # camera.capture('~/Desktop/IoT-project/{}' .format(image_name))    # Taking the picture of the detected motion
        
        blink(3,"red")
        file_name1 = image_name
        
        print("[INFO] Motion Detected")
        print("[INFO] Image Saved" .format(image_name))
        
        subject = "Motion Detected {}" .format(image_name)
        path_name = "~/Desktop/IoT-project/{}" .format(image_name)
        body_message = "\n Check the attachment below for the Image"

        print(subject,file_name1,path_name,body_message)
        # sendmail(subject, file_name1, path_name, body_message)
        
        pir.wait_for_no_motion()


motion()