from gpiozero import LED
from time import sleep
import time
import pigpio

laser = LED(15)
pi = pigpio.pi()

servo_positions = [1200, 1650]
servo_pins = [13, 12]

def move_servo(servo, position):
	"""Move the servo to a certain position slowly"""
	if servo_positions[servo] < position:
		step = 1
	else:
		step = -1

	for i in range(servo_positions[servo], position, step):
		pi.set_servo_pulsewidth(servo_pins[servo], i)
		servo_positions[servo] = i
		sleep(.01)

def home_position():
	move_servo(0, 1200)
	move_servo(1, 1650)

def circles():
	start_time = time.time()
	while time.time() - start_time < 10:
		move_servo(1, 1400)
		move_servo(0, 1100)
		move_servo(1, 1500)
		move_servo(0, 900)


def distract():
	laser.on()
	move_servo(0, 900)
	move_servo(1, 1625)
	move_servo(0, 1200)
	move_servo(1, 1600)
	move_servo(0, 900)
	move_servo(1, 1500)
	circles()
	laser.off()
	home_position()

distract()


# servo max is 2350 and min is 500
