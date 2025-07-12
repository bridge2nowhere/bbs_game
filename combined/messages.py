import random
import csv
import config



def make_message_list() -> 'Message[]':
    """creates a list of messages"""
    msgs = []
    #handles adds 1-4 items into the list
    #qty = random.randint(0,4+1)
    for m in range(random.randint(0,4)+1):
        index = random.randint(0,len(master_message_list)-1)
        msg = master_message_list.pop(index)
        msgs.append(msg)
        #msgs.append(master_message_list.pop(index))
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

if config.file_import:
    print('file import turned on')
    message_file = input('Enter CSV File: ')
    with open(message_file, 'r') as csv_file:
        reader = csv.reader(csv_file)

        header = True
        for row in reader:

            if not header:
                #print(row)
                master_message_list.append(Message(row[0],row[1],row[2],row[3], row[4], row[5]))
            header = False

else:
    print('file import turned off')
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

print()
print()
print()
