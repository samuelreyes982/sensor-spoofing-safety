import time
import RPi.GPIO as GPIO

# Light sensor digital output (DO) on GPIO17 (physical pin 11)
PIN = 17

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.IN)
    try:
        while True:
            val = GPIO.input(PIN)
            # Many LM393 modules output 0/LOW when light is detected; depends on trim pot.
            print(f"light_digital={val}")
            time.sleep(0.5)
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()

