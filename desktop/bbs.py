import random
import item
import messages

class BBS:
    """class for handleing BBS objects"""
    def __init__(self,phone_number,board_name,has_ident):
        self.phone = phone_number                                           #seven digit phone number
        self.bname = board_name                                             #BBS name
        self.identify = has_ident                                           #can identify items

        self.file_list = []
        self.message_list = []

        self.visited = False

    def first_visit(self):
        self.file_list = item.make_file_list(random.randint(5,50))         #populates file list for the site including distractors
        self.message_list = messages.make_message_list()
        self.visited = True


#current site connected to
bbs_connnected = None

bbs_list = []
bbs_list.append(BBS(3526544,'Free File Farm',True))
bbs_list.append(BBS(2230412,'Goose Roost',False))
bbs_list.append(BBS(2248216,'The Crystal Palace',False))
bbs_list.append(BBS(2257446,'Magic Carpet',False))

def lookup(pnum:int)-> str:
    """function that will lookup the bbs_name currently connected to"""
    global bbs_connected
    name = 'dial again'
    for index,bbs in enumerate(bbs_list):
        if bbs.phone == pnum:
            name = bbs.bname
            bbs_connected = index
    return name

