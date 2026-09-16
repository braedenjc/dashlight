# This class describes sensors inside of an
# hwmon instance.
#
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

    # PRIVATE METHODS

    # This probably needs to be a factory method?
    # There are lots of ways to read a sensor, after all.
    # For now, this reads a value and returns as a string,
    # But may read out differently later.
    # We do not read and hold the sensor open. Instead, we open,
    # read the sensor value, and then close it.
    def __get_sensor_reading__(self):
        reading = ''
        with open(self.__sensor_fs_location__, 'r') as sensor:
            reading = sensor.read()
        return reading.strip()  # we remove white space just in case.

    @property
    def name(self) -> str:
        return self.__sensor_name__

    @property
    def sensor_location(self) -> str:
        return self.__sensor_fs_location__

    def get_raw_sensor_reading(self):
        return self.__get_sensor_reading__()


# A TemperatureSensor is a type of Sensor that exposes temperature
# readings from a sensor in either: Celsius or Fahrenheit.
class TemperatureSensor(Sensor):

    def __init__(self, name, sensor_location):
        self.__sensor_name__ = name
        self.__sensor_fs_location__ = sensor_location

    # Does this violate the single responsibility principle?
    def __get_celsius_reading__(self):
        return (float)(self.__get_sensor_reading__() / 100)

    def __get_fahrenheit_reading__(self):
        return (float)((self.__get_celsius_reading__() * 1.8) + 32)

    def get_sensor_reading(self, mode='c'):
        if mode == 'f':
            return self.__get_fahrenheit_reading__()
        elif mode == 'c':
            return self.__get_celsius_reading__()
        else:
            return self.__get_celsius_reading__()


# A FanSpeedPWMSensor uses a pwm sensor on the motherboard
# to read the speed of the fan it is connected to.
# This also might be the speed of the pump for a liquid cooler.
class FanSpeedPWMSensor(Sensor):

    def __init__(self, name, sensor_location):
        self.__sensor_name__ = name
        self.__sensor_fs_location__ = sensor_location

    def get_fan_speed(self):
        return float(self.__get_sensor_reading__())
