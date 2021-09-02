import util
from common import get_name_and_ips

def getips():
    return get_name_and_ips.get_name_and_ips(util.get_path, util.failexit)
    # if filepath == None:
    #     filepath = util.get_path("ips.txt")
    #     #print(filepath)
    # try:
    #     f = open(filepath, "r")
    # except FileNotFoundError as err:
    #     traceback.print_tb(err.__traceback__)
    #     print("Could not find file: " + filepath)
    #     util.failexit()
    # else:
    #     lines = filter(lambda x : x[0] != "#", f.readlines())
    #     f.close()
    
    # lines = map(lambda x : x.strip("\n"), lines)
    # ips = list(map(lambda x : tuple(re.split(r"\s+", x)), lines))
    # print(ips)
    # return ips
