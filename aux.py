
import re
# https://monsterhunterrise.wiki.fextralife.com/Locations

GA_TYPES = ["Endemic Life", "Small Monsters", "Large Monsters", "Gathering"]

def splitList(eleList, rePat='; |  |\n|\t'):
    strSplit = re.split(rePat, eleList) 
    return set([i.strip() for i in strSplit if len(i)>0])