#!/usr/bin/env python3
from pin_set import init, loop
import RPi.GPIO as GPIO

try:
    init()
    loop()
except KeyboardInterrupt:
    GPIO.cleanup()
    print('Key Board Interrupt!')