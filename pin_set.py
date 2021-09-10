import RPi.GPIO as GPIO
import time
import random
from displayers import *

pins_num = {'pinA':3, 'pinB':5, 'pinC':21, 'pinD':8, 'pinE':10, 'pinF':11, 'pinG':12, 'pinDP':13}
pins_seg = {'pin_1':15, 'pin_2':16, 'pin_3':18, 'pin_4':19}
prev_number = -1

def init():
	GPIO.setmode(GPIO.BOARD)
	for i in pins_num:
		GPIO.setup(pins_num[i], GPIO.OUT)
	for i in pins_seg:
		GPIO.setup(pins_seg[i], GPIO.OUT)
	print('gpio init completed!')



def loop():
	while True:
		Display(random.randint(0, 9999), 1)



def Display(number, t):
	if number < 0 or number > 9999:
		print('Wrong number')
		exit(0)

	print('Display {}'.format(number))
	start = time.time()
	while True:
		for i, c in enumerate(str(number)):
			num_select(int(c))
			seg_select(i + 5 - len(str(number)))
			time.sleep(0.001)
			clear_segment()
		end = time.time()
		if end - start >= t:
			break


def num_select(number):
	for i in pins_num:
		GPIO.output(pins_num[i], GPIO.LOW)
	if number == 0:
		display_0()
	elif number == 1:
		display_1()
	elif number == 2:
		display_2()
	elif number == 3:
		display_3()
	elif number == 4:
		display_4()
	elif number == 5:
		display_5()
	elif number == 6:
		display_6()
	elif number == 7:
		display_7()
	elif number == 8:
		display_8()
	elif number == 9:
		display_9()
	else:
		clear()

def seg_select(seg):
	if seg < 0 or seg > 4:
		print('Wrong seg number.')
		exit(0)
	if seg == 1:
		GPIO.output(pins_seg['pin_1'], GPIO.HIGH)
	elif seg == 2:
		GPIO.output(pins_seg['pin_2'], GPIO.HIGH)
	elif seg == 3:
		GPIO.output(pins_seg['pin_3'], GPIO.HIGH)
	elif seg == 4:
		GPIO.output(pins_seg['pin_4'], GPIO.HIGH)

