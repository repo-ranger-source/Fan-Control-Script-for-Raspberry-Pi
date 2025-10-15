# Fan-Control-Script-for-Raspberry-Pi

This Python script is designed for **Raspberry Pi** systems running Linux with GPIO support. It uses the [`gpiod`](https://github.com/brgl/libgpiod) library to control fans connected to GPIO pins, keeping them continuously powered on.

## Requirements:

- Raspberry Pi (any model with GPIO headers)
- Raspberry Pi OS or other Linux-based OS with GPIO support
- Python 3
- `gpiod` Python library installed:
  ```bash
  pip install gpiod

## How to Use:
git clone https://github.com/repo-ranger-source/Fan-Control-Script-for-Raspberry-Pi.git
cd Fan-Control-Script-for-Raspberry-Pi

## GPIO Pin Configuration!
The GPIO pins used in this script — GPIO 18 and GPIO 19 — are hardcoded in the following line:
FAN_PINS = [18, 19]
If you want to use different GPIO pins for your fans, you must manually edit the script and replace these values with the appropriate GPIO numbers for your setup.
