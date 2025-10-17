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

1. Connect your fans to GPIO pins 18 and 19.
2. Clone this repository and navigate into the project folder:
   ```bash
   git clone https://github.com/repo-ranger-source/Fan-Control-Script-for-Raspberry-Pi.git
   cd Fan-Control-Script-for-Raspberry-Pi
3. Run the script with root privileges:
   ```bash
   sudo python3 fan_control.py

## Additional:
Use the systemd service file to automatically start your fan control Python script at system startup, ensuring your cooling system runs without manual input.
   
## GPIO Pin Configuration!
The GPIO pins used in this script — GPIO 18 and GPIO 19 — are hardcoded in the following line:
FAN_PINS = [18, 19]
If you want to use different GPIO pins for your fans, you must manually edit the script and replace these values with the appropriate GPIO numbers for your setup.
