import subprocess
import re
from platform import system
from common.launch_threads import launch_threads
from util import failexit

def check_output(outp):
    if system().lower() == "windows":
        return re.search\
            (r"Reply from [\d\.]+: bytes=[\d]+ time"\
            , outp, re.IGNORECASE)
    else:
        return re.search\
            (r"[\d]+ bytes from [\d\.]+: icmp_seq=[\d]+ ttl=[\d]+ time="\
            , outp, re.IGNORECASE)

def check_ping_core(ip):
    command = "ping {} -{} 1".format(ip, "n" if system().lower() == "windows" else "c")
    run = subprocess.run(command,\
        stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    if run.returncode == 0 and check_output(str(run.stdout)):
        print("[%s] replied to our ping" % ip)
    else:
        print("[%s] didn't reply to our ping" % ip)
        failexit()

def check_ping(ips):
    def dispatch_param(idx):
        return (ips[idx],)
    
    launch_threads(function = check_ping_core,\
        dispatch_param = dispatch_param, num_threads = len(ips))
