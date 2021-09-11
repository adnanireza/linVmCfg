from os import name
import os.path
from Crypto.PublicKey import ECC
from remote_script.log import *
from remote_script.init import *
from remote_script import path
from common import get_name_and_ips, text_processing
from remote_script.tool import bash

def is_public(ip, name_and_ips):
    #Check if I am public or private ip
    return list(filter(lambda x : ip == x[1], name_and_ips))[0][2] == "public"

def get_other_ips(name_and_ips):
    other_ips = list(filter(lambda x : x[1] != my_ip, name_and_ips))
    log_debug("Other IPs: " + str(other_ips))
    return other_ips

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
    log_debug("Processing vimrc file")
    vrc = path.path(".vimrc")
    rc_common(vrc, path.path("vimrc.txt"))

def bashrc(name_and_ips):
    log_debug("Processing bashrc file")
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

def gen_key():
    if os.path.isfile(path.path("id_ecdsa")):
        log_debug("Ssh key already exists. Skipping key creation.")
        return
    log_debug("Creating ssh key")
    key = ECC.generate(curve = "P-384")
    f = open(path.path("id_ecdsa"), "wt")
    f.write(key.export_key(format = "PEM"))
    f.close()
    pubkey = key.public_key()
    f = open(path.path("id_ecdsa.pub"), "wt")
    f.write(pubkey.export_key(format = "OpenSSH"))
    f.close()
    bash('chmod 600 {}'.format(path.path("id_ecdsa")))
    log_debug("Created ssh key")
