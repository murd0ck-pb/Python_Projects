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

HartNew = list(Hart)

def movedown(rate):
    global Hart
    intHart = list(Hart)
    intHartNew = list(intHart)
    intHartNew[0] =  intHart[1]
    intHartNew[1] =  intHart[2]
    intHartNew[2] =  intHart[3]
    intHartNew[3] =  intHart[4]
    intHartNew[4] =  intHart[5]
    intHartNew[5] =  intHart[6]
    intHartNew[6] =  intHart[7]
    intHartNew[7] =  intHart[0]

    intHart = list(intHartNew)
    sense.set_pixels(sum( intHart,[]))
    sleep(0.5/rate)
    Hart =list(intHart)
    return Hart

def moveup(rate):
    global Hart
    intHart = list(Hart)
    intHartNew = list(intHart)
    intHartNew[0] =  intHart[7]
    intHartNew[1] =  intHart[0]
    intHartNew[2] =  intHart[1]
    intHartNew[3] =  intHart[2]
    intHartNew[4] =  intHart[3]
    intHartNew[5] =  intHart[4]
    intHartNew[6] =  intHart[5]
    intHartNew[7] =  intHart[6]

    intHart = list(intHartNew)
    sense.set_pixels(sum( intHart,[]))
    sleep(0.5/rate)
    Hart =list(intHart)
    return Hart

def moveleft(rate):
    global Hart
    HartNew=[]

    for i in range(8):
         hv1=[0,0,0,0,0,0,0,0]
         hv2=[0,0,0,0,0,0,0,0]
         hv1=list(Hart[i])

         hv2[0] =  hv1[1]
         hv2[1] =  hv1[2]
         hv2[2] =  hv1[3]
         hv2[3] =  hv1[4]
         hv2[4] =  hv1[5]
         hv2[5] =  hv1[6]
         hv2[6] =  hv1[7]
         hv2[7] =  hv1[0]

         HartNew.append(hv2)

    Hart = list(HartNew)
    i=0

    sense.set_pixels(sum( Hart,[]))

    sleep(0.5/rate)
    return Hart

def moveright(rate):
    global Hart
    HartNew=[]

    for i in range(8):
         hv1=[0,0,0,0,0,0,0,0]
         hv2=[0,0,0,0,0,0,0,0]
         hv1=list( Hart[i])

         hv2[0] =  hv1[7]
         hv2[1] =  hv1[0]
         hv2[2] =  hv1[1]
         hv2[3] =  hv1[2]
         hv2[4] =  hv1[3]
         hv2[5] =  hv1[4]
         hv2[6] =  hv1[5]
         hv2[7] =  hv1[6]

         HartNew.append( hv2)

    Hart = list( HartNew)
    i=0

    sense.set_pixels(sum( Hart,[]))

    sleep(0.5/rate)
    return Hart

try:
    while True:


#Roll/Pitch in range 0-360
#90-0 360-270

        pitch = sense.get_orientation()['pitch'] #left/right
        roll = sense.get_orientation()['roll'] #up/down

        #while 0 < pitch < 10:

        #while 350 < pitch < 360:

        #while 0 < roll < 10:

        #while 350 < roll < 360:

        if 10 < pitch < 30:
            moveleft(1)
        elif 330 < pitch < 350:
            moveright(1)

        elif 10 < roll < 30:
            moveup(1)
        elif 330 < roll < 350:
            movedown(1)

        elif 30< pitch < 50:
            moveleft(2)
        elif 310 < pitch < 330:
            moveright(2)

        elif 30 < roll < 50:
            moveup(2)
        elif 310 < roll < 330:
            movedown(2)

        elif 50< pitch < 90:
            moveleft(5)
        elif 270 < pitch < 310:
            moveright(5)

        elif 50 < roll < 90:
            moveup(5)
        elif 270 < roll < 310:
            movedown(5)


except KeyboardInterrupt:
    sense.clear()
    print ("Quit")
