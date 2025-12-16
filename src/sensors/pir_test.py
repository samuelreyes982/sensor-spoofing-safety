import time
import RPi.GPIO as GPIO

# PIR OUT on GPIO27 (physical pin 13)
PIN = 27

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.IN)
    try:
        while True:
            val = GPIO.input(PIN)
            print(f"motion={val}")
            time.sleep(0.5)
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()

