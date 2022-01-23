
import aux
import pandas as pd

BAN = {
    "monster hunter rise wiki guide": '\t', 
    "material mhr wiki guide": '\t'
}
COLS = ['monster', 'material', 'carve', 'drop']

###############################################################################
# Bnahbra
###############################################################################
bnahbra_hi = '''
bnahabra carapace material mhr wiki guideBnahabra Carapace 	39% 	--%
bnahabra wing monster hunter rise wiki guideBnahabra Wing 	19% 	--%
bnahabra stinger monster hunter rise wiki guideBnahabra Stinger 	14% 	--%
monster broth material mhr wiki guideMonster Broth 	28% 	--%
'''
bnahbra_lo = '''
bnahabra shell monster hunter rise wiki guideBnahabra Shell 	34% 	--%
bnahabra wing monster hunter rise wiki guideBnahabra Wing 	27% 	--%
bnahabra stinger monster hunter rise wiki guideBnahabra Stinger 	22% 	--%
monster fluid monster hunter rise wiki guideMonster Fluid 	17% 	--%
'''


tst = aux.cleanMonster(bnahbra_hi, BAN)
df = aux.monsterToMaterials(tst)

pd.DataFrame(df, columns=COLS)