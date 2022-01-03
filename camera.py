from picamera import PiCamera
from time import ctime,sleep

camera=PiCamera()
# camera.rotation = 180

timestamp = ctime().replace(" ","-").replace(":","")
image = "Image-{}.png".format(timestamp)

camera.start_preview()
sleep(2)
camera.capture("/home/pi/Desktop/IoT-project/Photos/{}".format(image))
camera.stop_preview()