import time
import adafruit_dht
import board

# DHT22 DATA pin on GPIO4 (physical pin 7)
DHT = adafruit_dht.DHT22(board.D4)

def main():
    while True:
        try:
            temp_c = DHT.temperature
            humidity = DHT.humidity
            print(f"temp_c={temp_c:.2f}  humidity={humidity:.1f}")
        except RuntimeError:
            # DHT sensors are noisy; retries are normal
            pass
        time.sleep(2)

if __name__ == "__main__":
    main()

