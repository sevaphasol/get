import RPi.GPIO as GPIO
import time

dac    = [8, 11, 7, 1, 0, 5, 12, 6]
# number = [1,  1, 1, 1, 1, 1,  1, 1] # 255
# number = [0,  1, 1, 1, 1, 1,  1, 1] # 127
# number = [0,  0, 1, 1, 1, 1,  1, 0] # 64
# number = [0,  0, 0, 1, 1, 1,  1, 0] # 32
# number = [0,  0, 0, 0, 0, 1,  0, 1] # 5
# number = [0,  0, 0, 0, 0, 0,  0, 0] # 0 == 256

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac[0], 1)
for i in range(8): GPIO.output(dac[i], number[i])
time.sleep(10)
GPIO.cleanup()