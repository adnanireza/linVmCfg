import util
from common import get_name_and_ips

def getips():
    return get_name_and_ips.get_name_and_ips(util.get_path, util.failexit)
