
import aux

endemic="""
Antidobra 	Peepersects
Aurortle 	Rock Lizard
Blastoad 	Scale Lizard
Boulder Lizard 	Sleeptoad
Butterflame 	Snowbeetle
Clothfly 	Green Spiribird
Cutterfly 	Orange Spiribird
Escuregot 	Red Spiribird
Felicicrow 	Yellow Spiribird
Fortune Owl 	Gilded Spiribug
Giganha 	Golden Spiribug
Gilded Spiribug 	Stinkmink
Golden Spiribug 	Thunderbeetle
Great Wirebug 	Tricktoad
Lanternbug 	Vigorwasp
Mudbeetle 	Wirebug
Paratoad
"""

small="""
Altaroth
Bnahabra
Bullfango
Felyne
Gajau
Jagras
Kelbi
Ludroth
Melynx
Remobra
Slagtoth
Wroggi
"""

large = """
Almudron
Anjanath
Arzuros
Bishaten
Great Wroggi
Jyuratodus
Kulu-Ya-Ku
Mizutsune
Nargacuga
Pukei-Pukei
Rajang
Rathian
Royal Ludroth
Somnacanth
Tobi-Kadachi
Zinogre
"""

gathering="""
Herb 	Toadstool
Antidote Herb 	Exciteshroom
Ivy 	Mandragora
Sleep Herb 	Bitterbug
Snow Herb 	Godbug
Flowfern 	Flashbug
Felvine 	Thunderbug
Smokenut 	Spider Web
Nulberry 	Dung
Latchberry 	Monster Bone S
Needleberry 	Dragonhusk Shard
Blastnut 	Sturdy Bone
Flamenut 	Quality Bone
Blazenut 	Iron Ore
Honey 	Earth Crystal
Parashroom 	Machalite Ore
Lightcrystal
Dragonite Ore
Nova Crystal
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