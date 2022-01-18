
import aux

endemic="""
Brewhare 	Peepersects
Butterflame 	Poisontoad
Clothfly 	Puppet Spider
Escuregot 	Sleeptoad
Felicicrow 	Snowbeetle
Firebeetle 	Green Spiribird
Flashfly 	Orange Spiribird
Fortune Owl 	Red Spiribird
Great Wirebug 	Yellow Spiribird
Golden Lampsquid 	Gilded Spiribug
Green Lampsquid 	Golden Spiribug
Red Lampsquid 	Stinkmink
Yellow Lampsquid 	Thunderbeetle
Lanternbug 	Trapbugs
Boulder Lizard 	Vigorwasp
Rock Lizard 	Wirebug
Scale Lizard 	
"""

small="""
Altaroth
Anteka
Baggi
Bnahabra
Felyne
Gajau
Izuchi
Melynx
Popo
Remobra
Zamite
"""

large = """
Aknosom
Barioth
Goss Harag
Great Baggi
Great Izuchi
Khezu
Lagombi
Magnamalo
Mizutsune
Rajang
Somnacanth
Tetranadon
Tigrex
"""

gathering="""
Herb 	Honey
Ivy 	Blue Mushroom
Sleep Herb 	Exciteshroom
Snow Herb 	Mandragora
Flowfern 	Flashbug
Sunscorned Grass 	Thunderbug
Gloamgrass Bud 	Spider Web
Felvine 	Dung
Smokenut 	Monster Bone S
Nulberry 	Dragonhusk Shard
Latchberry 	Sturdy Bone
Huskberry 	Quality Bone
Dragonstrike Nut 	Dragonbone Relic
Slashberry 	Icium
Flamenut 	Earth Crystal
Gracium
Dragonite Ore
Machalite Ore
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