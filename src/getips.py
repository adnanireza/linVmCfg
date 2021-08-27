import os.path
import traceback
import re
from util import failexit

def getips(filepath = None):
    if filepath == None:
        filepath = os.path.join(os.path.dirname(__file__), "..", "data", "ips.txt")
        #print(filepath)
    try:
        f = open(filepath, "r")

    except FileNotFoundError as err:
        traceback.print_tb(err.__traceback__)
        print("Could not find file: " + filepath)
        failexit()
    
    lines = list(filter(lambda x : x[0] != "#", f.readlines()))
    lines = list(map(lambda x : x.strip("\n"), lines))
    ips = list(map(lambda x : tuple(re.split(r"\s+", x)), lines))
    if (len(ips) < 2):
        print("There must be two or more hostname/ip pairs.\nPlease check " + filepath)
        failexit()
    print(ips)
