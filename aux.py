
import re

GA_TYPES = ["Endemic Life", "Small Monsters", "Large Monsters", "Gathering"]


def splitList(eleList, rePat='; |  |\n|\t'):
    strSplit = re.split(rePat, eleList) 
    return set([i.strip() for i in strSplit if len(i)>0])


def cleanMonster(mstr, ban):
    # https://stackoverflow.com/questions/8687018/how-to-replace-two-things-at-once-in-a-string
    (str, repls) = (mstr, ban)                                
    return re.sub('|'.join(re.escape(key) for key in repls.keys()),
                  lambda k: repls[k.group(0)], str) 


def monsterToMaterials(monster):
    cln = [i.split('\t') for i in monster.split('\n')]
    return [i for i in cln if (len(i)>1)]