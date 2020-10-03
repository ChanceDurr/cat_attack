from gpiozero import LED
from time import sleep
import time
import pigpio

class Robot():
	def __init__(self):
		self.servo_positions = [1200, 1650]
		self.servo_pins = [13, 12]
		self.pi = pigpio.pi()
		self.laser = LED(15)
		self.pi.set_servo_pulsewidth(13, 1200)
		self.pi.set_servo_pulsewidth(12, 1650)

	def move_servo(self, servo, position):
		"""Move the servo to a given position slowly"""
		if self.pi.get_servo_pulsewidth(self.servo_pins[servo]) < position:
			step = 1
		else:
			step = -1

		for i in range(self.pi.get_servo_pulsewidth(self.servo_pins[servo]), position, step):
			self.pi.set_servo_pulsewidth(self.servo_pins[servo], i)
			sleep(.01)

	def toggle_laser(self):
		"""Toggle the laser"""
		if self.laser.value == 1:
			self.laser.off()
		else:
			self.laser.on()

	def manual_movement(self, direction):
		"""Used for manual movement on the homepage by steps of 10"""
		if direction == "up":
			self.move_servo(1, self.pi.get_servo_pulsewidth(self.servo_pins[1]) + 10)
		elif direction == "down":
			self.move_servo(1, self.pi.get_servo_pulsewidth(self.servo_pins[1]) - 10)
		elif direction == "left":
			self.move_servo(0, self.pi.get_servo_pulsewidth(self.servo_pins[0]) + 10)
		elif direction == "right":
			self.move_servo(0, self.pi.get_servo_pulsewidth(self.servo_pins[0]) - 10)
		else:
			return "Something isnt right"

	def home_position(self):
		"""Sets the servo's to the desired position for the distract function"""
		self.move_servo(0, 1200)
		self.move_servo(1, 1650)

	def circles(self):
		"""Does 'circles' in an area for 10 seconds"""
		start_time = time.time()
		while time.time() - start_time < 10:
			self.move_servo(1, 1400)
			self.move_servo(0, 1100)
			self.move_servo(1, 1500)
			self.move_servo(0, 900)


	def distract(self):
		"""Combines multiple functions to grab cats attention
		and lure it off of the bed"""
		self.home_position()
		self.laser.on()
		self.move_servo(0, 900)
		self.move_servo(1, 1625)
		self.move_servo(0, 1200)
		self.move_servo(1, 1600)
		self.move_servo(0, 900)
		self.move_servo(1, 1500)
		self.circles()
		self.laser.off()
		self.home_position()
