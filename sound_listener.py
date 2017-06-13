
import time
import grovepi

from common import send_trigger
from settings import sound_pin

while True:
    try:
        # Read the sound level
        sound_value = grovepi.analogRead(sound_pin)

        if sound_value > 873:
            send_trigger('sound')

        time.sleep(.5)

    except IOError:
        print "Error"