# Write your code here :-)
import bbs
import item
import config
from player import *


#state machine for the game
game_mode_list = ['dial_tone','bbs_menu','bbs_node']
game_mode = 'dial_tone'
phone_number = 0

#state machine for the menuing system
menu_mode_list = ['main','files','messages','ident']
menu_mode = 'main'

#game management
player = Player()
chapter = 1



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
    if not bbs.bbs_list[bbs.bbs_connected].visited:
       bbs.bbs_list[bbs.bbs_connected].first_visit()
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
        try:
            choice = int(input(']>'))
        except ValueError as ve:
            print('Not a valid number')
            choice = 0

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
        print('[1] List Messages')
        print('[2] Read Messages')
        print('[3] Return to Main Menu')
        choice = int(input(']>'),16)
        if choice == 1:
            print('INDEX| BRD |  USER        | SUBJECT')
            print('-----+-----+--------------+---------')
            for index,msg in enumerate(bbs.bbs_list[bbs.bbs_connected].message_list):
                print(format(index, '04X') + ' | ' + msg.board + ' | ' + msg.user + ' | '+ msg.subject )
            print('\n')
        elif choice == 2:
                #ask the user for the index, loop if the number is invalid or it's not an item
                msg_index = int(input('Message Index: '),16)
                while msg_index >= len(bbs.bbs_list[bbs.bbs_connected].message_list):
                    print('invalid index')
                    msg_index = int(input('Message Index: '),16)
                print(bbs.bbs_list[bbs.bbs_connected].message_list[msg_index].subject)
                print(bbs.bbs_list[bbs.bbs_connected].message_list[msg_index].date + '     ' + bbs.bbs_list[bbs.bbs_connected].message_list[msg_index].user )
                print('\n' + bbs.bbs_list[bbs.bbs_connected].message_list[msg_index].post + '\n\n')
        elif choice == 3:
            #return to the main meu
            menu_mode = 'main'
        else:
            print('invalid selection')
    elif menu_mode == 'files':
        print('[1] List Files')
        print('[2] Download Files')
        print('[3] Return to Main Menu')
        choice = int(input(']>'),16)
        if choice == 1:
            print('INDEX| NAME         | SIZE     | DESCRIPTION')
            print('-----+--------------+----------+-----------------')
            for index,file in enumerate(bbs.bbs_list[bbs.bbs_connected].file_list):
                fancy_size = ''
                if file.size < 1000:
                    fancy_size = str(file.size) + 'kb'
                else:
                    fancy_size = str(file.size/1000) + 'mb'
                print(format(index, '04X') + ' | ' + file.file_name + ' | ' + fancy_size.rjust(8,' ') + ' | '+ file.description )
        elif choice == 2:
                #ask the user for the index, loop if the number is invalid or it's not an item
                try:
                    download_index = int(input('File Index: '),16)
                except ValueError as ve:
                    pass
                else:
                    while download_index >= len(bbs.bbs_list[bbs.bbs_connected].file_list) or type(bbs.bbs_list[bbs.bbs_connected].file_list[download_index]) == item.File:
                        print('invalid file index')
                        download_index = int(input('File Index: '),16)
                    #download the file
                    bbs.bbs_list[bbs.bbs_connected].file_list[download_index].download()
        elif choice == 3:
            #return to the main meu
            menu_mode = 'main'
        else:
            print('invalid selection')
    elif menu_mode == 'ident':
        print('[1] List Local File Inventory')
        print('[2] Identify File')
        print('[3] Return to Main Menu')
        choice = int(input(']>'),16)
        if choice == 1:
            for i in item.download_list:
                print(format(i.itemIndex, '04X') + ' | ' + i.file_name + ' | ' + i.description)
            print('\n\n')
        elif choice == 2:
            for i in item.download_list:
                if not i.identified:
                    i.identify()
            print('operation complete')
        elif choice == 3:
            #return to the main meu
            menu_mode = 'main'
        else:
            print('invalid selection')



while True:

    if game_mode == 'dial_tone':
        #list of sites for testing purposes
        print('=========BBS List==================')
        print('Free File Farm     352-6544   IDENT')
        print('Goose Roost        223-0412')
        print('The Crystal Palace 224-8216')
        print('TMagic Carpet      225-7446')
        handle_dialing()

    if game_mode == 'bbs_menu':
        handle_menu()

    if game_mode == 'bbs_node':
        if not bbs.bbs_list[bbs.bbs_connected].node_initialized:
            node_initialize(bbs.bbs_list[bbs.bbs_connected],player,chapter)
            bbs.bbs_list[bbs.bbs_connected].node_initialized = True
        elif player.heat <= 0:
            node_game_over(player)
            break
        else:
            bbs.bbs_list[bbs.bbs_connected].update_enemies()
            if node_frame(bbs.bbs_list[bbs.bbs_connected],player):
                game_mode = 'bbs_menu'
                menu_mode = 'main'
                player.score += 1
