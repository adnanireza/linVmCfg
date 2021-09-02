import traceback
import re

def get_name_and_ips(get_path, failexit):
    filepath = get_path("ips.txt")
    try:
        f = open(filepath, "r")
    except FileNotFoundError as err:
        traceback.print_tb(err.__traceback__)
        print("Could not find file: " + filepath)
        failexit()
    else:
        lines = filter(lambda x : x[0] != "#", f.readlines())
        f.close()
    
    lines = map(lambda x : x.strip("\n"), lines)
    ips = list(map(lambda x : tuple(re.split(r"\s+", x)), lines))
    return ips
