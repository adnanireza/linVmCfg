from getips import getips
from check_ping import check_ping
from host_cfg import host_cfg
import util
import subprocess


ips = getips()
 # check_ping(list(map(lambda x : x[1], ips)))
host_cfg.host_cfg(ips)