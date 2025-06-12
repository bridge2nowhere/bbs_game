# Write your code here :-)
import bbs
import item

game_mode_list = ['dial_tone','bbs_menu','bbs_node']
game_mode = 'dial_tone'
phone_number = 0

menu_mode_list = ['main','files','messages','ident']
menu_mode = 'main'


def handle_dialing():
        phone_number = int(input('Enter phone number to dial (352-2222 should be 3522222): '))
        while bbs.lookup(phone_number) == 'dial again':
            phone_number = int(input('Enter phone number to dial (352-2222 should be 3522222): '))
        print('Connected to' + str(phone_number))
        print('\n\n')
        game_mode = 'bbs_menu'

def handle_menu():
    if menu_mode == 'main':
            print('Welcome to ' + bbs.lookup(phone_number))
            print('[1] Messages')
            print('[2] Download Files')
            if bbs.bbs_list[bbs.bbs_connected].identify:
                print('[3] Identify Files')
            print('[4] Node Mangement')
            print('[5] Disconnect')
            choice = int(input('>>>'))
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

while True:
    test_list = item.make_file_list(20)
    for i in test_list:
        print(i.id + ' ' + str(i.size) +' ' + i.description)
    if game_mode == 'dial_tone':
        handle_dialing()

    if game_mode == 'bbs_menu':
        handle_menu()

