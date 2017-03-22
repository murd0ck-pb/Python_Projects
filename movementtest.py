from sense_hat import SenseHat
from time import sleep
import sys
sense = SenseHat()

varpitch=[]
varroll=[]
maxroll=0
minroll=0
maxpitch=0
minpitch=0

try:
    # while True:
    #
    #     pitch = sense.get_orientation()['pitch']
    #     roll = sense.get_orientation()['roll']
    #     varpitch.append(pitch)
    #     varroll.append(roll)
    #     maxpitch=max(varpitch)
    #     minpitch=min(varpitch)
    #     maxroll=max(varroll)
    #     minroll=min(varroll)
    #     print("MaxPitch:" , maxpitch, "; MinPitch:", minpitch)
    #     print ("MaxRoll:" , maxroll, "; MinRoll:", minroll)
    #     sleep(0.3)

    while True:
        pitch = sense.get_orientation()['pitch']
        roll = sense.get_orientation()['roll']
        size_str =roll
        sys.stdout.write('%s\r' % size_str)
        sys.stdout.flush()
        #print("Roll:",roll, sep=' ', end='', flush=True)

except KeyboardInterrupt:
    sense.clear()
    print ("Quit")


#Roll/Pitch in range 0-360
#90-0 360-270
