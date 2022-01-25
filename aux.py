
import re

BASE_MONSTER_URL = 'https://monsterhunterrise.wiki.fextralife.com/'
###############################################################################
# Lists Columns
###############################################################################
GA_TYPES = ("Endemic Life", "Small Monsters", "Large Monsters", "Gathering")
BAN = {
    "monster hunter rise wiki guide": '\t', 
    "material mhr wiki guide": '\t',
    "-monster-hunter-rise-wiki-guide": '\t',
    "-material-mhr-wiki-guide": '\t',
    "_monster_hunter_rise_wiki_guide": '\t',
    "hunter rise wiki guide": '\t'
}
SM_COLS = ('Monster', 'Material', 'Carve', 'Drop')
LG_COLS =  (
    'Monster', 'Material', 'Target', 'Capture', 
    'Break Part', 'Carves', 'Dropped'
)
WPS_COLS = ('Pierce', 'Blunt', 'Projectile')
ELE_COLS = ('Fire', 'Water', 'Thunder', 'Ice', 'Dragon')

###############################################################################
# String Parsing
###############################################################################
def splitList(eleList, rePat='; |  |\n|\t'):
    strSplit = re.split(rePat, eleList) 
    return set([i.strip() for i in strSplit if len(i)>0])


def cleanMonster(mstr, ban=BAN):
    # https://stackoverflow.com/questions/8687018/how-to-replace-two-things-at-once-in-a-string
    (str, repls) = (mstr, ban)                                
    return re.sub('|'.join(re.escape(key) for key in repls.keys()),
                  lambda k: repls[k.group(0)], str) 


def monsterToMaterials(monster, name):
    cln = [i.split('\t') for i in monster.split('\n')]
    for i in cln:
        i[0] = name    
    return [i for i in cln if (len(i)>1)]