# import logging
from remote_script.init import *

# log_level = logging.DEBUG
# logging.basicConfig(format = '[{}({})] %(levelname)s: %(message)s'.format(my_ip, my_name), level = log_level)

log_level = 1   # Can be between 1 and 3. 1=DEBUG, 2=INFO, 3=ERROR
log_prefix = '[{}({})]: '.format(my_ip, my_name)

def log_debug(msg):
    if log_level <= 1:
        print(log_prefix + msg)
    # logging.debug(msg)

def log_info(msg):
    if log_level <= 2:
        print(log_prefix + msg)
    # logging.info(msg)

def log_error(msg):
    if log_level <= 3:
        print(log_prefix + " ERROR: " + msg)
    # logging.error(msg)

def error_exit(code = -1):
    print("Exiting...")
    exit(code)