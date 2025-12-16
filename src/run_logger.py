import csv
import time
from pathlib import Path

import adafruit_dht
import board
import RPi.GPIO as GPIO

DHT = adafruit_dht.DHT22(board.D4)
LIGHT_PIN = 17
PIR_PIN = 27

OUT = Path("experiments")
OUT.mkdir(exist_ok=True)
CSV_PATH = OUT / "sensor_log.csv"

def read_dht():
    try:
        return DHT.temperature, DHT.humidity
    except RuntimeError:
        return None, None

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LIGHT_PIN, GPIO.IN)
    GPIO.setup(PIR_PIN, GPIO.IN)

    new_file = not CSV_PATH.exists()
    with CSV_PATH.open("a", newline="") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["ts", "temp_c", "humidity", "light_digital", "motion"])

        try:
            while True:
                ts = time.time()
                temp_c, humidity = read_dht()
                light = GPIO.input(LIGHT_PIN)
                motion = GPIO.input(PIR_PIN)

                w.writerow([ts, temp_c, humidity, light, motion])
                f.flush()

                print(f"ts={ts:.0f} temp_c={temp_c} hum={humidity} light={light} motion={motion}")
                time.sleep(1)
        finally:
            GPIO.cleanup()

if __name__ == "__main__":
    main()

