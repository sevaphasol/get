import RPi.GPIO as GPIO

def decimal2binary(decimal):
    return [int(elem) for elem in bin(decimal)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        n = input("Enter integer (q for quit): ")

        try:
            n = int(n)

            if n != n % 256:
                print("must be from 0 to 255")
                continue 

            GPIO.output(dac, decimal2binary(n))

            v = n / 256.0 * 3.3
            print(f"{v:.4}")

        except Exception:
            if n == "q":
                break
            print("must be integer") 
finally:
    GPIO.output(dac, 0)

