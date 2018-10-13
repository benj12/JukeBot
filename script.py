import RPi.GPIO as GPIO
import time
import requests
import json
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

webhook_url = "https://discordapp.com/api/channels/500661295155249152/messages"
botToken = "NTAwNjY3NzU2NzUzMDU5ODQ5.DqPSJA.df72b25mJM_uyjfJBfOU3ySZdJM"

webhook = "https://discordapp.com/api/webhooks/500741204481409032/znAR90sCrJhbDn-bBPG3zTgFZfRuL_HV7T_dczLbOzTmQgdX_jb7j0SHW7RtspAgfHxV"
def sendData(data):
	payload={
		"username": "JukeBot",
		"content": data	
	}
	headers={
	"Authorization": "Bot {}".format(botToken),
	'Content-Type': 'application/json',
	}
	#response= requests.post(webhook_url, data=json.dumps(payload), headers=headers)
	response = requests.post(webhook, data=payload)
	print response

def sendPause():
	pass

def sendSkip():
	pass

def readpins():
	pass

def loop():
	while 1:
		if GPIO.input(18):
			print"Play"
			sendData("!Play")
			time.sleep(0.5)

		if GPIO.input(17):
			print"Pause"
			sendData("!Pause")
			time.sleep(0.5)

		if GPIO.input(27):
			print"Song Data"
			sendData("!SongData")
			time.sleep(0.5)

if __name__ == "__main__":
	 loop()







