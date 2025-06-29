
import board
import key


print(']> ',end = '')
while True:
    if key.key_handler():
        if key.key_routing == 'GEN':
            print('\n' + str(key.key_input_int))
        elif key.key_routing == 'LOAD':
            print('\nLOAD: ' + str(key.key_input_int))
            key.key_routing = 'GEN'
        elif key.key_routing == 'STORE':
            print('\nSTORE: ' + str(key.key_input_int))
            key.key_routing = 'GEN'
        print(']> ',end = '')
    #time.sleep(100)
