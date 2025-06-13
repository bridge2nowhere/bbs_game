# Write your code here :-)
import bbs
import item

game_mode_list = ['dial_tone','bbs_menu','bbs_node']
game_mode = 'dial_tone'
phone_number = 0

menu_mode_list = ['main','files','messages','ident']
menu_mode = 'main'


def handle_dialing():
    global game_mode
    global phone_number

    phone_number = int(input('Enter phone number to dial (352-2222 should be 3522222): '))
    while bbs.lookup(phone_number) == 'dial again':
        phone_number = int(input('Enter phone number to dial (352-2222 should be 3522222): '))
    print('Connected to ' + str(phone_number))
    print('\n\n')
    if bbs.bbs_list[bbs.bbs_connected].file_list == []:
        bbs.bbs_list[bbs.bbs_connected].first_connect()
    game_mode = 'bbs_menu'

def handle_menu():
    global game_mode
    global menu_mode
    global phone_number

    if menu_mode == 'main':
        print('Welcome to ' + bbs.lookup(phone_number))
        print('[1] Messages')
        print('[2] Download Files')
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
    elif menu_mode == 'files':
        for index,file in enumerate(bbs.bbs_list[bbs.bbs_connected].file_list):
            print(format(index, '04X') + ' | ' + file.id)
        user_input = input('Choose file to download: ')
        if user_input == '':
            menu_mode = 'main'
        else:
            download = int(user_input, 16)
            print(bbs.bbs_list[bbs.bbs_connected].file_list[download].id)
            input()


while True:

    if game_mode == 'dial_tone':
        print('=========BBS List==========')
        print('Free File Farm     352-6544')
        print('Goose Roost        223-0412')
        print('The Crystal Palace 224-8216')
        print('TMagic Carpet      225-7446')
        handle_dialing()

    if game_mode == 'bbs_menu':
        handle_menu()

