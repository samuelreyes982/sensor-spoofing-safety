.PHONY: setup run-dht run-light run-pir

setup:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

run-dht:
	. .venv/bin/activate && python -m src.sensors.dht22_test

run-light:
	. .venv/bin/activate && python -m src.sensors.light_test

run-pir:
	. .venv/bin/activate && python -m src.sensors.pir_test

