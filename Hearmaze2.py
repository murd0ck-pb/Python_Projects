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




try:
    while True:
        HartNew=[]

        for i in range(8):
            hv1=[0,0,0,0,0,0,0,0]
            hv2=[0,0,0,0,0,0,0,0]
            hv1=list(Hart[i])

            hv2[0] = hv1[1]
            hv2[1] = hv1[2]
            hv2[2] = hv1[3]
            hv2[3] = hv1[4]
            hv2[4] = hv1[5]
            hv2[5] = hv1[6]
            hv2[6] = hv1[7]
            hv2[7] = hv1[0]

            HartNew.append(hv2)

        Hart = list(HartNew)
        i=0

        sense.set_pixels(sum(Hart,[]))

        sleep(0.5)

except KeyboardInterrupt:
    sense.clear()
    print ("Quit")
#sense.set_pixels(sum(Hart,[]))
