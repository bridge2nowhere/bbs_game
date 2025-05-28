import random

#Each found program will have a two part name that is randomized each time the game starts

#Player Buffs/Curses Talisman = COLOR_ANIMAL.TLMN = YELLOW HUMMINGBIRD.TLMN
colorList = ['RED','YELLOW','BLUE','GREEN','INDIGO','CERULEAN','VIRIDIAN','CHARTREUSE','VERMILLION','PERIWINKLE',
            'CRIMSON','MAGENTA','SIENNA','CINNABAR']
animalList = ['AARDVARK','ALLIGATOR','ALPACA','ANACONDA','ANT','ANTEATER','ANTELOPE','ARMADILLO','BADGER','BARRACUDA','BAT',
            'BEAVER','BISON','BLACK PANTHER','BOBCAT','BUFFALO','BUTTERFLY','CAMEL','CAT','CHEETAH','CHIMPANZEE','CHIPMUNK','COBRA','COUGAR',
            'COW','COYOTE','CRICKET','CROCODILE','DEER','DOG','DONKEY','DRAGONFLY','ELEPHANT','FERRET','FISH','FLEA','FLY','FOX','FROG','GOAT',
            'GOPHER','GORILLA','HAMSTER','HARE','HAWK','HORSE','IGUANA','IMPALA','KANGAROO','LEMUR','LEOPARD','LION','LIZARD','LLAMA','MONKEY',
            'MOTH','MOUSE','MULE','OTTER','OX','PANDA','PIG','PORCUPINE','RABBIT','RACCOON','RAT','RATTLESNAKE','ROOSTER','SHEEP','SLOTH','SNAIL',
            'SNAKE','SPIDER','TIGER','WOLF','WOMBAT','ZEBRA',]

#Castable Spells Mesmers = GEMSTONE_CONSTILLATION.MSMR = ZIRCON_GEMINI.MSMR
gemstoneList = ['AGATE','ALEXANDRITE','AMBER','AMETHYST','AQUAMARINE','BERYL','BLOODSTONE','CERUELEITE','CITRINE','DIAMOND','EMERALD',
              'GARNATE','HEMATITE','JET','LAPISLAZULI', 'MALACHITE','MOONSTONE','OBSIDIAN','ONYX','PERIDOT','QUARTZ','RUBY','SAPHIRE',
              'SPINEL','TANTALITE','TOPAZ','TOURMALINE','ZIRCON']

constList = ['ANDROMEDA','ANTLIA','APUS','AQUARIUS','AQUILA','ARA','ARIES','AURIGA','BOOTES','CAELUM','CAMELOPARDALIS','CANCER','CANIS','CAPRICORNUS',
          'CARINA','CASSIOPEIA','CENTAURUS','CEPHEUS','CETUS','CIRCINUS','COLUMBA','CORVUS','CRATER','CRUX','CYGNUS','DELPHINUS','DORADO','DRACO','EQUULEUS','ERIDANUS',
          'FORNAX','GEMINI','GRUS','HERCULES','HOROLOGIUM','HYDRA','HYDRUS','INDUS','LACERTA','LEO','LEPUS','LIBRA','LUPUS','LYNX','LYRA','MENSA','MICROSCOPIUM','MONOCEROS',
          'MUSCA','NORMA','OCTANS','OPHIUCHUS','ORION','PAVO','PEGASUS','PERSEUS','PHOENIX','PICTOR','PISCES','PUPPIS','PYXIS','RETICULUM','SAGITTA','SAGITTARIUS','SCORPIUS',
          'SCULPTOR','SCUTUM','SERPENS','SEXTANS','TAURUS','TUCANA','URSA','VELA','VIRGO','VOLANS','VULPECULA']


#Player Weapons Procedures = METAL_WEAPON.PROC = TIN_FLAIL.PROC
metalList = ['TITANIUM','MERCURY','COPPER','BRASS','BRONZE','STEEL','IRON','GOLD','SILVER','LITHIUM','CHROME','COBALT','ZINC',
            'ZIRCONIUM','LEAD','PEWTER','RHODIUM','PALLADIUM','CABMIUM','TIN','ANTIMONY','TUNGSTEN','TANTALUM','IRIDIUM',
            'BISMUTH','POLONUIUM']

weaponList = ['GLAIVE','PIKE','HALBERD','SCYTHE','BATTLEAXE','DAGGER','CLUB','FLAIL','MACE','HAMMER','STAFF','LONGSWORD','ARMINGSWORD',
            'BROADSWORD','TRIDENT']


#stops repeat items
itemIndexMaster = []
#holds identified items if they are found again
knownItemMaster = []

#types of items to enforce good item creation
itemTypes = ['tlmn','msmr','proc','rndm']

class Item:
    def __init__(self,itemType):
        if itemType not in itemTypes:
           raise ValueError("not a valid type only rndm,tlmn,msmr,proc")
        else:
            #replaces rndm item types with specific type
            while itemType == "rndm":
                itemType = random.choice(itemTypes)
            #creates random item index between 1111 and FFFF and won't allow duplicates
            self.itemIndex = random.randint(4096,65534)
            while self.itemIndex in itemIndexMaster:
                self.itemIndex = random.randint(4096,65534)
            itemIndexMaster.append(self.itemIndex)

            #creates random item id and true id
            if itemType == 'tlmn':
                self.type = 'tlmn'
                self.id = random.choice(colorList) + "_" + random.choice(animalList) + ".TLMN"
                self.trueID = "HEALTH_BOOST.TLMN"
            elif itemType == 'proc':
                self.type = 'proc'
                self.id = random.choice(metalList) + "_" + random.choice(weaponList) + ".PROC"
                self.trueID = "PLUS_1_SMASHER.PROC"
            elif itemType == 'msmr':
                self.type = 'msmr'
                self.id = random.choice(gemstoneList) + "_" + random.choice(constList) + ".MSMR"
                self.trueID = "SHORT_CIRCUIT.MSMR"

            #if item has been found before, it is identified automatically
            if self.trueID in knownItemMaster:
                self.knownTrueID = True
            else:
                self.knownTrueID = False

    def identify(self):
        #identifies the item so that true id is known
        self.knownTrueID = True
        knownItemMaster.append(self.trueID)

    def itemReceipt(self):
        #handles generating item receipt data
        print(hex(self.itemIndex))
        if self.knownTrueID:
            print(self.trueID)
        else:
            print(self.id)

