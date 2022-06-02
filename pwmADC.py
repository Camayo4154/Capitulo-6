import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time

pwm1 = "P9_14"

GPIO.setup("P9_42", GPIO.IN)

ADC.setup()
PWM.start(pwm1, 0)

print("Introduzca la frecuencia deseada:")
frec = int(input())
PWM.set_frequency(pwm1, frec)

while True:
	if GPIO.input("P9_42"):
		print("El PWM está desactivado")
		PWM.stop(pwm1)
	else:
		leer_adc = ADC.read("P9_36")
		duty = leer_adc * 100
		PWM.start(pwm1, duty, frec, 0)
		print("Ciclo de trabajo actual:", duty)
		PWM.set_duty_cycle(pwm1, duty)
	time.sleep(0.5)
