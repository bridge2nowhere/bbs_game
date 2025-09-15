import random
import time
import item

class Person:
    """Superclass for all characters"""
    def __init__(self):
        self.heat = None
        self.power = None
        self.shield = 0

        self.critical = 20
        self.stunned = 0

        self.weapon_power = 0
        self.weapon_crit = 0


    def update_stun(self):
        """count down for stun effects (missed turns)"""
        self.stunned -= 1
        if self.stunned < 0:
            self.stunned = 0

    def attack(self) -> int:
        """creates attack damage"""
        crit = 1
        if random.randint(0,self.critical) == 1:
            crit = 2
        max_power = self.power + self.weapon_power
        low_power = max_power // 2
        damage_amnt = random.randint(low_power,(max_power+1) * crit)
        #print(f"max_power={max_power}, low_power={low_power}, damage={damage_amnt}")
        return damage_amnt

    def take_hit(self,damage_amnt):
        """removes damage from attack"""
        self.heat -= damage_amnt - self.shield

    def use_item(self,item):
        """updates all Person variables based on item effects"""
        self.power += item.power
        self.heat += item.heat
        self.shield += item.shield
        self.stunned += item.stun


        self.weapon_power = item.weapon_power
        self.weapon_crit  = item.weapon_crit

        if item.delete:
            self.heat = 0

class Player(Person):
    """class for player character"""
    def __init__(self):
        super().__init__()
        self.score = 0

        self.heat = 10
        self.power = 4

        self.weapon_power = 0
        self.weapon_crit = 0





class Enemy(Person):
    """Class for enemy characters"""
    def __init__(self,chap):
        super().__init__()
        self.enemy_index = random.randint(4096,65534)
        self.heat = chap * 3
        self.power = chap * 2


class Empty:
    """subsitute class for missing enemy nodes"""
    def __init__(self):
        self.enemy_index = 0000



def node_initialize(bbs,p,chap):
    """creates the node enemies on first arrival"""
    bbs.node_initalize(chap)

def node_frame(bbs,p)-> bool:
    """handles one node action"""
    #create list of active enemies
    enemy_print_list = []
    all_dead = True
    for e in bbs.enemy_list:

        if e.enemy_index == 0000:
            enemy_print_list.append(' $$ ')
        else:
            enemy_print_list.append(format(e.enemy_index, '04X'))
            all_dead = False
    #draw node screen
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
    #if there are no enemies left, exit with true
    if all_dead:
        pause = input('All Nodes Cleared')
        return True
    #get player's move and implement attacks
    else:
        print('Enter I for Inventory/L for Load')
        node = input('Choose node to attack: ').upper()
        if node == 'I':
            print('\n\n\n┌ Player Stats ───────────────')
            print('│ Heat = ' + str(p.heat) + ' Power = ' + str(p.power))
            print('└────────────────────────────')

            if item.download_list:
                for i in item.download_list:
                    print(format(i.itemIndex, '04X') + ' | ' + i.file_name + ' | ' + i.description)
            print('\n\n')
        elif node == 'L':
            i_index = int(input('Item Index: '),16)
            for array_index, itm in enumerate(item.download_list):
                if itm.itemIndex == i_index:
                    #use item
                    if itm.type == 'msmr':
                        target = input('target=')
                        for e in bbs.enemy_list:
                            if target == e.enemy_index:
                                e.use_item(itm)
                    else:
                        p.use_item(itm)
                    #remove item
                    download_list.pop(array_index)
        else:
            for i,e in enumerate(enemy_print_list):
                if node == e:
                    if p.stunned == 0:
                        bbs.enemy_list[i].take_hit(p.attack())
                    else:
                        p.update_stun()

                    if bbs.enemy_list[i].stunned == 0:
                        p.take_hit(bbs.enemy_list[i].attack())
                    else:
                        e.update_stun()
        return False

def node_game_over(p):
    print('The water of Lake Ontario roils as Hastur emerges.')
    print('the power of his aura incinerates youinstantly;')
    print('your death is painless. Other are not so lucky\n')
    print(p.score)
