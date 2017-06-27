from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (720, 480)

camera.start_preview()
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(15)
camera.stop_recording()
camera.stop_preview()
