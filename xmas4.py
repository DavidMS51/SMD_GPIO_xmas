from gpiozero import LEDBoard
from gpiozero import PWMLED
from gpiozero import Button
from time import sleep
import random
import os

#setup switch and put
switch = Button(17, pull_up=True)		# used to select beween flashing and fixed glow
push = Button(4, pull_up=True)		# shut down and maybe mode change one day


def shutdown():
	print("keep holding to shut down")
	count = 20
	while  count > 0:
		sleep(.1)
		count = count - 1
		if push.is_pressed == 0:
			return
	print('shuting down now')
	os.system('sudo powerdown')
	sleep(10)			# this just keeps things clean

push.when_pressed = shutdown


def  rand():
	return random.uniform(0,3)

#main
while True:


	if switch.is_pressed:			# test for steady of flashing
		st= 1			# record current switch status	
	# setup as random as possible gentle flashing 

		#setup for indivual contrl
		led1=PWMLED(26)
		led2=PWMLED(13)
		led3=PWMLED(6)
		led4=PWMLED(19)
		led5=PWMLED(5)

		led6=PWMLED(21)
		led7=PWMLED(20)
		led8=PWMLED(16)
		led9=PWMLED(12)
		led10=PWMLED(25)

		led11=PWMLED(24)
		led12=PWMLED(23)
		led13=PWMLED(18)
		led14=PWMLED(22)
		led15=PWMLED(27)


		led1.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led2.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led3.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led4.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led5.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led6.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led7.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led8.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led9.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led10.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led11.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led12.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led13.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led14.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))
		sleep(rand())
		led15.blink(on_time=random.uniform(0.7,1.5), off_time=random.uniform(0.7,1.5), fade_in_time= random.uniform(0.15,.3), fade_out_time=random.uniform(0.15,.3))

	else:
		st= 0                   # record current switch status

		# setup steady glow

		#setup for control of all
		tree = LEDBoard(26, 13, 6, 19, 5, 21, 20, 16, 12, 25, 24, 23, 18, 22, 27, pwm=True)
		tree.on()


	while switch.is_pressed == st:		# sit in holding loop until switch is moved
		sleep(1)

	#clean everything up and start again
	if st ==0:
		tree.close()	
	else:
		led1.close()
		led2.close()
		led3.close()
		led4.close()
		led5.close()
		led6.close()
		led7.close()
		led8.close()
		led9.close()
		led10.close()
		led11.close()
		led12.close()
		led13.close()
		led14.close()
		led15.close()

