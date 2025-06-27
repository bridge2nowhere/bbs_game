import random
import time
from item import *

class Player:
    def __init__(self):
        self.heat = 10
        self.power = 4
        self.score = 0

class Enemy:
    def __init__(self,chap):
        self.enemy_index = random.randint(4096,65534)
        self.heat = chap * 3
        self.power = chap * 2


class Empty:
    def __init__(self):
        self.enemy_index = 0000

def node_initialize(bbs,p,chap):
    bbs.node_initalize(chap)

def node_frame(bbs,p):
    enemy_print_list = []
    all_dead = True
    for e in bbs.enemy_list:

        if e.enemy_index == 0000:
            enemy_print_list.append(' $$ ')
        else:
            enemy_print_list.append(format(e.enemy_index, '04X'))
            all_dead = False

    print(enemy_print_list[0] + ' ' +
        enemy_print_list[1] + ' ' +
        enemy_print_list[2] + ' ' +
        enemy_print_list[3] + ' ')
    print('╔═╧════╧════╧════╧╗')
    print('╚═╤════╤════╤════╤╝')
    print(enemy_print_list[4] + ' ' +
        enemy_print_list[5] + ' ' +
        enemy_print_list[6] + ' ' +
        enemy_print_list[7] + ' ')
    if all_dead:
        pause = input('All Nodes Cleared')
        return True
    else:
        print('Enter I for Inventory/L for Load')
        node = input('Choose node to attack: ').upper()
        if node == 'I':
            print('Heat = ' + str(p.heat) + ' Power = ' + str(p.power))
            print('---------------------------------------------')
            if download_list:
                for i in item.download_list:
                    print(format(i.itemIndex, '04X') + ' | ' + i.file_name + ' | ' + i.description)
        if node == 'L':
            item = int(input('Item Index: ',16))
            target = input('Target [P]layer or Enemy Index: ')
            if target == 'P':
                p.power += 1
            else:
                for i,e in enumerate(enemy_print_list):
                    if node == e:
                        bbs.enemy_list[i].power += 1
        else:
            for i,e in enumerate(enemy_print_list):
                if node == e:
                    bbs.enemy_list[i].heat -= p.heat
                    p.heat -= 3
        return False

def node_game_over(p):
    print('The water of Lake Ontario roils as Hastur emerges.')
    print('the power of his aura incinerates youinstantly;')
    print('your death is painless. Other are not so lucky\n')
    print(p.score)
