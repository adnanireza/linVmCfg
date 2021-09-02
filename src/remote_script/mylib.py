import os.path
from remote_script.log import *
from remote_script.init import *
from remote_script import path
from common import get_name_and_ips, text_processing
from remote_script.tool import bash

def rc_common(orig_file, new_file):
    if not os.path.isfile(orig_file):
        bash("touch {}".format(orig_file))
    f = open(orig_file, "r")
    orig_lines = f.readlines()
    f.close()
    f = open(new_file, "r")
    new_lines = f.readlines()
    f.close()
    text_processing.add_line(orig_lines, new_lines)     # This modifies the first argument
    f = open(orig_file, "w")
    f.writelines(orig_lines)
    f.close()

def vimrc():
    vrc = path.path(".vimrc")
    rc_common(vrc, path.path("vimrc.txt"))

def bashrc(name_and_ips):
    brc = path.path(".bashrc")
    rc_common(brc, path.path("bashrc.txt"))
    f = open(brc, "r")
    orig_lines = f.readlines()
    f.close()
    updated_lines = text_processing.bashrc_processing(name_and_ips, orig_lines)
    f = open(brc, "w")
    f.writelines(updated_lines)
    f.close()

def getips():
    return get_name_and_ips.get_name_and_ips(path.path, error_exit)

def ssh_key():
    bash("ssh-keygen -t ecdsa -b 384 -C adnanireza@yahoo.com")
