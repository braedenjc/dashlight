# This Python file is used to parse information from the /proc filesystem to be
# used by other functions elsewhere.
# The Proc class is scoped to ONLY READ details from the /proc filesystem.
# Anything other work must be done outside this class.

class Proc:
    # Constants
    # Proc Folder Locations
    PROC_ROOT = "/proc/"
    # Proc files
    CPUINFO = "cpuinfo"
    MDSTAT = "mdstat"
