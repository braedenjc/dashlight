# This Python file is used to parse information from the /sys filesystem to be
# used by other functions elsewhere.
# The Sys class is scoped to ONLY READ details from the /sys filesystem.
# Any other work must be done outside this class.
import re


class Sys:
    # Constants
    # Sys root folder location
    _SYS_ROOT = "/sys/"

    # Sys child folders
    _BLOCK_FOLDER = _SYS_ROOT + "block/"
    _BUS_FOLDER = _SYS_ROOT + "bus/"
    _CLASS_FOLDER = _SYS_ROOT + "class/"
    _DEV_FOLDER = _SYS_ROOT + "dev/"
    _DEVICES_FOLDER = _SYS_ROOT + "devices/"
    _FIRMWARE_FOLDER = _SYS_ROOT + "firmware/"
    _FS_FOLDER = _SYS_ROOT + "fs/"
    _HYPERVISOR_FOLDER = _SYS_ROOT + "hypervisor/"
    _KERNEL_FOLDER = _SYS_ROOT + "kernel/"
    _MODULE_FOLDER = _SYS_ROOT + "module/"
    _POWER_FOLDER = _SYS_ROOT + "power/"

    # Maintain a list of classes that the Linux machine actually has
    _DEVICES_CLASS_LIST = []

    # Regular expressions to locate particular folders.
    _MD_FOLDERS_REGEX = re.compile(r'^md[0-9]*')

    # MD getter methods, used to collect states of
    # a particular array or all arrays

    # The prameter here is the MD id number (e.g., md100) found
    # in /sys/block/
    def get_array_degraded_disk_count(self, md_id: str) -> int:
        failed_disk_count_file = open
        (
            self._SYS_ROOT + self._BLOCK_FOLDER + md_id + '/degraded',
            'r'
        )
        failed_disk_count = failed_disk_count_file.read()
        failed_disk_count_file.close()
        return int(failed_disk_count)
