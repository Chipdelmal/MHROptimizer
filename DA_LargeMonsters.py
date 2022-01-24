
import aux
import pandas as pd


###############################################################################
# Tobi-Kadachi
###############################################################################
name = 'Tobi-Kadachi'
tobiKadachi_lo = '''
tobi kadachi pelt monster hunter rise wiki guideTobi-Kadachi Pelt 	13% 	12% 	70% (Back), 20% (Tail) 	27% (Body) 	35%
tobi kadachi scale monster hunter rise wiki guideTobi-Kadachi Scale 	29% 	19% 	30%(x2) (Head), 30%(x1) (Back), 20%(x1) (Tail) 	38% (Body) 	40%(x1), 50%(x1)
tobi kadachi membrane monster hunter rise wiki guideTobi-Kadachi Membrane 	23% 	22% 	-- 	23% (Body) 	--
tobi kadachi claw monster hunter rise wiki guideTobi-Kadachi Claw 	15% 	33% 	80% (Foreleg) 	12% (Body) 	10%(x1), 15%(x1)
tobi kadachi electrode monster hunter rise wiki guideTobi-Kadachi Electrode 	8% 	14% 	80% (Head), 80% (Tail) 	-- 	--
electro sac monster hunter rise wiki guideElectro Sac 	12% 	-- 	-- 	-- 	--
great izuchi tail monster hunter rise wiki guideWyvern Tear 	-- 	-- 	-- 	-- 	50%
'''
tobiKadachi_hi='''
tobi kadachi pelt monster hunter rise wiki guideTobi-Kadachi Pelt + 	17% 	14% 	70% (Back), 20% (Tail) 	31% (Body) 	35%
tobi kadachi scale monster hunter rise wiki guideTobi-Kadachi Scale + 	34% 	22%(x2) 	17%(x2) (Head), 30%(x1) (Back), 20%(x1) (Foreleg) 	43% (Body) 	39%(x1), 50%(x1)
tobi kadachi claw monster hunter rise wiki guideTobi-Kadachi Claw + 	24% 	34% 	80% (Foreleg) 	13% (Body) 	10%(x1), 15%(x1)
tobi kadachi electrode monster hunter rise wiki guideTobi-Kadachi Electrode + 	9% 	14% 	80% (Head), 80% (Tail) 	-- 	--
electro sac monster hunter rise wiki guideThunder Sac 	14% 	-- 	-- 	-- 	--
wyvern gem material mhr wiki guideWyvern Gem 	2% 	3% 	3% (Head) 	1% (Body) 	1%
tobi kadachi membrane monster hunter rise wiki guideTobi-Kadachi Membrane 	-- 	13%(x2) 	-- 	12%(x2) (Body) 	--
great izuchi tail monster hunter rise wiki guideWyvern Tear 	-- 	-- 	-- 	-- 	20%
great izuchi tail monster hunter rise wiki guideLarge Wyvern Tear 	-- 	-- 	-- 	-- 	30%
'''
tobiKadachi_el='''
Head 	20 	30 	0 	10 	5
Neck 	10 	20 	0 	10 	5
Torso 	5 	15 	0 	5 	0
Foreleg 	5 	15 	0 	5 	0
Back 	5 	15 	0 	5 	0
Hind Leg 	20 	30 	0 	20 	15
Tail 	15 	30 	0 	15 	10
'''
tobiKadachi_wp='''
Head 	48 	48 	45
Neck 	48 	48 	45
Torso 	45 	45 	35
Foreleg 	35 	35 	15
Back 	45 	45 	48
Hind Leg 	30 	30 	10
Tail 	65 	65 	55
'''
tst = aux.cleanMonster(tobiKadachi_hi)
df = aux.monsterToMaterials(tst, name)
pd.DataFrame(df, columns=aux.LG_COLS)