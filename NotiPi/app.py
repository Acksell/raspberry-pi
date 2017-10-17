from gpiozero import Buzzer

from alarm import Alarm
import discordbot

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/NOTIFY")
def buzz():
	msg = request.args.get("msg")
	discordbot.post_message(msg)

	buzzer = Buzzer(10)
	alarm = Alarm(buzzer, 5)
	alarm.buzz()
	return "<h1>Du notifierade nyss Axel!</h1><p>Meddelande: {}".format(msg)
	
