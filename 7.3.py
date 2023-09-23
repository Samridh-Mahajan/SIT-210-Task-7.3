# Import necessary libraries
import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM (Broadcom SOC channel)
GPIO.setmode(GPIO.BCM)

# Define pin numbers for TRIG, ECHO, and BUZZER
TRIG_PIN = 17
ECHO_PIN = 22
BUZZER_PIN = 19  # GPIO pin connected to the buzzer

# Disable GPIO warnings to suppress warnings during setup
GPIO.setwarnings(False)

# Set up GPIO pins as either outputs (OUT) or inputs (IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# Create a PWM (Pulse Width Modulation) object for the buzzer
pwm = GPIO.PWM(BUZZER_PIN, 100)  # PWM for the buzzer

# Start the PWM with a duty cycle of 0 (buzzer is off)
pwm.start(0)  # Start with no sound

try:
    while True:
        # Measure the distance using a function called measure_distance()
        distance = measure_distance()
        print(f"Distance: {distance:.2f} cm")
        time.sleep(1)

        # Calculate a value based on the distance
        value = 100 - distance
        print(value)
        time.sleep(1)

        # Control the buzzer based on the calculated value
        if 0 < value <= 100:
            pwm.ChangeDutyCycle(value)  
        else:
            pwm.ChangeDutyCycle(0)  # Turn off the buzzer
            time.sleep(0.5)

except KeyboardInterrupt:
    # Cleanup GPIO resources when the program is interrupted
    GPIO.cleanup()
