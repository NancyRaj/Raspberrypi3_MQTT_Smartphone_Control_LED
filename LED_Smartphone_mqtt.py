
# Controlling LED from smartphone via mqtt protocol
# Subscribe Client

import paho.mqtt.client as mq
import RPi.GPIO as gpio
import time
c=mq.Client()
gpio.setmode(gpio.BOARD)
pin=7
gpio.setup(pin,gpio.OUT)
c.connect('iot.eclipse.org',1883)
# C-Client object, userdata-Some user info
# flag-No of attempts client made to connect, rc-result code
# rc=0, Successful connection 
def onc(c,userdata,flag,rc):
    print('thevalue of rc is',rc)
    c.subscribe('nancy/iot')
def onm(c,userdata,msg):
    m=msg.payload.decode()
    print(m)
    if m=='a':
        gpio.output(pin,1)
    elif m=='b':
        gpio.output(pin,0)
c.on_connect=onc
c.on_message=onm
c.loop_forever()

