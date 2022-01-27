
import aux
import pandas as pd


mnst = {
    'Summary':
        '''
        Enemy Type 	Large Monster
        Class 	Flying Wyvern
        Threat Level 	5
        Element 	iceblightg icon mhr wiki guideIce
        Ailment(s) 	iceblightg icon mhr wiki guideIceblight
        Weakness(es) 	fireblight icon mhr wiki guideFire
        thunderblight icon mhr wiki guideThunder
        Resistance(s) 	iceblightg icon mhr wiki guideIce
        waterblight icon mhr wiki guideWater
        dragonblight icon mhr wiki guideDragon
        Location(s) 	Frost Islands
        Rampage Role 	N/A
        ''',
    'Hitboxes':
        '''
        Head 	65 	70 	55
        Neck/Back 	30 	30 	25
        Foreleg 	40 	45 	35
        Thorns 	25 	35 	25
        Abdomen 	38 	38 	25
        Wing 	30 	45 	20
        Hind Leg 	30 	30 	25
        Tail Tip 	60 	40 	40
        ''',
    'Elements':
        '''
        Head 	20 	10 	15 	0 	15
        Neck/Back 	5 	5 	5 	0 	5
        Foreleg 	15 	0 	10 	0 	5
        Thorns 	30 	5 	25 	0 	10
        Abdomen 	10 	0 	5 	0 	5
        Wing 	10 	0 	5 	0 	5
        Hind Leg 	5 	5 	5 	0 	5
        Tail Tip 	15 	0 	10 	0 	5
        ''',
    'High':
        '''
        barioth carapace material mhr wiki guideBarioth Carapace 	21% 	-- 	20% (Head) 	39% (Body), 15% (Tail) 	32%, 55%
        barioth pelt+ material mhr wiki guideBarioth Pelt+ 	33% 	33% 	-- 	25% (Body) 	35%
        barioth claw+ material mhr wiki guideBarioth Claw+ 	12% 	18% 	70% (Thorns) 	-- 	10%
        barioth spike monster hunter rise wiki guideBarioth Spike 	8%[x2] 	6%[x2] 	30%[x2] (Thorns) 	15%[x2] (Tail) 	7%[x2], 10%[x2]
        barioth tail monster hunter rise wiki guideBarioth Tail 	5% 	12% 	-- 	65% (Tail) 	--
        frost sac monster hunter rise wiki guideFreezer Sac 	18% 	14%[x2] 	-- 	20% (Body) 	--
        wyvern gem material mhr wiki guideWyvern Gem 	3% 	3% 	5% (Head) 	1% (Body), 5% (Tail) 	1%
        amber fang+ material mhr wiki guideAmber Fang+ 	-- 	14% 	75% (Head) 	15% (Body) 	--
        great izuchi tail monster hunter rise wiki guideWyvern Tear 	-- 	-- 	-- 	-- 	15%
        great izuchi tail monster hunter rise wiki guideLarge Wyvern Tear 	-- 	-- 	-- 	-- 	35%
        ''',
    'Low':
        '''
        barioth shell monster hunter rise wiki guideBarioth Shell 	21% 	-- 	25% (Head) 	40% (Body), 10% (Tail) 	30%, 50%
        barioth pelt monster hunter rise wiki guideBarioth Pelt 	33% 	31% 	-- 	25% (Body) 	35%
        barioth claw monster hunter rise wiki guideBarioth Claw 	9% 	17% 	75% (Thorns) 	-- 	10%
        barioth spike monster hunter rise wiki guideBarioth Spike 	13% 	9% 	25% (Thorns) 	20% (Tail) 	10%, 15%
        barioth tail monster hunter rise wiki guideBarioth Tail 	8% 	16% 	-- 	70% (Tail) 	--
        frost sac monster hunter rise wiki guideFrost Sac 	16% 	14%[x2] 	-- 	20% (Body) 	--
        amber fang monster hunter rise wiki guideAmber Fang 	-- 	13% 	75% (Head) 	15% (Body) 	--
        great izuchi tail monster hunter rise wiki guideWyvern Tear 	-- 	-- 	-- 	-- 	50%
        '''
}

