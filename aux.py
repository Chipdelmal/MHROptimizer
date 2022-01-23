
import re

GA_TYPES = ["Endemic Life", "Small Monsters", "Large Monsters", "Gathering"]


def splitList(eleList, rePat='; |  |\n|\t'):
    strSplit = re.split(rePat, eleList) 
    return set([i.strip() for i in strSplit if len(i)>0])


def cleanMonster(mstr, ban):
    (str, repls) = (mstr, ban)
    # return re.sub('|'.join(repls.keys()), lambda k: repls[k.group(0)], str)                                     
    return re.sub('|'.join(re.escape(key) for key in repls.keys()),
                  lambda k: repls[k.group(0)], str) 