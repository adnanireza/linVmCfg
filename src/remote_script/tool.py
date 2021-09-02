import subprocess
from remote_script.log import *

def bash(cmd):
    log_info("Sending command: <{}>".format(cmd))
    run = subprocess.run(cmd, universal_newlines = True, shell = True,\
        stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    if run.returncode or run.stderr:
        print(run.stderr)
        error_exit()
    log_debug("command output: " + run.stdout)
    return run.stdout

# def get_my_ip():
#     global my_ip
#     my_ip = bash(r"hostname -I | awk '{print $1}'")
#     log_debug("Fetched my_ip = " + my_ip)

# def get_my_name():
#     global my_name
#     my_name = bash(r'hostname')
#     log_debug("Fetched my_name = " + my_name)
