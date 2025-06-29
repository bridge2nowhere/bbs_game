import keypad
import board

KEY_NAMES = (
    'C','D','E','F','STORE',
    '8','9','A','B','LOAD',
    '4','5','6','7','CLEAR',
    '0','1','2','3','ENTER'
)


km = keypad.KeyMatrix(
    row_pins=(board.D5, board.D6, board.D9, board.D10),
    column_pins=(board.D11, board.D12, board.D13, board.D25, board.D24),
    columns_to_anodes = True,
)

key_input_int = None    #this holds the integeter value entered
key_string = ''         #this collects key presses until they are ready to process
key_routing = 'GEN'

def key_handler()-> bool:
    """handles keypad input, returns True when key_input_int is ready to be processed"""
    global key_input_int
    global key_string
    global key_routing
    event = km.events.get()

    if event and not event.pressed:
        key_input_ready = False
        if KEY_NAMES[event.key_number] == 'CLEAR':
            key_string = ''
            print('\n')
            key_routing = 'GEN'
        elif KEY_NAMES[event.key_number] == 'ENTER':
            if key_string != '':
                key_input_int = int(key_string,16)
                key_input_ready = True
                key_string = ''
                return True
        elif KEY_NAMES[event.key_number] == 'STORE':
            key_routing = 'STORE'
            key_string = ''
            print('\nSTORE: ', end ='')
        elif KEY_NAMES[event.key_number] == 'LOAD':
            key_routing = 'LOAD'
            key_string = ''
            print('\nLOAD: ', end ='')
        else:
            key_string += KEY_NAMES[event.key_number]
            print(KEY_NAMES[event.key_number], end='')
        return False


