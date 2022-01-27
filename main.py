
import aux
import pandas as pd
import DA_FloodedForest as FloodedForest
import DA_ShrineRuins as ShrineRuins
import DA_FrostIslands as FrostIslands
import DA_SandyPlains as SandyPlains
import DA_LavaCaverns as LavaCaverns

needed = [
    'Kelbi', 'Anteka', 'Mizutsune', 'Slagtoth', 'Tobi-Kadachi', 'Somnacanth',
    'Remobra'
]
needed = sorted(list(set(needed)))
###############################################################################
# Setup locales to look at
###############################################################################
LOCALES = {
    "Flooded Forest": FloodedForest.locale,
    "Shrine Ruins": ShrineRuins.locale,
    "Frost Islands": FrostIslands.locale,
    "Sandy Plains": SandyPlains.locale,
    "Lava Caverns": LavaCaverns.locale
}
###############################################################################
# Read monsters' database
###############################################################################
MNSTR_SM = pd.read_csv('./data/SmallMonsters.csv')
# Testing material filtering --------------------------------------------------
material = 'big fin'
fltr = (MNSTR_SM['Material'] == material)
MNSTR_SM[fltr]
###############################################################################
# Iterate for presence of materials
###############################################################################
presence = {}
for loc in LOCALES:
    presFull = []
    for goal in needed:
        presGoal = [
            goal for gath in aux.GA_TYPES if (goal in LOCALES[loc][gath])
        ]
        presFull.extend(presGoal)
    presence[loc] = presFull
###############################################################################
# Results
###############################################################################
presence