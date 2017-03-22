import picamera
import time

camera = picamera.PiCamera()
camera.start_preview()
time.sleep ()
camera.stop_preview()

for i in range(1000):
    camera.capture('image %(number)d.jpg'%{'number': i})
    time.sleep (1.5)
