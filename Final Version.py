"""
    Author: Zeph Frear Hanson
    Date: 29-10-2020
    Title: Full Components(Post Testing)
    Description: All the components before user testing and regular testing
    Improvements(Use if altering the code): Added all the advice from the
    user testing and added the database.
"""


#==-Libraries-==#
import time  
import random as rand
import sqlite3
from sqlite3 import Error

#====-Functions-====#

#==========-Introduction-==========#


def intro():
    global pid,name,coins
    print('''
        ╔══════════════════════════════════════════╗
        ║         Welcome to the Dunegeon!         ║
        ║                                          ║
        ║    In this, you will be entering three   ║
        ║      different dungeons and fighting     ║
        ║         a variety of enemies.            ║
        ║                                          ║
        ║     You start in a Tavern with a         ║
        ║  board full of three different dungeons  ║
        ║     with elemental enemies and LOOT!     ║
        ║                                          ║
        ║   Once you have completed the dungeons   ║
        ║    you will unload a FINAL DUNGEON!!!    ║
        ║   where you will fight the final boss.   ║
        ║                                          ║
        ║    When battling different enemies your  ║
        ║    weapons will do more or less damage   ║
        ║   depending on the enemy. So try it out  ║
        ║     and see which weapon does best!      ║
        ╚══════════════════════════════════════════╝
''')
    time.sleep(7)
    print('''
        Note: Goose noises are best experienced
        when spoken aloud.
''')
    name = input('Please enter your name: ')
    #========================================================
    conn = connect_db()  #connect to database function
    c = conn.cursor()
    c.execute( f"INSERT INTO players VALUES('{name}')" )
    conn.commit()
    c.execute(f"SELECT rowid FROM players WHERE username = '{name}'")
    conn.commit()
    result = c.fetchone()   #you can use fetchone/fetchall if you want just one result
    conn.commit()
    for i in result:    # this will get the current players id
        pid = int(i)
    coins = 0   #setting up the players starting coins 
    c.execute( f"INSERT INTO scores VALUES('{coins}','{pid}')")
    conn.commit()
    conn.close()
    player_info(name,pid)  #checking if its working.
    #========================================================
    tavern()


#==========-Tavern-==========#

    
def tavern():
    print('''
        ╔══════════════════════════════════════════════════╗
        ║       You enter The Thieving Goose Tavern. A     ║
        ║      mildly popular tavern located conveniently  ║
        ║      in the area of four dungeons filled with    ║
        ║                 danger and loot.                 ║
        ║                                                  ║
        ║   Inside the tavern, you see a mischievous band  ║
        ║   of treasure hunter and pirates. The perfect a  ║
        ║  place for you to be. Across from the entrance   ║
        ║  sits a board with places for treasure hunters   ║
        ║               like you to explore.               ║
        ╚══════════════════════════════════════════════════╝
''')
    time.sleep(6)
    while True:
        choice = input('''
        ┌────────────────────────────────────────────────────┐
        │ What would you like to do? Talk to the {B}artender,│
        │ Start a bar {F}ight, Look at the {Q}uest board,    │
        │             pet the tavern {G}oose.                │            
        └────────────────────────────────────────────────────┘
    ''')

        if(choice == 'B' or choice == 'b'):  #If players choice is b or B
            print('''
            You walk over to the bar, you see the bartender turn
            around to reveal that THE BARTENDER IS A GOOSE?!
            ''')
            time.sleep(3)
            print('''
            ╔══════════════════════════╗
            ║ BarTender Goose: hjörnk. ║
            ╚══════════════════════════╝
            ''')
            time.sleep(0.50)
            print('''
            The bartender's Swedish.
            ''')
            time.sleep(0.50)
            print('''
            ╔══════════════════════════════════╗
            ║ BarTender Goose: hjörnk angirly. ║
            ╚══════════════════════════════════╝
            ''')
            time.sleep(0.50)
            print('''
            It seems that the bartender is now angry
            ''')
            time.sleep(0.50)
            print('''
            ╔════════════════════════════════╗
            ║ BarTender Goose: hjörnk börnk. ║
            ╚════════════════════════════════╝
            ''')
            time.sleep(1)
            print('''
            The bartender bit you taking some coins.
            But they gave you a drink!
            ''')
        elif(choice == 'F' or choice == 'f'):  #If players choice is f or F
            print('''
            you approach a table filled with GEESE?!
            IN PIRATE COSTUMES?!
            ''')
            time.sleep(2)
            print('''
            ╔══════════════════════════════════════╗
            ║ The Pirate Geese Gang: haaaaarrggnk. ║
            ╚══════════════════════════════════════╝
            ''')
            time.sleep(0.50)
            print('''
            The all swarm you and bites you with
            their golden becks.
            ''')
        elif(choice == 'Q' or choice == 'q'):  #If players choice is q or Q
            quest()  #Runs the quest board function
        elif(choice == 'G' or choice == 'g'):  #If players choice is g or G
            print('''
            you walk over to the tavern's famous
            goose. you go to pat it but it quickly
            swivels and bites you.
    ''')


#==========-Quest-Board-==========#

            
def quest():
    global name, pid
    print('''
            You approach the quest board, you see three
            pieces of paper held to the board using throwing
            knives. 
            
''')
    time.sleep(1)
    qchoice = input('''
        ┌──────────────────────────────────────────────┐
        │   Which quest do you pick? {F}ire Dungeon,   │
        │      {I}ce Dungeon, {E}arth Dungeon          │
        └──────────────────────────────────────────────┘
    ''')
    if(qchoice == 'F' or qchoice == 'f'):  #If players choice is f or F it will run the fire dungeon
        print('Loading Dungeon....')
        time.sleep(9)
        fired()
    if(qchoice == 'I' or qchoice == 'i'):  #If players choice is i or I it will run the ice dungeon
        print('Loading Dungeon....')
        time.sleep(9)
        iced()
    if(qchoice == 'E' or qchoice == 'e'):  #If players choice is e or E it will run the earth dungeon
        print('Loading Dungeon....')
        time.sleep(9)
        rocked()
              

#==========-Fire-Dungeon-==========#

        
def fired():
    print('''
    Now entering the fire dungeon, hold onto your butt.
''')
    time.sleep(2)
    print('''
        As you walk into the dungeon the shear heat creeps
        up you whole body setting flames to leather gripping
        on your sword. You see that in the center of the
        room ther is a swarm of garden gnomes. You kick on over
        the ledge into the lava pools below. Doing this sets off
        something in the remaining gnomes, their eyes light up with
        a burning passion.
''')
    time.sleep(8)
    fire_gob()  
    fire_gob()
    fire_gob()
    print('''
        After smashing all the gnomes a pair of red firey eyes gleaming
        down on you. 
''')
    time.sleep(1)
    fire_drag()
    tavern()  #takes you back to the tavern function


#==========-Ice-Dungeon-==========#

    
def iced():
    print('''
    Now entering the ice dungeon, hold onto your butt.
''')
    time.sleep(2)
    print('''
        As you walk into the dungeon and immediately freeze up. Not that
        anything is scary in front of you, it's just really cold. You see
        surronding you that there are small ice pillars with garden gnomes
        wedged in them. You think nothing of it and continue towards the
        cave across the other side of the room. But then the ice pillars
        begin to shake and shatter revealing that the gnomes are infact
        sentient and ready to fight.
''')
    time.sleep(8)
    ice_gob()
    ice_gob()
    ice_gob()
    print('''
        After defeating all the gnomes you continue back towards the cave
        but now there seems to be more mist coming from out of the cave
        than before. Upon touching the mist your legs begin to freeze up.
        Again not because your scared, just the mist is really cold. A
        menacing reveals itself as being causing the mist.
''')
    time.sleep(1)
    ice_drag()
    tavern()  #takes you back to the tavern function


#==========-Earth-Dungeon-==========#

    
def rocked():
    print('''
    Now entering the earth dungeon, hold onto your butt.
''')
    time.sleep(2)
    print('''
        As you walk into the dungeon and see garden gnomes stuck in vines.
        you grab one but it seems to like its vine so it screams alerting
        the other gnomes in the area.
''')
    time.sleep(8)
    earth_gob()
    earth_gob()
    earth_gob()
    print('''
        After defeating the gnomes an older looking dragon walks in, catching
        you standing over the remains of his precious gnome collection.
''')
    time.sleep(1)
    ear_drag()
    tavern()  #takes you back to the tavern function


#==========-Fire-Gnome-==========#

    
def fire_gob(): #Battle system for the fire gnome
    fg_hp = 60
    global player_hp, db_coins,name,pid, coins
    print('''
        ╔═══════════════════════════════════════╗
        ║ Fire Gnome: enter witty comment here. ║
        ╚═══════════════════════════════════════╝
    ''')
    time.sleep(0.25)
    while(player_hp > 0 and fg_hp > 0):
        attack = input("""
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
        """)
        time.sleep(0.25)
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
        ╒═══════════════════════════════════════╕
        │ the Fire Gnome hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(fg_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',fg_hp)
            time.sleep(0.25)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(14,15)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            fg_hp -= damage
            fg_att = rand.randint(1,3)
            player_hp -= fg_att
            print('''
        ╒═══════════════════════════════════════╕
        │ the Fire Gnome hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(fg_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',fg_hp)
            time.sleep(0.25)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(9,11)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            fg_hp -= damage
            fg_att = rand.randint(1,3)
            player_hp -= fg_att
            print('''
        ╒═══════════════════════════════════════╕
        │ the Fire Gnome hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(fg_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',fg_hp)
            time.sleep(0.25)
        elif(attack == 'p' or attack == 'P'):
            heal = rand.randint(1,30)
            print('''
        ╓────────────────────╖
        ║ you heal {} damage ║
        ╙────────────────────╜'''.format(heal))
            time.sleep(0.25)
            player_hp += heal
            dum_att = rand.randint(1,2)
            player_hp -= dum_att
            print('''
        ╒═══════════════════════════════════════╕
        │ the Fire Gnome hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(dum_att))
        if(fg_hp < 1):
            coin = rand.randint(14,17)
            
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            #users[0] = int(users[0]) + coin #adds coins to the users coin list
            time.sleep(0.25)
            #----updating the coins amount in the database----
            #coins += int(users[0])
            adding_coins(pid,coin)
            
            

            
            

    

#==========-Earth-Gnome-==========#

            
def earth_gob():  #Battle system for the earth gnome
    eg_hp = 80
    global player_hp, pid, coins
    print('''
        ╔════════════════════════════════════════╗
        ║ Earth Gnome: enter witty comment here. ║
        ╚════════════════════════════════════════╝
    ''')
    time.sleep(0.25)
    while(player_hp > 0 and eg_hp > 0):
        attack = input("""
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
        """)
        time.sleep(0.25)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(13,16)
            print('''
        ╓──────────────────────────────────────────╖
        ║ you hit using your sword doing {} damage ║
        ╙──────────────────────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            eg_hp -= damage
            eg_att = rand.randint(2,4)
            player_hp -= eg_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Earth Gnome hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(eg_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',eg_hp)
            time.sleep(0.25)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(11,14)
            print('''
        ╓────────────────────────────────────────╖
        ║ you hit using your bow doing {} damage ║
        ╙────────────────────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            eg_hp -= damage
            eg_att = rand.randint(2,4)
            player_hp -= eg_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Earth Gnome hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(eg_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',eg_hp)
            time.sleep(0.25)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(9,12)
            print('''
        ╓───────────────────────────────────────────╖
        ║ you hit using your mallet doing {} damage ║
        ╙───────────────────────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            eg_hp -= damage
            eg_att = rand.randint(2,4)
            player_hp -= eg_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Earth Gnome hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(eg_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',eg_hp)
            time.sleep(0.25)
        elif(attack == 'p' or attack == 'P'):
            heal = rand.randint(1,30)
            print('''
        ╓────────────────────╖
        ║ you heal {} damage ║
        ╙────────────────────╜'''.format(heal))
            time.sleep(0.25)
            player_hp += heal
            dum_att = rand.randint(1,2)
            player_hp -= dum_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Earth Gnome hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(dum_att))
        if(eg_hp < 1):
            coin = rand.randint(13,16)
            
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            #users[0] = int(users[0]) + coin  #adds coins to the users coin list
            #----updating the coins amount in the database----
            #coins += int(users[0])
            adding_coins(pid,coin)
            time.sleep(0.25) 


#==========-Ice-Gnome-==========#

            
def ice_gob():  #Battle system for the ice gnome
    ig_hp = 60
    global player_hp, pid, coins
    print('''
        ╔══════════════════════════════════════╗
        ║ Ice Gnome: enter witty comment here. ║
        ╚══════════════════════════════════════╝
    ''')
    time.sleep(0.25)
    while(player_hp > 0 and ig_hp > 0):
        attack = input("""
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
        """)
        time.sleep(0.25)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(12,14)
            print('''
        ╓──────────────────────────────────────────╖
        ║ you hit using your sword doing {} damage ║
        ╙──────────────────────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            ig_hp -= damage
            ig_att = rand.randint(2,4)
            player_hp -= ig_att
            print('''
        ╒══════════════════════════════════════╕
        │ the Ice Gnome hit you doing {} damage │
        ╘══════════════════════════════════════╛'''.format(ig_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',ig_hp)
            time.sleep(0.25)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(8,10)
            print('''
        ╓────────────────────────────────────────╖
        ║ you hit using your bow doing {} damage ║
        ╙────────────────────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            ig_hp -= damage
            ig_att = rand.randint(2,4)
            player_hp -= ig_att
            print('''
        ╒══════════════════════════════════════╕
        │ the Ice Gnome hit you doing {} damage │
        ╘══════════════════════════════════════╛'''.format(ig_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',ig_hp)
            time.sleep(0.25)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(12,15)
            print('''
        ╓───────────────────────────────────────────╖
        ║ you hit using your mallet doing {} damage ║
        ╙───────────────────────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            ig_hp -= damage
            ig_att = rand.randint(2,4)
            player_hp -= ig_att
            print('''
        ╒══════════════════════════════════════╕
        │ the Ice Gnome hit you doing {} damage │
        ╘══════════════════════════════════════╛'''.format(ig_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',ig_hp)
            time.sleep(0.25)
        elif(attack == 'p' or attack == 'P'):
            heal = rand.randint(1,30)
            print('''
        ╓────────────────────╖
        ║ you heal {} damage ║
        ╙────────────────────╜'''.format(heal))
            time.sleep(0.25)
            player_hp += heal
            dum_att = rand.randint(1,2)
            player_hp -= dum_att
            print('''
        ╒══════════════════════════════════════╕
        │ the Ice Gnome hit you doing {} damage │
        ╘══════════════════════════════════════╛'''.format(dum_att))
        if(ig_hp < 1):
            coin = rand.randint(12,16)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            #users[0] = int(users[0]) + coin  #adds coins to the users coin list
            #----updating the coins amount in the database----
            #coins += int(users[0])
            adding_coins(pid,coin)
            time.sleep(0.25)


#==========-Fire-Dragon-==========#

            
def fire_drag():  #Battle system for the fire dragon
    fd_hp = 120
    global player_hp, pid, coins
    global dungeonkey
    print('''
        ╔════════════════════════════════════════╗
        ║ Fire Dragon: enter witty comment here. ║
        ╚════════════════════════════════════════╝
    ''')
    time.sleep(0.25)
    while(player_hp > 0 and fd_hp > 0):
        attack = input("""
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
        """)
        time.sleep(0.25)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(12,14)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            fd_hp -= damage
            fd_att = rand.randint(8,10)
            player_hp -= fd_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Fire Dragon hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(fd_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',fd_hp)
            time.sleep(0.25)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(14,15)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            fd_hp -= damage
            fd_att = rand.randint(8,10)
            player_hp -= fd_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Fire Dragon hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(fd_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',fd_hp)
            time.sleep(0.25)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(9,11)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            fd_hp -= damage
            fd_att = rand.randint(8,10)
            player_hp -= fd_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Fire Dragon hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(fd_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',fd_hp)
            time.sleep(0.25)
        elif(attack == 'p' or attack == 'P'):
            heal = rand.randint(1,30)
            print('''
        ╓────────────────────╖
        ║ you heal {} damage ║
        ╙────────────────────╜'''.format(heal))
            time.sleep(0.25)
            player_hp += heal
            dum_att = rand.randint(8,10)
            player_hp -= dum_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Fire Dragon hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(dum_att))
        if(fd_hp < 1):
            coin = rand.randint(23,41)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            #users[0] = int(users[0]) + coin  #adds coins to the users coin list
            #----updating the coins amount in the database----
            #coins += int(users[0])
            adding_coins(pid,coin)
            
            dungeonkey = dungeonkey -1
            time.sleep(0.25)
        if(dungeonkey == 0):  #way of triggering the hydra goose story text
            final_b()


#==========-Ice-Dragon-==========#

            
def ice_drag():  #Battle system for the ice dragon
    id_hp = 130
    global player_hp, pid, coins
    global dungeonkey
    print('''
        ╔═══════════════════════════════════════╗
        ║ Ice Dragon: enter witty comment here. ║
        ╚═══════════════════════════════════════╝
    ''')
    time.sleep(0.25)
    while(player_hp > 0 and id_hp > 0):
        attack = input("""
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
        """)
        time.sleep(0.25)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(12,14)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            id_hp -= damage
            id_att = rand.randint(9,12)
            player_hp -= id_att
            print('''
        ╒═══════════════════════════════════════╕
        │ the Ice Dragon hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(id_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',id_hp)
            time.sleep(0.25)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(14,15)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            id_hp -= damage
            id_att = rand.randint(9,12)
            player_hp -= id_att
            print('''
        ╒═══════════════════════════════════════╕
        │ the Ice Dragon hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(id_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',id_hp)
            time.sleep(0.25)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(9,11)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            id_hp -= damage
            id_att = rand.randint(9,12)
            player_hp -= id_att
            print('''
        ╒═══════════════════════════════════════╕
        │ the Ice Dragon hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(id_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',id_hp)
            time.sleep(0.25)
        elif(attack == 'p' or attack == 'P'):
            heal = rand.randint(1,30)
            print('''
        ╓────────────────────╖
        ║ you heal {} damage ║
        ╙────────────────────╜'''.format(heal))
            time.sleep(0.25)
            player_hp += heal
            dum_att = rand.randint(9,12)
            player_hp -= dum_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Ice Dragon hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(dum_att))
        if(id_hp < 1):
            coin = rand.randint(21,39)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            #users[0] = int(users[0]) + coin  #adds coins to the users coin list
            #----updating the coins amount in the database----
            #coins += int(users[0])
            adding_coins(pid,coin)
            
            dungeonkey = dungeonkey -1
            time.sleep(0.25)
        if(dungeonkey == 0):  #way of triggering the hydra goose story text
            final_b()


#==========-Earth-Dungeon-==========#

            
def ear_drag():  #Battle system for the earth dragon
    ed_hp = 170
    global player_hp, coins
    global dungeonkey
    print('''
        ╔═════════════════════════════════════════╗
        ║ Earth Dragon: enter witty comment here. ║
        ╚═════════════════════════════════════════╝
    ''')
    time.sleep(0.25)
    while(player_hp > 0 and ed_hp > 0):
        attack = input("""
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
        """)
        time.sleep(0.25)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(11,14)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            ed_hp -= damage
            ed_att = rand.randint(10,12)
            player_hp -= ed_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Earth Dragon hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(ed_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',ed_hp)
            time.sleep(0.25)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(14,15)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            ed_hp -= damage
            ed_att = rand.randint(10,12)
            player_hp -= ed_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Earth Dragon hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(ed_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',ed_hp)
            time.sleep(0.25)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(9,11)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            ed_hp -= damage
            ed_att = rand.randint(10,12)
            player_hp -= ed_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Earth Dragon hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(ed_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',ed_hp)
            time.sleep(0.25)
        elif(attack == 'p' or attack == 'P'):
            heal = rand.randint(1,30)
            print('''
        ╓────────────────────╖
        ║ you heal {} damage ║
        ╙────────────────────╜'''.format(heal))
            time.sleep(0.25)
            player_hp += heal
            dum_att = rand.randint(10,12)
            player_hp -= dum_att
            print('''
        ╒══════════════════════════════════════════╕
        │ the Earth Dragon hit you doing {} damage │
        ╘══════════════════════════════════════════╛'''.format(dum_att))
        if(ed_hp < 1):
            coin = rand.randint(22,40)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            #users[0] = int(users[0]) + coin  #adds coins to the users coin list
            #----updating the coins amount in the database----
            #coins += coin
            adding_coins(pid,coin)
            dungeonkey = dungeonkey -1
            time.sleep(0.25)
        if(dungeonkey == 0):  #way of triggering the hydra goose story text
            final_b()
            

#==========-Hydra-Goose-==========#


def final_b():  #Story text for the hyrda goose
    print('''
        You return back to the Tavern but something seems off.
        You peek at a table and see a glass full of "juice"
        shaking slightly. SUDDENLY! the door swings open
        revealing the source of the shaking! Its a goose.

        ╔══════════════╗
        ║ Goose: Quack ║
        ╚══════════════╝

        Confused by this herasy you cut the gooses head off.
        Suddenly a second head sprouts from the goose's head stump
''')
    hydra_goose()


#==========-Hydra-Goose-==========#

            
def hydra_goose():  #Battle system for the hydra goose
    hydg_hp = 160
    head = 2
    global player_hp, pid,coins
    print('''
        ╔═══════════════════╗
        ║ Hydra Goose: Honk ║
        ╚═══════════════════╝
    ''')
    time.sleep(0.25)
    while(player_hp > 0 and hydg_hp > 0):
        attack = input("""
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
        """)
        time.sleep(0.25)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(12,14)
            print('''
        ╓──────────────────────────────────────────╖
        ║ you hit using your sword doing {} damage ║
        ╙──────────────────────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            hydg_att = rand.randint(2,4)
            if(rand.randint(1,2) == 2):
                head = head + 1
                hydg_att = hydg_att * head
                print('''
        You split its head now it does more damage
''')
            hydg_hp -= damage
            player_hp -= hydg_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Hydra Goose hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(hydg_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',hydg_hp)
            time.sleep(0.25)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(8,10)
            print('''
        ╓────────────────────────────────────────╖
        ║ you hit using your bow doing {} damage ║
        ╙────────────────────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            hydg_att = rand.randint(2,4)
            if(rand.randint(1,2) == 2):
                head = head + 1
                hydg_att = hydg_att * head
                print('''
        You split its head now it does more damage
''')
            hydg_hp -= damage
            player_hp -= hydg_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Hydra Goose hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(hydg_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',hydg_hp)
            time.sleep(0.25)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(12,15)
            print('''
        ╓───────────────────────────────────────────╖
        ║ you hit using your mallet doing {} damage ║
        ╙───────────────────────────────────────────╜'''.format(damage))
            time.sleep(0.25)
            hydg_att = rand.randint(2,4)
            if(rand.randint(1,2) == 2):
                head = head + 1
                hydg_att = hydg_att * head
                print('''
        You split its head now it does more damage
''')
            hydg_hp -= damage
            player_hp -= hydg_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Hydra Goose hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(hydg_att))
            time.sleep(0.25)
            print('''
        Your health:''',player_hp)
            time.sleep(0.25)
            print('''
        Enemies health:''',hydg_hp)
            time.sleep(0.25)
        elif(attack == 'p' or attack == 'P'):
            heal = rand.randint(1,30)
            print('''
        ╓────────────────────╖
        ║ you heal {} damage ║
        ╙────────────────────╜'''.format(heal))
            time.sleep(0.25)
            player_hp += heal
            dum_att = rand.randint(1,2)
            player_hp -= dum_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Hydra Goose hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(dum_att))
        if(hydg_hp < 1):
            coin = rand.randint(45,120)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            #users[0] = int(users[0]) + coin  #adds coins to the users coin list
            #coins += coin
            adding_coins(pid,coin)
            time.sleep(0.25)
            end()



#====-End-====#
def end():
    print('''
        ╔════════════════════════════════════════╗
        ║         Congratulations you win!       ║
        ║                                        ║
        ║         Thank you for playing!         ║
        ╚════════════════════════════════════════╝
''')
#end of game stats  --- giving player options for and running different queries
    data = input("Do you want to see your results or everyones, [y]ours, [e]veryones")
    if(data == 'y'):
        player_info(name,pid)
    else:
        display()


#====-Database functions====#

def connect_db():
    '''This connects to the database and returns a connection'''
    conn = None
    db_file = "dunegeon.db" #creates database if not exists already

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_tables():
    '''creates the tables in the database'''
    conn = connect_db() #connects to the database
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS players(
        username DATATYPE text
        )"""
    )

    c.execute("""CREATE TABLE IF NOT EXISTS scores(
        coins DATATYPE integer,
        player_id DATATYPE integer
        )"""
    )

def adding_coins(pid,coins):
    '''adding coins to the database'''
    conn = connect_db()  #connects to the database
    c = conn.cursor()
    c.execute(f"SELECT coins FROM scores WHERE player_id = '{pid}' ")
    result = c.fetchone()
    conn.commit()

    #adding coins to database
    new_coins = result[0] + coins
    c.execute(f"""UPDATE scores SET coins = '{new_coins}'
            WHERE rowid = '{pid}' """)
    conn.commit()

    
#====-Display data-====#
def player_info(name,pid):
    '''Displaying just the players information and coins'''
    #global name, pid  #not sure if needed?
    conn = connect_db()  #connects to the database
    c = conn.cursor()
    c.execute(f"""
    SELECT players.rowid,players.username,scores.coins,scores.player_id
    FROM players INNER JOIN scores
    ON players.rowid = scores.player_id
    WHERE players.username = '{name}' and scores.player_id = '{pid}'
    """)  #showing row id and other fields
    results = c.fetchall()   #you can use fetchone if you want just one result
    conn.commit()
    print("player info")
    for i in results:    # this will display the tuples in the list
         print(f"""
    player id: {i[0]}
     username: {i[1]}
        coins: {i[2]}
     score id: {i[3]}
""")

def display():
    '''For displaying the queries from the database'''
    conn = connect_db()  #connects to the database
    c = conn.cursor()

    #displaying all player data
    #c.execute("SELECT rowid,* FROM players ORDER BY usernames ASC")  #showing row id and other fields
    results = c.fetchall()   #you can use fetchone if you want just one result
    conn.commit()
    print("All player information")
    for i in results:    # print(i[0], i[1]) will display the results with no brackets
        print("""
        id: {}
  username: {}
        """.format(i[0],i[1]))
    
    #displaying all score data
    c.execute("SELECT rowid,* FROM scores")
    results = c.fetchall()   #you can use fetchone if you want just one result
    conn.commit()
    print("All score information")
    for i in results:    # print(i[0], i[1], i[2]) will display the results with no brackets
        print("""
        id: {}
     coins: {}
 player id: {}
        """.format(i[0],i[1],i[2]))       


#====-Main Routine-====#

create_tables() #This creates the tables
pid = None  # Current player
db_coins = 0
global player_hp
global dungeonkey

player_hp = 100
dungeonkey = 3
name = ''
coins = 0 
users = [0]
fg_hp = 60
ig_hp = 40
eg_hp = 80
hydg_hp = 160

#fire_gob()

#display()  #checking database information displays
intro()




            
