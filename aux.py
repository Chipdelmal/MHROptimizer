
import re

def splitList(eleList, rePat='; | |\n|\t'):
    strSplit = re.split(rePat, eleList) 
    return [i for i in strSplit if len(i)>0]