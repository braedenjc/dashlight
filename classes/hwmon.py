# This class describes a hwmon object that the Linux
# ABI and sysfs reveals to the user.
# This hwmon object is usually a folder inside of /sys/class,
# so we make an object that represents that folder.
# Inside of each hwmon folder there are one
# or more sensors. We need to track
# those sensors and give easy access to them.

'''
TODO: Add a method to detect all of the sensors, and designate a type of sensor
        Implement the Factory programming pattern for use in find_sensors().
'''


class Hwmon:

    __hwmon_name__ = ''
    __hwmon_location = ''
    # Do we actually need to use a dictionary here?
    __sensors_dict__: {} = None

    def __init__(self, name, fs_location):
        #  When we init a hwmon object, we are representing a folder that
        # that contains files, which symbolize sensors.
        # The process that init should follow is:
        # 1) Get the hwmon folder's name.
        # 2) Get the hwmon folder's location
        # 3) Collect all of the sensors inside of
        #     hwmon inside of a dictionary.
        #     We need to detect the type of sensor we are making
        #     and add it into the sensors dict appropriately.
        #     The mapping of the sensors dict should be: (sensor name, sensor)
        self.__hwmon_name__ = name
        self.__hwmon_location__ = fs_location
        self.__sensors_dict__ = self.__find_sensors__()

    # A helper method to help locate the sensors inside of hwmon.
    def __find_sensors__():
        return None

    def get_sensors_of_type():
        return None

    def get_all_sensors():
        return None

    def get_sensor_reading(self, name):
        return self.__sensors_dict__[name].get_sensor_reading()
