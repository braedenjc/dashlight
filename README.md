# Dashlight
## System health at a glance

## Goal
> The idea behind it is to make it easy to see the health of your Linux computer
> at a glance through the command line or a web browser by exposing
> your computers state through /proc, /sys, and future additional inputs.

## Motivation
The idea behind it is to make it easy to see the health of your Linux computer
at a glance through the command line or a web browser by exposing
your computers state through /proc, /sys, and future additional inputs.

## Dependencies
lm-sensors

## Quick Start
Pending
## Usage
Pending
## Contributing
### Clone the repo
```bash
git clone https://github.com/braedenjc/dashlight.git
cd dashlight
```
### Submit a pull request
If you'd like to help, please fork and open a pull request on the main branch. Thank you!

## TODO
Currently, the project:
- Needs to scan a /sys/class/hwmon/ for any hwmon folders, and then parse their contents for each sensor.
- Create objects for the appropriate type of sensor.
- Identity proper separation of concerns for behaviors, such as if formatting the output of sensors should be left to the view or the model.

## Contact
You can contact me at braeden.j.christensen[at]gmail.com

## License
This project uses the [GPL-3 license](https://https//choosealicense.com/licenses/gpl-3.0/License).
