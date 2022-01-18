
import aux

endemic="""
Brewhare 	Peepersects
Butterflame 	Pincercrab
Clothfly 	Poisontoad
Cutterfly 	Regitrice
Escuregot 	Sleeptoad
Felicicrow 	Snowbeetle
Firebeetle 	Green Spiribird
Flashfly 	Orange Spiribird
Fortune Owl 	Red Spiribird
Great Wirebug 	Yellow Spiribird
Gustcrab 	Gilded Spiribug
Boulder Lizard 	Golden Spiribug
Rock Lizard 	Stinkmink
Scale Lizard 	Trapbugs
Mudbeetle 	Vigorwasp
Paratoad 	Wirebug	
"""

small="""
Altaroth
Bnahabra
Delex
Felyne
Jaggi
Jaggia
Kelbi
Kestodon
Melynx
Rachnoid
Remobra
Rhenoplos
"""

large = """
Almudron
Anjanath
Barroth
Basarios
Diablos
Kulu-Ya-Ku
Pukei-Pukei
Rajang
Rakna-Kadaki
Rathian
Tigrex
Volvidon
"""

gathering="""
Herb 	Honey
Antidote Herb 	Nitroshroom
Fire Herb 	Parashroom
Sunscorned Grass 	Mandragora
Gloamgrass Bud 	Bitterbug
Felvine 	Godbug
Might Seed 	Spider Web
Adamant Seed 	Dung
Nulberry 	Monster Bone S
Latchberry 	Eroded Skeleton
Needleberry 	Sturdy Bone 
Bomberry 	Quality Bone 
Slashberry 	Eroded Husk 
Flamenut 	Iron Ore
Blazenut 	Earth Crystal
Machalite Ore
Dragonite Ore 
Fucium Ore 
Carbalite Ore 
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