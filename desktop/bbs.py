import random
import item

class BBS:
    def __init__(self,phone_number,board_name,has_ident):
        self.phone = phone_number
        self.bname = board_name
        self.identify = has_ident
        self.file_list = item.make_file_list(random.randint(5,50))
bbs_connnected = None

bbs_list = []
bbs_list.append(BBS(585,'Free File Farm',True))
bbs_list.append(BBS(223,'Goose Roost',False))
bbs_list.append(BBS(233,'Daves Castle',False))
bbs_list.append(BBS(224,'The Crystal Palace',False))
bbs_list.append(BBS(225,'Magic Carpet',False))

def lookup(pnum):
    global bbs_connected
    name = 'dial again'
    for index,bbs in enumerate(bbs_list):
        if bbs.phone == pnum:
            name = bbs.bname
            bbs_connected = index
    return name

