from gpiozero import Buzzer
from time import sleep

class Alarm:
	def __init__(self, buzzer, snoozeT, durationT=3, idleT=1, frequency=0.001):
		self.snoozeT = snoozeT
		self.durationT = durationT
		self.idleT = idleT
		self.frequency = frequency
		self.repetitions = int(snoozeT/(durationT+idleT))
		self.snoozed = False
		self.buzzer = buzzer

	def buzz(self):
		for rep in range(self.repetitions):
			self.buzzer.off()
			self.buzzer.beep(self.frequency,self.frequency)
			sleep(self.durationT)
			self.buzzer.off()
			sleep(self.idleT)
			#check gpio pin if on
			if self.snoozed:
				break

	def snooze(self):
		self.snoozed = True

if __name__ == "__main__":
	buzzer = Buzzer(10)
	alarm = Alarm(buzzer,60)
	alarm.buzz()

