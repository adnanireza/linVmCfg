from logging import root
import os.path
import traceback
from remote_script.log import *

from remote_script.log import error_exit

def rootdir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

path_dict = {
    "bashrc.txt" : os.path.join(rootdir(), "data", "bashrc.txt"),
    "vimrc.txt" : os.path.join(rootdir(), "data", "vimrc.txt"),
    "ips.txt" : os.path.join(rootdir(), "data", "ips.txt"),
    ".bashrc" : os.path.join("/", "home", "mith", ".bashrc"),
    ".vimrc" : os.path.join("/", "home", "mith", ".vimrc"),
    "id_ecdsa" : os.path.join("/", "home", "mith", ".ssh", "id_ecdsa"),
    "id_ecdsa.pub" : os.path.join("/", "home", "mith", ".ssh", "id_ecdsa.pub")
}

def path(path):
    try:
        return path_dict[path]
    except KeyError as err:
        traceback.print_tb(err.__traceback__)
        log_error("Could not find path for <{}>".format(path))
        error_exit()
