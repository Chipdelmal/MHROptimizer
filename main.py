
import aux
import DA_FloodedForest as FloodedForest
import DA_ShrineRuins as ShrineRuins
import DA_FrostIslands as FrostIslands
import DA_SandyPlains as SandyPlains
import DA_LavaCaverns as LavaCaverns

needed = [
    'Kelbi', 'Anteka', 'Mizutsune', 'Delex', 'Icium'
]
needed = sorted(list(set(needed)))
###############################################################################
# Setup Locales to look at
###############################################################################
LOCALES = {
    "Flooded Forest": FloodedForest.locale,
    "Shrine Ruins": ShrineRuins.locale,
    "Frost Islands": FrostIslands.locale,
    "Sandy Plains": SandyPlains.locale,
    "Lava Caverns": LavaCaverns.locale
}
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