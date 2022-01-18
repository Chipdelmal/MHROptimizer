
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
Fire Herb 	Mandragora
Flowfern 	Godbug
Sunscorned Grass 	Thunderbug
Gloamgrass Bud 	Spider Web
Felvine 	Dung
Might Seed 	Iron Ore
Adamant Seed 	Earth Crystal
Nulberry 	Machalite Ore
Dragonfell Berry 	Dragonite Ore (High Rank)
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