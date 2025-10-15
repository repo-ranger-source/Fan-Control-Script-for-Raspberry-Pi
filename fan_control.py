import gpiod
import signal
import sys
import time

# Configuration
FAN_PINS = [18, 19]  # GPIO 18 and GPIO 19

# Set up GPIOs
chip = gpiod.Chip("gpiochip0")
lines = [chip.get_line(pin) for pin in FAN_PINS]
for line in lines:
    line.request(consumer="fan_control", type=gpiod.LINE_REQ_DIR_OUT)
    line.set_value(1)  # Fans stay ON

print("Turning fans ON (GPIO 18 & 19)")

# Handle termination signals
def handle_exit(sig, frame):
    print("Process is exiting, but fans remain ON...")
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_exit)
signal.signal(signal.SIGINT, handle_exit)

# Keep running efficiently
while True:
    time.sleep(1)