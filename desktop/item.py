import random
import string

def make_file_list(qty):
    files = []
    items = random.randint(0,3) + 1
    for f in range(items):
        files.append(Item('rndm'))
    for f in range(qty-items):
        files.append(random.choice(file_list))
    random.shuffle(files)
    return(files)

#Each found program will have a two part name that is randomized each time the game starts

#Player Buffs/Curses Talisman = COLOR_ANIMAL.TLMN = YELLOW HUMMINGBIRD.TLMN
colorList = ['RED','YLW','BLU','GRN','IND','CER','CHA','VER','PER','CRM','MAG','SNA','CIN']
animalList = ['ADVK','AGTR','ALPC','ANTR','ANTL','ARMD','BDGR','BRCD','BAT',
            'BVER','BISN','PNTR','BBCT','BUFF','BTRF','CAML','CAT','CHTH','CHMP','CBRA','CGAR',
            'COW','COYT','CRKT','DEER','DOG','DNKY','DRGN','ELPT','FRRT','FISH','FLEA','FLY','FOX','FROG','GOAT',
            'GPHR','GRLA','HMST','HARE','HAWK','HRSE','IGNA','KNGR','LMUR','LPRD','LION','LZRD','LLMA','MNKY',
            'MOTH','MOUS','MULE','OTTR','OX','PNDA','PIG','PRPN','RBIT','RACN','RAT','RSNK','RSTR','SHEEP','SLOTH','SNAIL',
            'SNAK','SPDR','TIGR','WOLF','WMBT','ZBRA']

#Castable Spells Mesmers = GEMSTONE_CONSTILLATION.MSMR = ZIRCON_GEMINI.MSMR
#gemstoneList = ['AGATE','ALEXANDRITE','AMBER','AMETHYST','AQUAMARINE','BERYL','BLOODSTONE','CERUELEITE','CITRINE','DIAMOND','EMERALD',
#              'GARNATE','HEMATITE','JET','LAPISLAZULI', 'MALACHITE','MOONSTONE','OBSIDIAN','ONYX','PERIDOT','QUARTZ','RUBY','SAPHIRE',
#              'SPINEL','TANTALITE','TOPAZ','TOURMALINE','ZIRCON']

constList = ['ANDROMDA','ANTLIA','APUS','AQUARIUS','AQUILA','ARA','ARIES','AURIGA','BOOTES','CAELUM','CANCER','CANIS','CAPRICRN',
          'CARINA','CASSIPIA','CNTAURUS','CEPHEUS','CETUS','CIRCINUS','COLUMBA','CORVUS','CRATER','CRUX','CYGNUS','DELPHNUS','DORADO','DRACO','EQUULEUS','ERIDANUS',
          'FORNAX','GEMINI','GRUS','HERCULES','HOROLGUM','HYDRA','HYDRUS','INDUS','LACERTA','LEO','LEPUS','LIBRA','LUPUS','LYNX','LYRA','MENSA','MONOCROS',
          'MUSCA','NORMA','OCTANS','OPHIUCHUS','ORION','PAVO','PEGASUS','PERSEUS','PHOENIX','PICTOR','PISCES','PUPPIS','PYXIS','RETICULUM','SAGITTA','SAGITRIS','SCORPIUS',
          'SCULPTOR','SCUTUM','SERPENS','SEXTANS','TAURUS','TUCANA','URSA','VELA','VIRGO','VOLANS','VULPCULA']


#Player Weapons Procedures = METAL_WEAPON.PROC = TIN_FLAIL.PROC
metalList = ['TI','HG','CU','FE','AU','AG','LI','CR','CO','ZN',
            'ZR','PB','RH','PD','CD','SN','SB','W','TA','IR',
            'BI','PO']

weaponList = ['GLAIV','PIKE','HLBRD','SCYTH','BTLAX','DAGGR','CLUB','FLAIL','MACE','HAMMR','STAFF','LNSWD',
            'SWORD','TRIDN']


#stops repeat items
itemIndexMaster = []
#holds identified items if they are found again
knownItemMaster = []

#types of items to enforce good item creation
itemTypes = ['tlmn','msmr','proc','rndm']

class Item:
    def __init__(self,itemType):
        self.size = random.randint(250,4000)
        self.description = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

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
                self.id = (random.choice(colorList) + "_" + random.choice(animalList) + ".TMN").ljust(12,' ')
                self.trueID = "HEALTH_BOOST.TMN"
            elif itemType == 'proc':
                self.type = 'proc'
                self.id = (random.choice(metalList) + "_" + random.choice(weaponList) + ".PRC").ljust(12,' ')
                self.trueID = "PLUS_1_SMASHER.PRC"
            elif itemType == 'msmr':
                self.type = 'msmr'
                self.id = (random.choice(constList) + ".MSR").ljust(12,' ')
                self.trueID = "SHORT_CIRCUIT.MMR"

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

class File:
     def __init__(self,file_name, file_size, file_description):
        self.id = file_name
        self.size = file_size
        self.description = file_description


file_list = []
file_list.append(File('KEEN1.ZIP   ',1200,'Commander Keen 1'))
file_list.append(File('KEEN4.ZIP   ',2300,'Ep4:GoodbyeGalaxy'))
file_list.append(File('JILL1.ZIP   ',745,'Jill of the Jungle'))
file_list.append(File('WOLF3D.ZIP  ',2625,'Wolfenstein 3-D'))
file_list.append(File('DUKE1.ZIP   ',896,'Duke Nukem Ep1'))
file_list.append(File('MORAFFWO.ZIP',964,'Moraff\'s World'))
file_list.append(File('CATAABYS.ZIP',3590,'Catacomb Abyss'))
file_list.append(File('COSMOEP1.ZIP',964,'Cosmo\'s Cosmic Adv'))
file_list.append(File('FORDSIM1.ZIP',320,'Ford Simulator'))
file_list.append(File('FORDSIM1.ZIP',320,'Ford Simulator'))
file_list.append(File('ARCTIC1.ZIP ',811,'Arctic Adventure'))
file_list.append(File('CC1.ZIP     ',320,'Crystal Caves'))
file_list.append(File('MJRSTRKR.ZIP',1290,'Major Stryker'))
file_list.append(File('OXYD.ZIP    ',3312,'Major Stryker'))
file_list.append(File('SHOOTGAL.ZIP',545,'VGA Shooting Gallery'))
file_list.append(File('MJRSTRKR.ZIP',698,'Major Stryker'))
file_list.append(File('CDMAN.ZIP   ',699,'CD-MAN'))
file_list.append(File('REDHOOK.ZIP ',968,'Redhook\'s Revenge'))
file_list.append(File('CAPTURE1.ZIP',396,'Capture the Flag'))
file_list.append(File('PINBALL.ZIP ',614,'EGA/VGA Pinball'))
file_list.append(File('PT1.ZIP     ',275,'Pharaoh\'s Tomb'))
file_list.append(File('HHH.ZIP     ',319,'Hugo\'s House of Horror'))
file_list.append(File('SW1.ZIP     ',614,'Solar Winds Ep1'))
file_list.append(File('CRNCOB3D.ZIP',770,'Corncob 3-D'))
file_list.append(File('CVLWARST.ZIP',332,'Big Three WW2'))
file_list.append(File('BIGTHREE.ZIP',614,'EGA/VGA Pinball'))
file_list.append(File('STRATEGY.ZIP',722,'Stratego Clone'))
file_list.append(File('C_CHCKRS.ZIP',614,'Chinese Checkers'))
file_list.append(File('PRO-GOLF.ZIP',588,'PC Pro-Golf'))
file_list.append(File('DARTS.ZIP   ',927,'Darts'))
file_list.append(File('PC-POOL.ZIP ',697,'PC-Pool'))
file_list.append(File('DARTS.ZIP   ',927,'Darts'))
file_list.append(File('BASSMSTR.ZIP',729,'Bass Master'))
file_list.append(File('ULT_BJ.ZIP  ',296,'Ult Black Jack'))
file_list.append(File('DARTS.ZIP   ',927,'Darts'))
file_list.append(File('EGACSINO.ZIP',230,'Vegas EGA Casino'))
file_list.append(File('EUCHRE.ZIP  ',153,'Euchre'))
file_list.append(File('ULTRIS.ZIP  ',696,'Tetris Clone'))
file_list.append(File('ZENTRIS.ZIP ',1341,'Zentris'))
file_list.append(File('BIBLE_Q.ZIP ',927,'Bible Quiz'))
file_list.append(File('MAZE.ZIP    ',330,'Random 3D Maze'))
file_list.append(File('SCPACK1.ZIP ',927,'Sim Cities Pack'))
file_list.append(File('JNG_CRSE.ZIP',1384,'JackNicGolf Ext Crses'))
file_list.append(File('PC-RR.ZIP   ',971,'PC-Railroad Layout'))
file_list.append(File('USA_QUIZ.ZIP',1384,'Our United States'))
file_list.append(File('TRBOMENU.ZIP',824,'Turbo Menu'))
file_list.append(File('AQUA_TSR.ZIP',1384,'Aquarium Screen Saver'))
file_list.append(File('MANDLEBR.ZIP',339,'Mandlebrot Scrn Savr'))
file_list.append(File('SSPLLUS.ZIP ',394,'Screen Savers Plus'))
file_list.append(File('CATDISK.ZIP ',533,'Disk Catalog Util'))
file_list.append(File('USA_QUIZ.ZIP',1384,'Our United States'))
file_list.append(File('PK_UNZIP.EXE',675,'PK Unzip'))
file_list.append(File('TLK_KBD.ZIP ',2372,'Talking Keyboard'))
file_list.append(File('ZZT.ZIP     ',638,'ZZT'))
file_list.append(File('SFWAREFT.ZIP',9707,'SF Ware Laser Fonts'))
file_list.append(File('BANNER.ZIP  ',462,'Banner Maker'))
file_list.append(File('S_LABELS.ZIP',9707,'Simply Labels'))
file_list.append(File('WP_MACRO.ZIP',153,'Wordperfect 5.1 Macros'))
file_list.append(File('EZ-SPDSH.ZIP',856,'EZ-Spreadsheet'))
file_list.append(File('MODEM-DR.ZIP',245,'Modem Doctor'))
file_list.append(File('EXCHECK.ZIP ',921,'Express Check'))
file_list.append(File('ZIP-FNDR.ZIP',414,'Zip Key Finder'))
file_list.append(File('A86-ASSM.ZIP',2166,'Assembler/Debugger'))
file_list.append(File('VZPASCAL.ZIP',480,'Visible Pascal'))
file_list.append(File('KJVBIBLE.ZIP ',8142,'KJV Bible'))
file_list.append(File('GUITEACH.ZIP ',715,'Guitar Teacher'))
file_list.append(File('LOTTO.ZIP    ',323,'Lottery Prophet'))
file_list.append(File('GARDASST.ZIP ',224,'Gardener\'s Asst.'))
file_list.append(File('SKYGLOBE.ZIP ',877,'Skyglobe'))
file_list.append(File('FASTYPE.ZIP  ',606,'PC-Fastype Tutor'))
#Catalog Page 35
