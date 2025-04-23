import RPi.GPIO as GPIO
import time

dac    = [8, 11, 7, 1, 0, 5, 12, 6]
leds   = [2, 3, 4, 17, 27, 22, 10, 9]
comp   = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for value in range(256):
        GPIO.output(dac, decimal2binary(value))
        time.sleep(0.005)
        comp_val = GPIO.input(comp)

        if comp_val == 1:
            return value
    return 255

def volume(value):
    ret_value = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(value//32):
        ret_value[7-i] = 1
    
    return ret_value

try:
    while True:
        value = adc()
        voltage = 3.3 * value / 256.0
        print(f"{value} <---> {voltage:.2f} V")
        GPIO.output(leds, volume(value))
        time.sleep(0.01)

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
