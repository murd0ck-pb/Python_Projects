from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()


r = [255,0,0]
p = [255,20,147]
e = [255,255,0]

Hart = [
[e,e,e,e,e,e,e,e,],
[e,r,r,e,r,r,e,e,],
[r,r,r,r,r,r,r,e,],
[r,r,r,r,p,r,r,e,],
[e,r,r,p,r,r,e,e,],
[e,e,r,r,r,e,e,e,],
[e,e,e,r,e,e,e,e,],
[e,e,e,e,e,e,e,e,]
]

HartNew = Hart

#print(Hart[1])

while True:
    HartNew[0] = Hart[1]
    HartNew[1] = Hart[2]
    HartNew[2] = Hart[3]
    HartNew[3] = Hart[4]
    HartNew[4] = Hart[5]
    HartNew[5] = Hart[6]
    HartNew[6] = Hart[7]
    HartNew[7] = Hart[0]

    Hart = HartNew

    sense.set_pixels(sum(Hart,[]))

    sleep(0.5)

#sense.set_pixels(sum(Hart,[]))
