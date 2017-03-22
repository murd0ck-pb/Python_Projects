import picamera
import time

camera = picamera.PiCamera()
camera.start_preview()
time.sleep (20)
camera.stop_preview()
