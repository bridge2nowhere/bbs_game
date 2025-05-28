class BBS:
    def __init__(self,p,n):
        self.phone = p
        self.bname = n


bbs_list = []
bbs_list.append(BBS(585,'Free File Farm'))
bbs_list.append(BBS(223,'Goose Roost'))
bbs_list.append(BBS(233,'Daves Castle'))
bbs_list.append(BBS(224,'The Crystal Palace'))
bbs_list.append(BBS(225,'Magic Carpet'))

def lookup(pnum):
    name = "dial again"
    for b in bbs_list:
        if b.phone == pnum:
            name = b.bname
    return name

