"""
    Author: Zeph Frear Hanson
    Date: 24-09-2020
    Title: enemy function
    Description: function for battle
    Improvements(Use if altering the code): Healing included
    Notes: The Healing code needs to be added to all the other battle functions."""

#==-Libraries-==#
import random as rand
import time

#====-Functions-====#
def dummy():
    dum_hp = 60
    global player_hp
    print('''
        ╔══════════════════════════════════╗
        ║ Dummy: enter witty comment here. ║
        ╚══════════════════════════════════╝
    ''')
    time.sleep(1)
    while(player_hp > 0 and dum_hp > 0):
        attack = input("""
        ┌───────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet or {P}otion │
        └───────────────────────────────────────────────────────┘
        """)
        time.sleep(1)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(12,14)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            dum_hp -= damage
            dum_att = rand.randint(1,2)
            player_hp -= dum_att
            print('''
        ╒═══════════════════════════════════╕
        │ the Dummy hit you doing {} damage │
        ╘═══════════════════════════════════╛'''.format(dum_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',dum_hp)
            time.sleep(1)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(14,15)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(1)
            dum_hp -= damage
            dum_att = rand.randint(1,2)
            player_hp -= dum_att
            print('''
        ╒═══════════════════════════════════╕
        │ the Dummy hit you doing {} damage │
        ╘═══════════════════════════════════╛'''.format(dum_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',dum_hp)
            time.sleep(1)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(9,11)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(1)
            dum_hp -= damage
            dum_att = rand.randint(1,2)
            player_hp -= dum_att
            print('''
        ╒═══════════════════════════════════╕
        │ the Dummy hit you doing {} damage │
        ╘═══════════════════════════════════╛'''.format(dum_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',dum_hp)
            time.sleep(1)
        elif(attack == 'p' or attack == 'P'):
            heal = rand.randint(1,30)
            print('''
        ╓────────────────────╖
        ║ you heal {} damage ║
        ╙────────────────────╜'''.format(heal))
            time.sleep(1)
            player_hp += heal
            dum_att = rand.randint(1,2)
            player_hp -= dum_att
            print('''
        ╒═══════════════════════════════════╕
        │ the Dummy hit you doing {} damage │
        ╘═══════════════════════════════════╛'''.format(dum_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',dum_hp)
            time.sleep(1)
        if(dum_hp < 1):
            coin = rand.randint(14,17)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            time.sleep(1)


#====-Main Routine-====#
global player_hp
player_hp = 100

dummy()




            
