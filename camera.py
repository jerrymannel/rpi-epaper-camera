from picamera import PiCamera
from time import gmtime, strftime, sleep

imageName = strftime("%Y-%m-%d-%H-%M-%S", gmtime()) + ".jpg"

camera = PiCamera(resolution=(212, 104), framerate=30)
camera.iso = 1000
camera.start_preview()
sleep(2)
camera.capture(imageName)
camera.stop_preview()
