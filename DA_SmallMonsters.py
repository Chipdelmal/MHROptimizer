
import aux
import pandas as pd
from collections import OrderedDict

monsters = OrderedDict()
###############################################################################
# Monsters Database
###############################################################################
monsters['Kelbi'] = {
    'Low': 
        '''
        kelbi horn monster hunter rise wiki guideKelbi Horn 	30% 	100%
        warm pelt monster hunter rise wiki guideWarm Pelt 	45% 	--%
        raw meat monster hunter rise wiki guideRaw Meat 	10% 	--%
        white liver monster hunter rise wiki guideWhite Liver 	15% 	--%
        ''',
    'High':
        '''
        kelbi horn monster hunter rise wiki guideKelbi Horn 	30% 	100%
        high quality pelt monster hunter rise wiki guideHigh-quality Pelt 	45% 	--%
        raw meat monster hunter rise wiki guideRaw Meat 	10% 	--%
        white liver monster hunter rise wiki guideWhite Liver 	15% 	--%
        '''
}
# -----------------------------------------------------------------------------
""" monsters['Bombadgy'] = {
    'Low': 
        '''
        raw_meat-monster-hunter-rise-wiki-guideRaw Meat 	70% 	--%
        bombadgy_igniter-monster-hunter-rise-wiki-guideBombadgy Igniter 	30% 	--%
        ''',
    'High': 
        '''
        raw_meat-monster-hunter-rise-wiki-guideRaw Meat 	70% (Body) 	--%
        bombadgy_igniter-monster-hunter-rise-wiki-guideBombadgy Igniter 	30% (Body) 	--%
        '''
} """
# -----------------------------------------------------------------------------
monsters['Gargwa'] = {
    'Low': 
        '''
        gargwa feather monster hunter rise wiki guideGargwa Feather 	25%(Body) 	--%
        raw meat monster hunter rise wiki guideRaw Meat 	60%(Body) 	--%
        monster bone s monster hunter rise wiki guideMonster Bone S 	15%(Body) 	--%
        Gargwa Guano 	--% 	60%
        herb material mhr wiki guideHerb 	--% 	40%
        gargwa egg hunter rise wiki guideGargwa Egg 	--% 	100%
        Gold Gargwa Egg 	--% 	100%
        ''',
    'High': 
        '''
        gargwa feather monster hunter rise wiki guideGargwa Feather 	35% (Body) 	--%
        raw meat monster hunter rise wiki guideRaw Meat 	60% (Body) 	--%
        monster bone s monster hunter rise wiki guideMonster Bone S 	15% (Body) 	--%
        Gargwa Guano 	--% 	60%
        herb material mhr wiki guideHerb 	--% 	40%
        gargwa egg hunter rise wiki guideGargwa Egg 	--% 	100%
        Gold Gargwa Egg 	--% 	100%
        '''
}
# -----------------------------------------------------------------------------
""" monsters['Bullfango'] = {
    'Low': 
        '''
        bullfango_pelt-monster-hunter-rise-wiki-guideBullfango Pelt 	50% 	--%
        bullfango_head-material-mhr-wiki-guideBullfango Head 	20% 	--%
        sharp_fang-monster-hunter-rise-wiki-guideSharp Fang 	20% 	--%
        ''',
    'High': 
        '''
        bullfango_pelt-monster-hunter-rise-wiki-guideBullfango Pelt + 	50% 	--%
        bullfango_head-material-mhr-wiki-guideBullfango Head 	17% 	--%
        jumbo_bone-monster-hunter-rise-wiki-guideJumbo Bone 	15% 	--%
        acute_fang-monster-hunter-rise-wiki-guideAcute Fang 	18% 	--%
        '''
} """
# -----------------------------------------------------------------------------
monsters['Jagras'] = {
    'Low': 
        '''
        jagras hide monster hunter rise wiki guideJagras Hide 	53% 	--%
        jagras scale monster hunter rise wiki guideJagras Scale 	32% 	--%
        sharp claw monster hunter rise wiki guideSharp Claw 	15% 	--%
        ''',
    'High': 
        '''
        jagras hide+ material mhr wiki guideJagras Hide + 	53% 	--%
        jagras scale+ material mhr wiki guideJagras Scale + 	32% 	--%
        piercing claw monster hunter rise wiki guidePiercing Claw 	15% 	--%
        '''
}
# -----------------------------------------------------------------------------
monsters['Bnahbra'] = {
    'Low': 
        '''
        bnahabra shell monster hunter rise wiki guideBnahabra Shell 	34% 	--%
        bnahabra wing monster hunter rise wiki guideBnahabra Wing 	27% 	--%
        bnahabra stinger monster hunter rise wiki guideBnahabra Stinger 	22% 	--%
        monster fluid monster hunter rise wiki guideMonster Fluid 	17% 	--%
        ''',
    'High': 
        '''
        bnahabra carapace material mhr wiki guideBnahabra Carapace 	39% 	--%
        bnahabra wing monster hunter rise wiki guideBnahabra Wing 	19% 	--%
        bnahabra stinger monster hunter rise wiki guideBnahabra Stinger 	14% 	--%
        monster broth material mhr wiki guideMonster Broth 	28% 	--%
        '''
}
# -----------------------------------------------------------------------------
monsters['Altaroth'] = {
    'Low': 
        '''
        altaroth stomach monster hunter rise wiki guideAltaroth Stomach 	50% 	50%
        altaroth jaw monster hunter rise wiki guideAltaroth Jaw 	25% 	25%
        monster fluid monster hunter rise wiki guideMonster Fluid 	25% 	25%
        ripened mushroom monster hunter rise wiki guideRipened Mushroom 	--% 	90%
        nulberry monster hunter rise wiki guideNulberry 	--% 	90%
        honey material mhr wiki guideHoney 	--% 	90%
        fine stomach monster hunter rise wiki guideFine Stomach 	--% 	100%
        ''',
    'High': 
        '''
        quality stomach hunter rise wiki guideQuality Stomach 	55% 	55%
        altaroth jaw monster hunter rise wiki guideAltaroth Jaw 	20% 	20%
        monster broth material mhr wiki guideMonster Broth 	25% 	25%
        ripened mushroom monster hunter rise wiki guideRipened Mushroom 	--% 	90%
        nulberry monster hunter rise wiki guideNulberry 	--% 	90%
        honey material mhr wiki guideHoney 	--% 	90%
        fine stomach monster hunter rise wiki guideFine Stomach 	--% 	100%
        '''
}
# -----------------------------------------------------------------------------
""" monsters['Gajau'] = {
    'Low': 
        '''
        gajau_skin-monster-hunter-rise-wiki-guideGajau Skin 	70% 	--%
        gajau_whisker+-monster-hunter-rise-wiki-guideGajau Whisker 	20% 	--%
        sharp_fang-monster-hunter-rise-wiki-guideSharp Fang 	10% 	--%
        ''',
    'High': 
        '''
        gajau_skin-monster-hunter-rise-wiki-guideGajau Scale 	70% 	--%
        gajau_whisker+-monster-hunter-rise-wiki-guideGajau Whisker + 	20% 	--%
        acute_fang-monster-hunter-rise-wiki-guideAcute Fang 	10% 	--%
        '''
} """
# -----------------------------------------------------------------------------
monsters['Remobra'] = {
    'Low': 
        '''
        remobra hide monster hunter rise wiki guideRemobra Hide 	49% 	--%
        striped hide monster hunter rise wiki guideStriped Hide 	31% 	--%
        remobra head monster hunter rise wiki guideRemobra Head 	20% 	--%
        ''',
    'High': 
        '''
        remobra hide+ monster hunter rise wiki guideRemobra Hide + 	54% 	--%
        striped hide monster hunter rise wiki guideStriped Hide 	30% 	--%
        remobra head monster hunter rise wiki guideRemobra Head 	16% 	--%
        '''
}
# -----------------------------------------------------------------------------
""" monsters['Izuchi'] = {
    'Low': 
        '''
        Izuchi Tail 	52% 	--%
        Izuchi Pelt 	33% 	--%
        Sharp Claw 	15% 	--%
        ''',
    'High': 
        '''
        Izuchi Tail 	32% 	--%
        Izuchi Pelt + 	53% 	--%
        Piercing Claw 	15% 	--%
        '''
} """
# -----------------------------------------------------------------------------
monsters['Wroggi'] = {
    'Low': 
        '''
        wroggi scale+ material mhr wiki guideWroggi Scale 	48% 	--%
        wroggi hide monster hunter rise wiki guideWroggi Hide 	37% 	--%
        sharp fang monster hunter rise wiki guideSharp Fang 	15% 	--%
        ''',
    'High': 
        '''
        wroggi scale+ material mhr wiki guideWroggi Scale + 	60% 	--%
        wroggi hide monster hunter rise wiki guideWroggi Hide 	25% 	--%
        acute fang monster hunter rise wiki guideAcute Fang 	15% 	--%
        '''
}
# -----------------------------------------------------------------------------
""" monsters['Popo'] = {
    'Low': 
        '''
        raw_meat-monster-hunter-rise-wiki-guideRaw Meat 	41% 	--%
        popo_tongue_monster_hunter_rise_wiki_guidePopo Tongue 	53% 	--%
        jumbo_bone-monster-hunter-rise-wiki-guideJumbo Bone 	6% 	--%
        ''',
    'High': 
        '''
        raw_meat-monster-hunter-rise-wiki-guideRaw Meat 	41% 	--%
        popo_tongue_monster_hunter_rise_wiki_guidePopo Tongue 	53% 	--%
        stoutbone-material-mhr-wiki-guideStoutbone 	6% 	--%
        '''
} """
# -----------------------------------------------------------------------------
""" monsters['Anteka'] = {
    'Low': 
        '''
        raw_meat-monster-hunter-rise-wiki-guideRaw Meat 	32% 	--%
        warm_pelt-monster-hunter-rise-wiki-guideWarm Pelt 	18% 	--%
        anteka_antler-monster-hunter-rise-wiki-guideAnteka Antler 	40% 	--%
        white_liver_monster_hunter_rise_wiki_guideWhite Liver 	10% 	--%

        ''',
    'High': 
        '''
        raw_meat-monster-hunter-rise-wiki-guideRaw Meat 	32% 	--%
        high-quality_pelt-monster-hunter-rise-wiki-guideHigh-quality Pelt 	18% 	--%
        anteka_antler-monster-hunter-rise-wiki-guideAnteka Antler 	40% 	--%
        white_liver_monster_hunter_rise_wiki_guideWhite Liver 	10% 	--%
        '''
} """
# -----------------------------------------------------------------------------
monsters['Slagtoth'] = {
    'Low': 
        '''
        slagtoth_hide-monster-hunter-rise-wiki-guideSlagtoth Oil 	40% 	--%
        slagtoth_hide-monster-hunter-rise-wiki-guideSlagtoth Hide 	40% 	--%
        monster_bone_m-monster-hunter-rise-wiki-guideMonster Bone M 	5% 	--%
        raw_meat-monster-hunter-rise-wiki-guideRaw Meat 	15% 	--%
        ''',
    'High': 
        '''
        slagtoth_hide-monster-hunter-rise-wiki-guideSlagtoth Oil 	4 	34% 	--%
        slagtoth_hide-monster-hunter-rise-wiki-guideSlagtoth Hide + 	?? 	45% 	--%
        monster_bone_m-monster-hunter-rise-wiki-guideMonster Bone M 	4 	5% 	--%
        raw_meat-monster-hunter-rise-wiki-guideRaw Meat 	1 	15% 	--%
        '''
}
# -----------------------------------------------------------------------------
monsters['Kestodon'] = {
    'Low': 
        '''
        kestodon shell monster hunter rise wiki guideKestodon Shell 	80% (Body) 	--%
        kestodon scalp monster hunter rise wiki guideKestodon Scalp 	20% (Body) 	--%
        ''',
    'High': 
        '''
        kestodon carapace hunter rise wiki guideKestodon Carapace 	70% (Body) 	--%
        kestodon scalp monster hunter rise wiki guideKestodon Scalp 	30% (Body) 	--%
        '''
}
# -----------------------------------------------------------------------------
monsters['Rhenoplos'] = {
    'Low': 
        '''
        rhenoplos shell monster hunter rise wiki guideRhenoplos Shell 	35% (Body) 	--%
        rhenoplos scalp monster hunter rise wiki guideRhenoplos Scalp 	20% (Body) 	--%
        raw meat monster hunter rise wiki guideRaw Meat 	25% (Body) 	--%
        monster bone m monster hunter rise wiki guideMonster Bone M 	20% (Body) 	--%
        ''',
    'High': 
        '''
        rhenoplos shell monster hunter rise wiki guideRhenoplos Carapace 	45% (Body) 	--%
        rhenoplos scalp monster hunter rise wiki guideRhenoplos Scalp 	20% (Body) 	--%
        raw meat monster hunter rise wiki guideRaw Meat 	25% (Body) 	--%
        monster bone m monster hunter rise wiki guideMonster Bone M 	10% (Body) 	--%
        '''
}
# -----------------------------------------------------------------------------
""" monsters['Rachnoid'] = {
    'Low': 
        '''
        rachnoid_silk-monster-hunter-rise-wiki-guideRachnoid Silk 	53% (Part) 	--%
        sharp_claw-monster-hunter-rise-wiki-guideSharp Claw 	15% (Part) 	--%
        monster_fluid-monster-hunter-rise-wiki-guideMonster Fluid 	32% (Part) 	
        ''',
    'High': 
        '''
        rachnoid_silk+-material-mhr-wiki-guideRachnoid Silk + 	53% (Body) 	--%
        piercing_claw-monster-hunter-rise-wiki-guidePiercing Claw 	15% (Body) 	--%
        monster_broth-material-mhr-wiki-guideMonster Broth 	32% (Body) 	--%
        '''
} """
# -----------------------------------------------------------------------------
monsters['Uroktor'] = {
    'Low': 
        '''
        uroktor scale+ material mhr wiki guideUroktor Scale 	72% (Body) 	--%
        dragonfell berry monster hunter rise wiki guideDragonfell Berry 	10% (Body) 	--%
        sharp claw monster hunter rise wiki guideSharp Claw 	18% (Body) 	--%
        ''',
    'High': 
        '''
        uroktor scale+ material mhr wiki guideUroktor Scale + 	72% (Body) 	--%
        dragonfell berry monster hunter rise wiki guideDragonfell Berry 	10% (Body) 	--%
        piercing claw monster hunter rise wiki guidePiercing Claw 	18% (Body) 	--%
        '''
}
# -----------------------------------------------------------------------------
""" monsters['Zamite'] = {
    'Low': 
        '''
        meaty_hide-monster-hunter-rise-wiki-guideMeaty Hide 	38% (Body) 	--%
        sharqskin_scale-monster-hunter-rise-wiki-guideSharqskin Scale 	27% (Body) 	--%
        acute_fang-monster-hunter-rise-wiki-guideAcute Fang 	12% ( (Body) 	--%
        monster_guts_monster_hunter_rise_wiki_guideMonster Guts 	23% (Body) 	--%
        ''',
    'High': 
        '''
        meaty_hide+-material-mhr-wiki-guideMeaty Hide + 	40% (Body) 	--%
        sharqskin_scale-monster-hunter-rise-wiki-guideSharqskin Scale 	30% (Body) 	--%
        acute_fang-monster-hunter-rise-wiki-guideAcute Fang 	17% (Body) 	--%
        monster_guts_monster_hunter_rise_wiki_guideMonster Guts 	13% (Body) 	--%
        '''
} """
# -----------------------------------------------------------------------------
""" monsters['Ludroth'] = {
    'Low': 
        '''
        hydro_hide+-material-mhr-wiki-guideHydro Hide 	52%(Part) 	--%
        immature_sponge-monster-hunter-rise-wiki-guideImmature Sponge 	36%(Part) 	--%
        sharp_claw-monster-hunter-rise-wiki-guideSharp Claw 	12% (Part) 	--%
        ''',
    'High': 
        '''
        hydro_hide-monster-hunter-rise-wiki-guideHydro Hide + 	56%(Body) 	--%
        immature_sponge-monster-hunter-rise-wiki-guideImmature Sponge 	28%(Body) 	--%
        piercing_claw-monster-hunter-rise-wiki-guidePiercing Claw 	16%(Part) 	--%
        '''
} """
# -----------------------------------------------------------------------------
""" monsters['Baggi'] = {
    'Low': 
        '''
        Baggi Scale 	60% (Body) 	--%
        Baggi Hide 	25% (Body) 	--%
        Sharp Fang 	15% (Body) 	--%
        ''',
    'High': 
        '''
        Baggi Scale + 	48% (Body) 	--%
        Baggi Hide 	37% (Body) 	--%
        Acute Fang 	15% (Body) 	--%
        '''
} """
# -----------------------------------------------------------------------------
""" monsters['Jaggia'] = {
    'Low': 
        '''
        jaggi_hide-monster-hunter-rise-wiki-guideJaggi Hide 	38% (Body) 	--%
        jaggi_scale-monster-hunter-rise-wiki-guideJaggi Scale 	32% (Body) 	--%
        screamer_sac-monster-hunter-rise-wiki-guideScreamer Sac 	20% (Body) 	--%
        sharp_fang-monster-hunter-rise-wiki-guideSharp Fang 	10% (Body) 	--%
        ''',
    'High': 
        '''
        jaggi_hide+-material-mhr-wiki-guideJaggi Hide + 	38% (Body) 	--%
        jaggi_scale+-material-mhr-wiki-guideJaggi Scale + 	32% Body) 	--%
        screamer_sac-monster-hunter-rise-wiki-guideScreamer Sac 	20% (Body) 	--%
        acute_fang-monster-hunter-rise-wiki-guideAcute Fang 	10% (Body) 	--?%
        '''
} """
# -----------------------------------------------------------------------------
""" monsters['Jaggi'] = {
    'Low': 
        '''
        jaggi_hide-monster-hunter-rise-wiki-guideJaggi Hide 	35% (Part) 	--%
        jaggi_scale-monster-hunter-rise-wiki-guideJaggi Scale 	25% (Part) 	--%
        screamer_sac-monster-hunter-rise-wiki-guideScreamer Sac 	30% (Part) 	--%
        sharp_fang-monster-hunter-rise-wiki-guideSharp Fang 	10% (Part) 	--%
        ''',
    'High': 
        '''
        jaggi_hide+-material-mhr-wiki-guideJaggi Hide + 	35% (Part) 	--%
        jaggi_scale+-material-mhr-wiki-guideJaggi Scale + 	25% (Part) 	--%
        screamer_sac-monster-hunter-rise-wiki-guideScreamer Sac 	30% (Part) 	--%
        acute_fang-monster-hunter-rise-wiki-guideAcute Fang 	10% (Part) 	--%
        '''
} """
###############################################################################
# Test Dataframe
###############################################################################
i = -1
mEntry = list(monsters.items())[i]
(name, lo, hi) = (mEntry[0], mEntry[1]['Low'], mEntry[1]['High'])
tst = [aux.cleanMonster(x) for x in (lo, hi)]
cln = [aux.monsterToMaterials(x, '{} {}'.format(name, nme)) for (x, nme) in zip(tst, ('-', '+'))]
dfs = [pd.DataFrame(x, columns=aux.SM_COLS) for x in cln]
df = pd.concat(dfs, ignore_index=True)
df