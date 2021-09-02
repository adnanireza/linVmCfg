from getips import getips
from check_ping import check_ping
from host_cfg import host_cfg
import remote_cfg

# Get list of hostname and ip from text file
name_and_ips = getips()

# Ping each one to see if connected
check_ping(list(map(lambda x : x[1], name_and_ips)))

# Configure host: bashrc, vimrc, ssh
host_cfg.host_cfg(name_and_ips)

#Configure VMs: send files, run commands to setup their bashrc, ssh etc
remote_cfg.remote_cfg(name_and_ips)

