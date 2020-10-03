# Webpage for calling the program remotely and manually moving the servos
from flask import Flask, render_template, request
from cat_attack import *

app = Flask(__name__)

robot = Robot()

@app.route("/cat_attack")
def cat_attack():
	robot.distract()
	return("Program has been run")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/move", methods=["GET", "POST"])
def move():
	print(request.form)
	slider1 = request.form["slider1"]
	slider2 = request.form["slider2"]
	if "toggle_laser" in request.form:
		robot.toggle_laser()
	robot.move_servo(0, int(slider1))
	robot.move_servo(1, int(slider2))

	return render_template("move.html", s1=slider1, s2=slider2)

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)
