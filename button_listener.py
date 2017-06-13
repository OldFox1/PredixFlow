
import mraa

import pyupm_grove as grove

import requests

click_url = 'http://172.16.0.236:3000/trigger'

pin_number = 8
# button = mraa.Gpio(pin_number)
# button.dir(mraa.DIR_OUT)

button = grove.GroveButton(pin_number)


# last_state = button.read(pin_number)
last_state = button.value()
try:
    print 'last button state is :: ' + last_state
except:
    print 'last button state is :: None'

print 'start listen to button...'

while(True):
    # sample = button.read(pin_number)
    sample = button.value()
    if sample != last_state:
        print 'A click was occurred!'
        last_state = sample
        try:
            requests.get(url=click_url)
        except:
            print 'Server not found url :: ' + click_url