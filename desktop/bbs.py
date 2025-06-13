import random
import item
import messages

class BBS:
    def __init__(self,phone_number,board_name,has_ident):
        self.phone = phone_number
        self.bname = board_name
        self.identify = has_ident

        self.file_list = []
        self.message_list = []

    def first_connect(self):
        self.file_list = item.make_file_list(random.randint(5,50))
        self.message_list = messages.make_message_list()

bbs_connnected = None

bbs_list = []
bbs_list.append(BBS(3526544,'Free File Farm',True))
bbs_list.append(BBS(2230412,'Goose Roost',False))
bbs_list.append(BBS(2248216,'The Crystal Palace',False))
bbs_list.append(BBS(2257446,'Magic Carpet',False))

def lookup(pnum):
    global bbs_connected
    name = 'dial again'
    for index,bbs in enumerate(bbs_list):
        if bbs.phone == pnum:
            name = bbs.bname
            bbs_connected = index
    return name

