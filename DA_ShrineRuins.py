
import aux

endemic="""
Antidobra 	Peepersects
Blastoad 	Poisontoad
Brewhare 	Puppet Spider
Butterflame 	Snowbeetle
Clothfly 	Green Spiribird
Cutterfly 	Orange Spiribird
Escuregot 	Red Spiribird
Felicicrow 	Yellow Spiribird
Firebeetle 	Gilded Spiribug
Flashfly 	Golden Spiribug
Fortune Owl 	Stinkmink
Great Wirebug 	Thunderbeetle
Boulder Lizard 	Trapbugs
Rock Lizard 	Vigorwasp
Scale Lizard 	Wailnard
Mudbeetle 	Wirebug
"""

small="""
Altaroth
Bnahabra
Bombadgy
Bullfango
Felyne
Gajau
Gargwa
Izuchi
Jagras
Kelbi
Melynx
Remobra
Wroggi
"""

large = """
Aknosom
Almudron
Anjanath
Arzuros
Bishaten
Great Izuchi
Great Wroggi
Kulu-Ya-Ku
Magnamalo
Mizutsune
Nargacuga
Pukei-Pukei
Rajang
Rathalos
Rathian
Tetranadon
Tobi-Kadachi
Zinogre
"""

gathering="""
Herb 	Honey
Antidote Herb 	Blue Mushroom
Fire Herb 	Nitroshroom
Ivy 	Parashroom
Sleep Herb 	Toadstool
Flowfern 	Exciteshroom
Felvine 	Mandragora
Might Seed 	Bitterbug
Adamant Seed 	Godbug
Nulberry 	Flashbug
Latchberry 	Thunderbug
Huskberry 	Spider Web
Needleberry 	Monster Bone S
Bomberry 	Twisted Remains
Blastnut 	Sturdy Bone (High Rank)
Dragonstrike Nut 	Quality Bone (High Rank)
Slashberry 	 Twisted Rockbone (High Rank)
Flamenut 	Iron Ore
Earth Crystal
Dragonite Ore (High Rank)
Carbalite Ore (High Rank)
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