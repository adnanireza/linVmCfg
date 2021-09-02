from getips import getips
from check_ping import check_ping
from host_cfg import host_cfg
from remote_cfg import remote_cfg
import util
import subprocess

from shutil import copyfile
import os

# import logging
# logging.basicConfig(format = '[myipError(myname)] %(levelname)s: %(message)s', level = logging.INFO)
# logging.error("Hi! error")
# logging.info("infoooo")
# exit()

name_and_ips = getips()
 # check_ping(list(map(lambda x : x[1], name_and_ips)))
host_cfg.host_cfg(name_and_ips)
remote_cfg.remote_cfg(name_and_ips)
# print(name_and_ips)
