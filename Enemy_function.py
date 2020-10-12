"""
    Author: Zeph Frear Hanson
    Date: 17-09-2020
    Title: Enemy Function
    Description: Where the battle function is stored
    Improvements(Use if altering the code): 
"""

#==-Libraries-==#
import random as rand
import time

#====-Functions-====#
def fire_gob():
    fg_hp = 60
    global player_hp
    print('''
        ╔════════════════════════════════════════╗
        ║ Fire Goblin: enter witty comment here. ║
        ╚════════════════════════════════════════╝
    ''')
    time.sleep(1)
    while(player_hp > 0 and fg_hp > 0):
        attack = input("""
        ┌───────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet │
        └───────────────────────────────────────────┘
        """)
        time.sleep(1)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(12,14)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            fg_hp -= damage
            fg_att = rand.randint(1,3)
            player_hp -= fg_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Fire Goblin hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(fg_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',fg_hp)
            time.sleep(1)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(14,15)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(1)
            fg_hp -= damage
            fg_att = rand.randint(1,3)
            player_hp -= fg_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Fire Goblin hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(fg_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',fg_hp)
            time.sleep(1)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(9,11)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(1)
            fg_hp -= damage
            fg_att = rand.randint(1,3)
            player_hp -= fg_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Fire Goblin hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(fg_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',fg_hp)
            time.sleep(1)
        if(fg_hp < 1):
            coin = rand.randint(14,17)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            time.sleep(1)
    

def earth_gob():
    eg_hp = 80
    global player_hp
    print('''
        ╔═════════════════════════════════════════╗
        ║ Earth Goblin: enter witty comment here. ║
        ╚═════════════════════════════════════════╝
    ''')
    time.sleep(1)
    while(player_hp > 0 and eg_hp > 0):
        attack = input("""
        ┌───────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet │
        └───────────────────────────────────────────┘
        """)
        time.sleep(1)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(13,16)
            print('''
        ╓──────────────────────────────────────────╖
        ║ you hit using your sword doing {} damage ║
        ╙──────────────────────────────────────────╜'''.format(damage))
            time.sleep(1)
            eg_hp -= damage
            eg_att = rand.randint(2,5)
            player_hp -= eg_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Earth Goblin hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(eg_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',eg_hp)
            time.sleep(1)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(11,14)
            print('''
        ╓────────────────────────────────────────╖
        ║ you hit using your bow doing {} damage ║
        ╙────────────────────────────────────────╜'''.format(damage))
            time.sleep(1)
            eg_hp -= damage
            eg_att = rand.randint(2,5)
            player_hp -= eg_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Earth Goblin hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(eg_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',eg_hp)
            time.sleep(1)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(9,12)
            print('''
        ╓───────────────────────────────────────────╖
        ║ you hit using your mallet doing {} damage ║
        ╙───────────────────────────────────────────╜'''.format(damage))
            time.sleep(1)
            eg_hp -= damage
            eg_att = rand.randint(2,5)
            player_hp -= eg_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Earth Goblin hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(eg_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',eg_hp)
            time.sleep(1)
        if(eg_hp < 1):
            coin = rand.randint(13,16)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            time.sleep(1)


def ice_gob():
    ig_hp = 60
    global player_hp
    print('''
        ╔═══════════════════════════════════════╗
        ║ Ice Goblin: enter witty comment here. ║
        ╚═══════════════════════════════════════╝
    ''')
    time.sleep(1)
    while(player_hp > 0 and ig_hp > 0):
        attack = input("""
        ┌───────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet │
        └───────────────────────────────────────────┘
        """)
        time.sleep(1)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(12,14)
            print('''
        ╓──────────────────────────────────────────╖
        ║ you hit using your sword doing {} damage ║
        ╙──────────────────────────────────────────╜'''.format(damage))
            time.sleep(1)
            ig_hp -= damage
            ig_att = rand.randint(4,7)
            player_hp -= ig_att
            print('''
        ╒═══════════════════════════════════════╕
        │ the Ice Goblin hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(ig_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',ig_hp)
            time.sleep(1)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(8,10)
            print('''
        ╓────────────────────────────────────────╖
        ║ you hit using your bow doing {} damage ║
        ╙────────────────────────────────────────╜'''.format(damage))
            time.sleep(1)
            ig_hp -= damage
            ig_att = rand.randint(4,7)
            player_hp -= ig_att
            print('''
        ╒═══════════════════════════════════════╕
        │ the Ice Goblin hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(ig_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',ig_hp)
            time.sleep(1)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(12,15)
            print('''
        ╓───────────────────────────────────────────╖
        ║ you hit using your mallet doing {} damage ║
        ╙───────────────────────────────────────────╜'''.format(damage))
            time.sleep(1)
            ig_hp -= damage
            ig_att = rand.randint(4,7)
            player_hp -= ig_att
            print('''
        ╒═══════════════════════════════════════╕
        │ the Ice Goblin hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(ig_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',ig_hp)
            time.sleep(1)
        if(ig_hp < 1):
            coin = rand.randint(12,16)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            time.sleep(1)

#====-Main Routine-====#
global player_hp
player_hp = 100
fg_hp = 60
ig_hp = 40
eg_hp = 80


#fire_gob()
#ice_gob()
#earth_gob()
