import random

def make_message_list() -> 'Message[]':
    """creates a list of messages"""
    msgs = []
    #handles adds 1-4 items into the list
    #qty = random.randint(0,4+1)
    for m in range(random.randint(0,4+1)):
        index = random.randint(0,len(master_message_list))
        msgs.append(master_message_list.pop(index))
    random.shuffle(msgs)
    return(msgs)



class Message:
    """class handles message"""
    def __init__(self, chp, usr, dt, brd, sbj, pst, ):
        self.board = brd
        self.subject = sbj
        self.post = pst
        self.date = dt
        self.chapter = chp
        self.user = usr



master_message_list = []
master_message_list.append(Message(0,'sysop99','06/12/1991','GEN', 'Hayes Modem Firmware Needed', 'Need v3.1 firmware for 2400 baud, anyone have it?'))
master_message_list.append(Message(0,'circuit_fiend','06/05/1991','GEN', 'EPROM Failures', '8k Blank EPROMs fail checksum right out of the pack.'))
master_message_list.append(Message(0,'sysop99','06/12/1991','GEN', 'Hayes Modem Firmware Needed', 'Need v3.1 firmware for 2400 baud, anyone have it?'))
master_message_list.append(Message(0,'circuit_fiend','06/05/1991','GEN', 'EPROM Failures', '8k Blank EPROMs fail checksum right out of the pack.'))
master_message_list.append(Message(0,'sysop99','06/12/1991','GEN', 'Hayes Modem Firmware Needed', 'Need v3.1 firmware for 2400 baud, anyone have it?'))
master_message_list.append(Message(0,'circuit_fiend','06/05/1991','GEN', 'EPROM Failures', '8k Blank EPROMs fail checksum right out of the pack.'))
master_message_list.append(Message(0,'sysop99','06/12/1991','GEN', 'Hayes Modem Firmware Needed', 'Need v3.1 firmware for 2400 baud, anyone have it?'))
master_message_list.append(Message(0,'circuit_fiend','06/05/1991','GEN', 'EPROM Failures', '8k Blank EPROMs fail checksum right out of the pack.'))
master_message_list.append(Message(0,'sysop99','06/12/1991','GEN', 'Hayes Modem Firmware Needed', 'Need v3.1 firmware for 2400 baud, anyone have it?'))
master_message_list.append(Message(0,'circuit_fiend','06/05/1991','GEN', 'EPROM Failures', '8k Blank EPROMs fail checksum right out of the pack.'))
