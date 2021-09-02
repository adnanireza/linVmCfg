from os import name
import sys
from remote_script import mylib
from remote_script.init import *
from remote_script import tool
from common.launch_threads import launch_threads
from remote_script.log import *

# Get name and ips from text file
name_and_ips = mylib.getips()

# Get the ips of other remote VMs
other_ips = mylib.get_other_ips(name_and_ips)

# Password for those other remove VMs
passwd = sys.argv[1]

# Get self public key
f = open("/home/mith/.ssh/id_ecdsa.pub", "r")
pubkey = f.readlines()[0]
f.close()

def ssh_copy(name, ip):
    ssh = tool.ssh_open(ip, passwd)
    cmd = 'python3 /home/mith/.cfg/remote_vm.py {}'.format(pubkey)
    log_debug("Sending ssp copy command to {}({})".format(ip, name))
    outp = tool.ssh_exec(cmd, ssh)
    log_debug("Output:<<<")
    log_debug(outp)
    log_debug(">>>Output")
    tool.ssh_close(ssh)

def dispatch_param(idx):
    return name_and_ips[idx]

# Dispatch threads to send public key to all other VMs
launch_threads(function = ssh_copy, dispatch_param = dispatch_param, num_threads = len(name_and_ips))
