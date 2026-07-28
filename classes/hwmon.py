# This class describes a hwmon object that the Linux
# ABI and sysfs reveals to the user.
# Inside of each hwmon there are one
# or more sensors. We need to track
# those sensors and give easy access to them.

class Hwmon:

    __hwmon_name__ = ''
    __sensors_list__ = []
