# This class describes sensors inside of an
# hwmon instance.
# The logic is that the sensor has a name, and inputs that tell us
# the state of the sensor.
# A hwmon then collects and gives access to each sensor as a model manager.


class Sensor:
    __sensor_name__ = ''

    # This is where the sensor is in the sysfs filesystem.
    __sensor_fs_location__ = ''

    def __init__(self, name: str, sensor_location: str):
        self.__sensor_name__ = name
        self.__sensor_fs_location__ = sensor_location

    @property
    def name(self) -> str:
        return self.__sensor_name__

    @property
    def sensor_location(self) -> str:
        return self.__sensor_fs_location__

    # This probably needs to be a factory method?
    # There are lots of ways to read a sensor, after all.
    # For now, this reads a value and returns as a string,
    # But may read out differently later.
    @property
    def get_sensor_reading(self):
        reading = ''
        with open(self.__sensor_fs_location__, 'r') as sensor:
            reading = sensor.read()
        return reading.strip()
