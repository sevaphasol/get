# =============================================================================
# Importing needed libraries

import RPi.GPIO as GPIO
import time as time
import matplotlib.pyplot as plt

# =============================================================================
# Function for translating decimal number to binary array.

def decimal_to_binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

# =============================================================================
# Function for finding the voltage of troyka module.

def adc():
    value = 0

    for i in range(7, -1, -1):
        test_value = value + 2**i

        GPIO.output(dac, decimal_to_binary(test_value))
        time.sleep(0.01)
    
        if GPIO.input(comp) == 1:
            value = test_value
    
    return value

# =============================================================================
# Function for setting dac according to value.

def set_dac(value):
    GPIO.output(dac, decimal_to_binary(value))

# =============================================================================
# Function for printing voltage of troyka module voltage.
# Although write this voltage and elapsed time to corresponding lists.

def get_voltages(start_time):
    value = adc()
    print("voltage = {:.2f}".format(value / 255 * 3.3))
    
    set_dac(value)
    
    voltage.append(value)
    timing.append(time.time() - start_time)
    
    return value

# =============================================================================
# Main body of this programm.
# -----------------------------------------------------------------------------
# Initing GPIO ports

dac    = [26, 19, 13, 6, 5, 11, 9, 10]
leds   = [21, 20, 16, 12, 7, 8, 25, 24]
comp   = 4
troyka = 17

# -----------------------------------------------------------------------------
# Setting GPIO ports

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

# -----------------------------------------------------------------------------
# Arrays for measuring data

voltage = []
timing  = []

# -----------------------------------------------------------------------------
# Initing some constants

max_voltage = 220 # Maximal voltage on the capacitor.
min_voltage = 30  # Minimal voltage on the capacitor. 

# -----------------------------------------------------------------------------

try:
    # -------------------------------------------------------------------------
    # Setting value - voltage on the capacitor.

    value = 0

    # -------------------------------------------------------------------------
    # Start charging of the capacitor.

    print("The capacitor is charging")
    GPIO.output(troyka, 1)

    # -------------------------------------------------------------------------
    # Start timer.

    start_time = time.time()

    # -------------------------------------------------------------------------
    # Measure data while capacitor is charging.

    while(value < max_voltage):
        value = get_voltages(start_time)

    # -------------------------------------------------------------------------
    # Start discharging of the capacitor.

    print("The capacitor is discharging")
    GPIO.output(troyka, 0)

    # -------------------------------------------------------------------------
    # Measure data while capacitor is discharging.

    while(value > min_voltage):
        value = get_voltages(start_time)

    # -------------------------------------------------------------------------
    # Working with measured data.

    elapsed_time = time.time() - start_time

    with open("settings.txt", "w") as file:
        file.write(f"{str(elapsed_time)} {str(3.3/256)}")

    print(f"elapsed time = {elapsed_time} s\n"
          f"frequency    = {len(voltage) / elapsed_time} Hz\n")

# -----------------------------------------------------------------------------
# Cleaning up GPIO ports.

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()

# -----------------------------------------------------------------------------
# Plotting a graph

timing_str  = [str(item) for item in timing]
voltage_str = [str(item) for item in voltage]

with open("data.txt", "w") as file:
    file.write("\n".join(voltage_str))

plt.plot(timing, voltage)
plt.savefig("graph.png")
plt.show()

# =============================================================================