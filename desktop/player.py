import random
import time

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

def node_initialize(bbs,p,chap):
    bbs.node_initalize(chap)

def draw_screen():



def node_frame(bbs,p):
    print('2345 4324 12F5 586C')
    print('--]----]----[----[-')
    print('--]----]----[----[-')
    print('2345 4324 12F5 586C')
    node = int(input('Choose node to attack'),16)


def node_game_over(p):
    print('The water of Lake Ontario roils as Hastur emerges.')
    print('the power of his aura incinerates youinstantly;')
    print('your death is painless. Other are not so lucky\n')
    print(p.score)


