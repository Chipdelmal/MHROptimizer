
import aux
import DA_FloodedForest as FloodedForest
import DA_ShrineRuins as ShrineRuins


needed = [
    'Aknosom', 'Magnamalo', 'Nargacuga'
]


LOCS = {
    "Flooded Forest": FloodedForest.locale,
    "Shrine Ruins": ShrineRuins.locale
}


presence = {}
for loc in LOCS:
    presFull = []
    for goal in needed:
        presGoal = [goal for gath in aux.GA_TYPES if (goal in LOCS[loc][gath])]
        presFull.extend(presGoal)
    presence[loc] = presFull
presence