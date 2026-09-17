# This class describes a hwmon object that the Linux
# ABI and sysfs reveals to the user.
# This hwmon object is usually a folder inside of /sys/class,
# so we make an object that represents that folder.
# Inside of each hwmon folder there are one
# or more file that tells us:
# - A name for the hwmon hardware inside
# - sensor readings
# We need to track those sensors and give easy access to them.

'''
TODO:
    - Add a method to detect all of the sensors, and designate a type of sensor
    - Implement the Factory programming pattern for use in find_sensors().
    - Load all valid sensor files
'''
from pathlib import Path
from sensors import Sensor
import os


class Hwmon:

    __hwmon_name__ = ''
    __hwmon_location__ = ''
    # Do we actually need to use a dictionary here?
    __sensors_dict__: {} = None

    def __init__(self, fs_location: Path):
        #  When we init a hwmon object, we are representing a folder that
        # that contains files, which symbolize sensor readings.
        # The process that init should follow is:
        # 1) Store the hwmon folder's location.
        # 2) Get the hwmon --DEVICE'S-- name from the hwmon folder's name file.
        # 3) Assign the name to this hwmon's object.
        # 4) Collect all of the sensor files inside of
        # the device directory, and assign names in a dict.

        self.__hwmon_location__ = fs_location
        self.__hwmon_name__ = self.__get_hwmon_name__()
        self.__sensors_dict__ = self.__find_sensors__()

    # PRIVATE METHODS:

    # A helper method to help locate the sensors inside of hwmon.
    # This helper method scans the hwmon location for sensors,
    # their file name, and then puts it into a dictionary
    # for later use.
    def __find_sensors__(self):
        hwmon_path = Path(self.__hwmon_location__)

        fileList = [
            sensor for sensor in hwmon_path.iterdir() if sensor.is_file()
            ]
        sensors_dict = dict()
        for sensorFile in fileList:
            if self.__is_valid_sensor_file__(sensorFile):
                sensors_dict[sensorFile.name] = Sensor(
                    sensorFile.name, sensorFile.absolute()
                )
        return sensors_dict

    def __get_hwmon_name__(self):
        tempName = ''
        with Path.open(self.__hwmon_location__ / "name") as hwmonName:
            tempName = hwmonName.readline().strip()
        return tempName

    # Private parser method for determining if a file is a sensor file.
    def __is_valid_sensor_file__(self, file):
        is_valid_file_size = os.path.getsize(file) > 0
        is_not_named_name = file.name != 'name'
        is_not_named_uevent = file.name != 'uevent'
        if is_valid_file_size and is_not_named_name and is_not_named_uevent:
            return True
        return False

    # PUBLIC METHODS

    def get_device_name(self):
        return self.__hwmon_name__

    def get_sensors_of_type(self):
        return None

    def get_all_sensors(self):
        return self.__sensors_dict__

    def get_sensor_reading(self, name):
        return self.__sensors_dict__[name].get_raw_sensor_reading()
