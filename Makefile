run-dev:
	watchmedo auto-restart python run.py --patterns="*.py" --recursive

run:
	WRITE_HANDLE=/sys/class/backlight/rpi_backlight/brightness \
	READ_HANDLE=/sys/class/backlight/rpi_backlight/actual_brightness \
	python3 run.py

lint:
	flake8 app/
	mypy --ignore-missing-imports app/

test: lint
