import RPi.GPIO as GPIO

pins_num = {'pinA':3, 'pinB':5, 'pinC':21, 'pinD':8, 'pinE':10, 'pinF':11, 'pinG':12, 'pinDP':13}
pins_seg = {'pin_1':15, 'pin_2':16, 'pin_3':18, 'pin_4':19}

def display_0():
	GPIO.output(pins_num['pinG'], GPIO.HIGH)
	GPIO.output(pins_num['pinDP'], GPIO.HIGH)

def display_1():
    all_pi_high()
    GPIO.output(pins_num['pinB'], GPIO.LOW)
    GPIO.output(pins_num['pinC'], GPIO.LOW)
	
def display_2():
	GPIO.output(pins_num['pinC'], GPIO.HIGH)
	GPIO.output(pins_num['pinF'], GPIO.HIGH)
	GPIO.output(pins_num['pinDP'], GPIO.HIGH)
	
def display_3():
	GPIO.output(pins_num['pinE'], GPIO.HIGH)
	GPIO.output(pins_num['pinF'], GPIO.HIGH)
	GPIO.output(pins_num['pinDP'], GPIO.HIGH)

def display_4():
	GPIO.output(pins_num['pinA'], GPIO.HIGH)
	GPIO.output(pins_num['pinD'], GPIO.HIGH)
	GPIO.output(pins_num['pinE'], GPIO.HIGH)
	GPIO.output(pins_num['pinDP'], GPIO.HIGH)
	
def display_5():
	GPIO.output(pins_num['pinB'], GPIO.HIGH)
	GPIO.output(pins_num['pinE'], GPIO.HIGH)
	GPIO.output(pins_num['pinDP'], GPIO.HIGH)
	
def display_6():
	GPIO.output(pins_num['pinB'], GPIO.HIGH)
	GPIO.output(pins_num['pinDP'], GPIO.HIGH)

def display_7():
	GPIO.output(pins_num['pinD'], GPIO.HIGH)
	GPIO.output(pins_num['pinE'], GPIO.HIGH)
	GPIO.output(pins_num['pinF'], GPIO.HIGH)
	GPIO.output(pins_num['pinG'], GPIO.HIGH)
	GPIO.output(pins_num['pinDP'], GPIO.HIGH)
	
def display_8():
	GPIO.output(pins_num['pinDP'], GPIO.HIGH)


def display_9():
	GPIO.output(pins_num['pinE'], GPIO.HIGH)
	GPIO.output(pins_num['pinDP'], GPIO.HIGH)
	
def display_dp():
    all_pi_high()
    GPIO.output(pins_num['pinDP'], GPIO.LOW)

def clear():
	all_pi_high()
	print('clear the screen!')
 
def all_pi_high():
	for i in pins_num:
		GPIO.output(pins_num[i], GPIO.HIGH)

def clear_segment():
	for i in pins_seg:
		GPIO.output(pins_seg[i], GPIO.LOW)