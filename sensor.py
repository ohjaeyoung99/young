import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
trig = 8
echo = 25
sensor = 1
led = 24
buzzer = 18
gamgi = 23

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(gamgi, GPIO.IN)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 50)

pwm.start(0)

try:
	while True:
		GPIO.output(trig,False)
		time.sleep(0.5)
		
		GPIO.output(trig,True)
		time.sleep(0.00001)
		GPIO.output(trig,False)
		
		while GPIO.input(echo) == 0:
			pulse_start = time.time()
		
		while GPIO.input(echo) == 1:
			pulse_end = time.time()
			
		pulse_duration = pulse_end-pulse_start
		distance = pulse_duration*17000
		distance = round(distance,2)
		
		print'distance: ', distance, 'cm'
		
		if GPIO.input(sensor) == True:
			print 'Motion Detected'
			
			if distance>=15:
				pwm.ChangeDutyCycle(25)
			elif distance>=8:
				pwm.ChangeDutyCycle(50)
			else: 
				pwm.ChangeDutyCycle(100)		      						
				
		if GPIO.input(sensor) == False:
			pwm.ChangeDutyCycle(5)	
			
		
except KeyboardInterrupt:
	GPIO.cleanup()			
		
		
		
