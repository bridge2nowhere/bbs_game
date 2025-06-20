# Write your code here :-)
import bbs
import item

#state machine for the game
game_mode_list = ['dial_tone','bbs_menu','bbs_node']
game_mode = 'dial_tone'
phone_number = 0

#state machine for the menuing system
menu_mode_list = ['main','files','messages','ident']
menu_mode = 'main'



def handle_dialing():
    """this function handles the dialing of a bbs once connected it returns"""
    global game_mode
    global phone_number


    phone_number = input('Enter phone number to dial (352-2222 should be 3522222): ')
    try:
        phone_number = int(phone_number)
    except ValueError as ve:
        print('Not a valid number')
    while bbs.lookup(phone_number) == 'dial again':
        phone_number = input('Enter phone number to dial (352-2222 should be 3522222): ')
        try:
            phone_number = int(phone_number)
        except ValueError as ve:
            print('Not a valid number')
    print('Connected to ' + str(phone_number))
    print('\n\n')
    game_mode = 'bbs_menu'

def handle_menu():
    """this function handles the menu system for the BBS, returns to dialing or to node management"""
    global game_mode
    global menu_mode
    global phone_number

    if menu_mode == 'main':
        print('Welcome to ' + bbs.lookup(phone_number))
        print('[1] Messages')
        print('[2] Files')
        if bbs.bbs_list[bbs.bbs_connected].identify:
            print('[3] Identify Files')
        print('[4] Node Mangement')
        print('[5] Disconnect')
        choice = int(input(']>'))
        if choice == 1:
            menu_mode = 'messages'
        elif choice == 2:
            menu_mode = 'files'
        elif choice == 3 and bbs.bbs_list[bbs.bbs_connected].identify:
            menu_mode = 'ident'
        elif choice == 4:
            game_mode = 'bbs_node'
        elif choice == 5:
            print("\n\nDisconnected\n")
            game_mode = 'dial_tone'
            bbs.bbs_connected = None
            phone_number = None
        else:
            print('invalid selection')
    elif menu_mode == 'messages':
        pass
    elif menu_mode == 'files':
        print('[1] List Files')
        print('[2] Download Files')
        choice = int(input(']>'))
        if choice == 1:
            for index,file in enumerate(bbs.bbs_list[bbs.bbs_connected].file_list):
                fancy_size = ''
                if file.size < 1000:
                    fancy_size = str(file.size) + 'kb'
                else:
                    fancy_size = str(file.size/1000) + 'mb'
                print(format(index, '04X') + ' | ' + file.id + fancy_size.rjust(8,' ')  )
        else:
            print('invalid selection')



while True:

    if game_mode == 'dial_tone':
        #list of sites for testing purposes
        print('=========BBS List==========')
        print('Free File Farm     352-6544')
        print('Goose Roost        223-0412')
        print('The Crystal Palace 224-8216')
        print('TMagic Carpet      225-7446')
        handle_dialing()

    if game_mode == 'bbs_menu':
        handle_menu()

