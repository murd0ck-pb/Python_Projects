from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


r = [255,0,0]
p = [255,20,147]
e = [255,255,0]

image = [
e,e,e,e,e,e,e,e,
e,r,r,e,r,r,e,e,
r,r,r,r,r,r,r,e,
r,r,r,r,p,r,r,e,
e,r,r,p,r,r,e,e,
e,e,r,r,r,e,e,e,
e,e,e,r,e,e,e,e,
e,e,e,e,e,e,e,e,
]

back= [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
]

sense.set_pixels(image)
sleep(1)
sense.set_pixels(back)
sleep(.5)
sense.set_pixels(image)
sleep(1)
sense.set_pixels(back)
sleep(.5)
sense.set_pixels(image)
sleep(1)
sense.clear()

sense.show_message("Hallo Lisa ;)" ,text_colour=[0,0,255])

sense.set_pixels(image)
sleep(1)
sense.set_pixels(back)
sleep(.5)
sense.set_pixels(image)
sleep(1)
sense.set_pixels(back)
sleep(.5)
sense.set_pixels(image)
sleep(1)
sense.clear()
