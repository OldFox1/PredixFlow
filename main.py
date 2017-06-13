
import mraa
import json

import time
from flask import Flask
import pyupm_buzzer as upm_buzzer


app = Flask(__name__)


windmill_pin = 7
buzzer_pin = 5
led_pin = 4

windmill = mraa.Gpio(windmill_pin)
windmill.dir(mraa.DIR_OUT)

buzzer = upm_buzzer.Buzzer(buzzer_pin)
buzzer.stopSound()
buzzer.setVolume(0.9)

led = mraa.Gpio(led_pin)
led.dir(mraa.DIR_OUT)


@app.route('/windmill/start', methods=['POST'])
def start_windmill():
    windmill.write(1)
    return json.dumps({'status': 0})


@app.route('/windmill/stop', methods=['POST'])
def stop_windmill():
    start_buzzer()
    time.sleep(5)
    stop_buzzer()
    windmill.write(0)
    return json.dumps({'status': 0})


@app.route('/buzzer/start', methods=['POST'])
def start_buzzer():
    buzzer.playSound(upm_buzzer.DO, 0)
    return json.dumps({'status': 0})


# @app.route('')
@app.route('/buzzer/stop', methods=['POST'])
def stop_buzzer():
    try:
        buzzer.stopSound()
        buzzer.stopSound()
    except:
        print 'error in buzzer'
    return json.dumps({'status': 0})


@app.route('/led/start', methods=['POST'])
def start_led():
    led.write(1)
    return json.dumps({'status': 0})


@app.route('/led/stop', methods=['POST'])
def stop_led():
    led.write(0)
    return json.dumps({'status': 0})


if __name__ == "__main__":
    app.run(port=8080, host="172.16.1.122")


