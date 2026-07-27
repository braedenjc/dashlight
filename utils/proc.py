# This Python file is used to parse information from the /proc filesystem to be
# used by other functions elsewhere.
# The Proc class is scoped to ONLY READ details from the /proc filesystem.
# Anything other work must be done outside this class.
# For sake of sanity, we are going to also use programs inside of linux
# that reads information from /proc, because some of /proc is not human
# readable.
# Maybe later, we can learn how to parse this information

class Proc:
    # Constants
    # Proc Folder Locations
    PROC_ROOT = "/proc/"

    # Proc files
    CPUINFO = "cpuinfo"
    MDSTAT = "mdstat"
