import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
# GPIO.setup(10, GPIO.OUT)

con = GPIO.PWM(24, 1000)
# led = GPIO.PWM(10, 1000)
con.start(0)
# led.start(0)
try:
    while True:
        f = int(input())
        con.ChangeDutyCycle(f)
        # led.ChangeDutyCycle(f)
        print(3.3*f/100)
finally:
    con.stop()
    # led.stop()
    GPIO.cleanup()