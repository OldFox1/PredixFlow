
import mraa

from flask import Flask


app = Flask(__name__)


windmill = mraa.Gpio(7)
windmill.dir(mraa.DIR_OUT)


def start_windmill():
    windmill.write(1)


def stop_windmill():
    windmill.write(0)




if __name__ == "__main__":
    app.run(port=80)


