import RPi.GPIO as GPIO
import time

def decimal2binary(decimal):
    return [int(elem) for elem in bin(decimal)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

T = float(input()) / 255

try:
    n = 0

    while True:
        n = (n + 1) % 512
        if n < 256: 
            GPIO.output(dac, decimal2binary(n))
            v = n / 256.0 * 3.3
        else:
            GPIO.output(dac, decimal2binary(511 - n))
            v = (511 - n) / 256.0 * 3.3
        print(f"{v:.4}")

        time.sleep(T)
    
finally:
    GPIO.output(dac, 0)

