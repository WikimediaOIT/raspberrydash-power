#!/usr/bin/python

"""
Simple script to turn off a TV connected to a raspbery pi.

Power Switch used:  Powerswitch tail 2
http://www.adafruit.com/product/268

pin 1 on power switch goes to pin 11 on pi
pin 2 on power swtich goes to pin 25 on pi (ground)

FIXME: Use motion sensors to detect activity and then turn the thing on - and turn it off X hours later.

"""

import RPi.GPIO as GPIO
from time import sleep, gmtime, strftime

MyPin=11

# We want it to be on 8:00am-4:59pm
OnHour=8
OffHour=17
# We want it to be OFF on Saturday and Sunday
Saturday=6 # 6th day of the week

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MyPin, GPIO.OUT)

# Get current hour and day of week
hour      = int(strftime("%H"))
dayofweek = int(strftime("%w"))

print '-'*80
print("Hour       = %s" % hour)
print("Dayofweek  = %s" % dayofweek)


if hour >= OnHour and hour < OffHour and dayofweek < Saturday:
    # turn it on
    print 'its daytime - making sure power is on'
    GPIO.output(MYPIN, True)
else:
    # turn it off
    print 'its night time - making sure power is off'
    GPIO.output(MYPIN, False)
