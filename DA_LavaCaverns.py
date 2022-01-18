
import aux

endemic="""
Antidobra 	Scale Lizard
Aurortle 	Mudbeetle
Blastoad 	Paratoad
Butterflame 	Peepersects
Clothfly 	Puppet Spider
Cutterfly 	Green Spiribird
Echobat 	Orange Spiribird
Felicicrow 	Red Spiribird
Firebeetle 	Yellow Spiribird
Flashfly 	Gilded Spiribug
Fortune Owl 	Golden Spiribug
Great Wirebug 	Stinkmink
Gustcrab 	Thunderbeetle
Lanternbug 	Vigorwasp
Boulder Lizard 	Wirebug
Rock Lizard 	
"""

small="""
Altaroth
Bnahabra
Felyne
Gajau
Ludroth
Melynx
Rachnoid
Remobra
Rhenoplos
Slagtoth
Uroktor
Wroggi
"""

large = """
Anjanath
Basarios
Great Wroggi
Khezu
Kulu-Ya-Ku
Magnamalo
Rajang
Rakna-Kadaki
Rathalos
Rathian
"""

gathering="""
Herb 	Honey
Antidote Herb 	Nitroshroom
Fire Herb 	Mandragora
Flowfern 	Godbug
Sunscorned Grass 	Thunderbug
Gloamgrass Bud 	Spider Web
Felvine 	Dung
Might Seed 	Iron Ore
Adamant Seed 	Earth Crystal
Nulberry 	Machalite Ore
Dragonfell Berry 	Dragonite Ore
Latchberry 	Firestone
Huskberry 	Firecell Stone (High Rank)
Bomberry 	Fucium Ore (High Rank)
Blastnut 	Carbalite Ore (High Rank)
Flamenut 	Monster Bone S
Blazenut 	Dragonhusk Shard
Sturdy Bone
Quality Bone (High Rank)
Dragonbone Relic (High Rank)
"""

###############################################################################
# Locale Dictionary
###############################################################################
locale = {
    "Endemic Life": aux.splitList(endemic),
    "Small Monsters": aux.splitList(small),
    "Large Monsters": aux.splitList(large),
    "Gathering": aux.splitList(gathering)
}