
import time
import grovepi

from common import send_trigger
from settings import touch_pin

while True:
    try:

        if grovepi.pinMode(touch_pin, "INPUT") == 1:
            send_trigger('touch')

        time.sleep(.5)

    except IOError:
        print "Error"

