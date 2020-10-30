"""
    Author: Zeph Frear Hanson
    Date: 29-10-2020
    Title: FUll Components(Pre Testing)
    Description: All the components before user testing and regular testing
    Improvements(Use if altering the code): 
"""


#==-Libraries-==#
import time
import random as rand


#====-Functions-====#


#==========-Introduction-==========#


def intro():
    print('''
        ╔════════════════════════════════════════╗
        ║        Welcome to the Dunegeon!        ║
        ║                                        ║
        ║   In this you will be entering three   ║
        ║     different dungens and fighting     ║
        ║        a variety of enemies.           ║
        ║                                        ║
        ║    You start in a Tavern with with a   ║
        ║ board full of three different dungeons ║
        ║    with elemental enemies and LOOT!    ║
        ║                                        ║
        ║  Once you have completed the dungeons  ║
        ║   you will unload a FINAL DUNGEON!!!   ║
        ║  where you will fight the final boss.  ║
        ╚════════════════════════════════════════╝
''')
    time.sleep(7)
    print('''
        Note: Goose noises are best experienced
        when spoken aloud.
''')
    tavern()


#==========-Tavern-==========#

    
def tavern():
    print('''
        ╔════════════════════════════════════════════════╗
        ║     You enter The Thieving Goose Tavern. A     ║
        ║    mildly popular tavern loctaed conveniently  ║
        ║    in the area of four dungeons filled with    ║
        ║               danger and loot.                 ║
        ║                                                ║
        ║  Inside the tavern you see a mischievous band  ║
        ║  of treasure hunter and pirates. The perfect   ║
        ║ place for you to be. Across from the enterance ║
        ║ sits a board with places for treasure hunters  ║
        ║              like you to explore.              ║
        ╚════════════════════════════════════════════════╝
''')
    time.sleep(8)
    while True:
        choice = input('''
        ┌────────────────────────────────────────────────────┐
        │ What would you like to do? Talk to the {B}artender,│
        │ Start a bar {F}ight, Look at the {Q}uest board,    │
        │             pet the tavern {G}oose.                │            
        └────────────────────────────────────────────────────┘
    ''')

        if(choice == 'B' or choice == 'b'):
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
            time.sleep(1)
            print('''
            The bartender's Swedish.
            ''')
            time.sleep(1)
            print('''
            ╔══════════════════════════════════╗
            ║ BarTender Goose: hjörnk angirly. ║
            ╚══════════════════════════════════╝
            ''')
            time.sleep(1)
            print('''
            It seems that the bartender is now angry
            ''')
            time.sleep(1)
            print('''
            ╔════════════════════════════════╗
            ║ BarTender Goose: hjörnk börnk. ║
            ╚════════════════════════════════╝
            ''')
            time.sleep(2)
            print('''
            The bartender bit you taking some coins.
            But they gave you a drink!
            ''')
        elif(choice == 'F' or choice == 'f'):
            print('''
            you aproach a table filled with GEESE?!
            IN PIRATE COSTUMES?!
            ''')
            time.sleep(3)
            print('''
            ╔══════════════════════════════════════╗
            ║ The Pirate Geese Gang: haaaaarrggnk. ║
            ╚══════════════════════════════════════╝
            ''')
            time.sleep(1)
            print('''
            The all swarm you and bites you with
            their golden becks.
            ''')
        elif(choice == 'Q' or choice == 'q'):
            quest()
        elif(choice == 'G' or choice == 'g'):
            print('''
            you walk over to the taverens famous
            goose. you go to pat it but it quickly
            shivels and bites you.
    ''')


#==========-Quest-Board-==========#

            
def quest():
    print('''
            You aproach the quest board, you see three
            pices of paper held to the board using throwing
            knives. 
            
''')
    time.sleep(3)
    qchoice = input('''
        ┌────────────────────────────────────────────────────────┐
        │ Which quest do you pick? {F}ire Dungeon, {I}ce Dungeon │
        │               or the {E}arth Dungeon?                  │
        └────────────────────────────────────────────────────────┘
    ''')
    if(qchoice == 'F' or qchoice == 'f'):
        print('Loading Dungeon....')
        time.sleep(9)
        fired()
    if(qchoice == 'I' or qchoice == 'i'):
        print('Loading Dungeon....')
        time.sleep(9)
        iced()
    if(qchoice == 'E' or qchoice == 'e'):
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
        on your sword. Yopu see that in the center of the
        room ther is a swarm of garden knomes. You kick on over
        the ledge into the lava pools below. Doing this sets off
        somethin in the remaining knomes, their eyes light up with
        a burning passion.
''')
    time.sleep(8)
    fire_gob()
    fire_gob()
    fire_gob()
    fire_gob()
    fire_gob()
    fire_gob()
    fire_gob()
    fire_gob()
    print('''
        After smashing all the gnomes a pair of red firey eyes gleaming
        down on you. 
''')
    time.sleep(1)
    fire_drag()
    tavern()


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
        cave across in the other side of the room. But then the ice pillars
        begin to shake and shatter reveiling that the gnomes are infact
        sentient and ready to fight.
''')
    time.sleep(8)
    ice_gob()
    ice_gob()
    ice_gob()
    ice_gob()
    ice_gob()
    ice_gob()
    ice_gob()
    ice_gob()
    print('''
        After defeating all the gnomes you continue back towards the cave
        but now these seems to be more mist coming from out of the cave
        than before. Apon touching the mist yoour legs begin to freeze up.
        Again not because your scared, just the mist is really cold. A
        menacing reveils itself as the being causing the mist.
''')
    time.sleep(1)
    ice_drag()
    tavern()


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
    earth_gob()
    earth_gob()
    earth_gob()
    earth_gob()
    earth_gob()
    print('''
        After defeating the gnomes an older looking dragon walks in, catching
        you standing over the remains of his precious gnome collection.
''')
    time.sleep(1)
    earth_drag()
    tavern()


#==========-Fire-Gnome-==========#

    
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
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
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
        ╒═════════════════════════════════════════╕
        │ the Fire Goblin hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(dum_att))
        if(fg_hp < 1):
            coin = rand.randint(14,17)
            
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            int(users[0])+coin
            time.sleep(1)
    

#==========-Earth-Gnome-==========#

            
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
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
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
        ╒══════════════════════════════════════════╕
        │ the Earth Goblin hit you doing {} damage │
        ╘══════════════════════════════════════════╛'''.format(dum_att))
        if(eg_hp < 1):
            coin = rand.randint(13,16)
            
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            int(users[0])+coin
            time.sleep(1)


#==========-Ice-Gnome-==========#

            
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
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
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
        ╒════════════════════════════════════════╕
        │ the Ice Goblin hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(dum_att))
        if(ig_hp < 1):
            coin = rand.randint(12,16)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            int(users[0])+coin
            time.sleep(1)


#==========-Fire-Dragon-==========#

            
def fire_drag():
    fd_hp = 120
    global player_hp
    print('''
        ╔════════════════════════════════════════╗
        ║ Fire Dragon: enter witty comment here. ║
        ╚════════════════════════════════════════╝
    ''')
    time.sleep(1)
    while(player_hp > 0 and fd_hp > 0):
        attack = input("""
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
        """)
        time.sleep(1)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(12,14)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            fd_hp -= damage
            fd_att = rand.randint(7,12)
            player_hp -= fd_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Fire Dragon hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(fd_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',fd_hp)
            time.sleep(1)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(14,15)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(1)
            fd_hp -= damage
            fd_att = rand.randint(7,12)
            player_hp -= fd_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Fire Dragon hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(fd_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',fd_hp)
            time.sleep(1)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(9,11)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(1)
            fd_hp -= damage
            fd_att = rand.randint(7,12)
            player_hp -= fd_att
            print('''
        ╒════════════════════════════════════════╕
        │ the Fire Dragon hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(fd_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',fd_hp)
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
        ╒═════════════════════════════════════════╕
        │ the Fire Dragon hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(dum_att))
        if(fd_hp < 1):
            coin = rand.randint(23,41)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            int(users[0])+coin
            time.sleep(1)


#==========-Ice-Dragon-==========#

            
def ice_drag():
    id_hp = 130
    global player_hp
    print('''
        ╔═══════════════════════════════════════╗
        ║ Ice Dragon: enter witty comment here. ║
        ╚═══════════════════════════════════════╝
    ''')
    time.sleep(1)
    while(player_hp > 0 and id_hp > 0):
        attack = input("""
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
        """)
        time.sleep(1)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(12,14)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            id_hp -= damage
            id_att = rand.randint(18,23)
            player_hp -= id_att
            print('''
        ╒═══════════════════════════════════════╕
        │ the Ice Dragon hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(id_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',id_hp)
            time.sleep(1)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(14,15)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(1)
            id_hp -= damage
            id_att = rand.randint(18,23)
            player_hp -= id_att
            print('''
        ╒═══════════════════════════════════════╕
        │ the Ice Dragon hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(id_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',id_hp)
            time.sleep(1)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(9,11)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(1)
            id_hp -= damage
            id_att = rand.randint(18,23)
            player_hp -= id_att
            print('''
        ╒═══════════════════════════════════════╕
        │ the Ice Dragon hit you doing {} damage │
        ╘═══════════════════════════════════════╛'''.format(id_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',id_hp)
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
        ╒════════════════════════════════════════╕
        │ the Ice Dragon hit you doing {} damage │
        ╘════════════════════════════════════════╛'''.format(dum_att))
        if(id_hp < 1):
            coin = rand.randint(21,39)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            int(users[0])+coin
            time.sleep(1)    


#==========-Earth-Dungeon-==========#

            
def ear_drag():
    ed_hp = 170
    global player_hp
    print('''
        ╔═════════════════════════════════════════╗
        ║ Earth Dragon: enter witty comment here. ║
        ╚═════════════════════════════════════════╝
    ''')
    time.sleep(1)
    while(player_hp > 0 and ed_hp > 0):
        attack = input("""
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
        """)
        time.sleep(1)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(12,14)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            ed_hp -= damage
            ed_att = rand.randint(16,21)
            player_hp -= ed_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Earth Dragon hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(ed_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',ed_hp)
            time.sleep(1)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(14,15)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(1)
            ed_hp -= damage
            ed_att = rand.randint(16,21)
            player_hp -= ed_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Earth Dragon hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(ed_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',ed_hp)
            time.sleep(1)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(9,11)
            print('''
        ╓─────────────────────────╖
        ║ you hit doing {} damage ║
        ╙─────────────────────────╜'''.format(damage))
            time.sleep(1)
            ed_hp -= damage
            ed_att = rand.randint(16,21)
            player_hp -= ed_att
            print('''
        ╒═════════════════════════════════════════╕
        │ the Earth Dragon hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(ed_att))
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',ed_hp)
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
        ╒══════════════════════════════════════════╕
        │ the Earth Dragon hit you doing {} damage │
        ╘══════════════════════════════════════════╛'''.format(dum_att))
        if(ed_hp < 1):
            coin = rand.randint(22,40)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            int(users[0])+coin
            time.sleep(1)


#==========-Hydra-Goose-==========#

            
def hydra_goose():
    hydg_hp = 160
    head = 1
    global player_hp
    print('''
        ╔════════════════════════════════════════╗
        ║ Hydra Goose: enter witty comment here. ║
        ╚════════════════════════════════════════╝
    ''')
    time.sleep(1)
    while(player_hp > 0 and hydg_hp > 0):
        attack = input("""
        ┌─────────────────────────────────────────────────────┐
        │ Select a weapon: {S}word, {B}ow, {M}allet, {P}otion │
        └─────────────────────────────────────────────────────┘
        """)
        time.sleep(1)
        if(attack == 's' or attack == 'S'):
            damage = rand.randint(12,14)
            print('''
        ╓──────────────────────────────────────────╖
        ║ you hit using your sword doing {} damage ║
        ╙──────────────────────────────────────────╜'''.format(damage))
            time.sleep(1)
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
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',hydg_hp)
            time.sleep(1)
        elif(attack == 'b' or attack == 'B'):
            damage = rand.randint(8,10)
            print('''
        ╓────────────────────────────────────────╖
        ║ you hit using your bow doing {} damage ║
        ╙────────────────────────────────────────╜'''.format(damage))
            time.sleep(1)
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
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',hydg_hp)
            time.sleep(1)
        elif(attack == 'm' or attack == 'M'):
            damage = rand.randint(12,15)
            print('''
        ╓───────────────────────────────────────────╖
        ║ you hit using your mallet doing {} damage ║
        ╙───────────────────────────────────────────╜'''.format(damage))
            time.sleep(1)
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
            time.sleep(1)
            print('''
        Your health:''',player_hp)
            time.sleep(1)
            print('''
        Enemies health:''',hydg_hp)
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
        ╒═════════════════════════════════════════╕
        │ the Hydra Goose hit you doing {} damage │
        ╘═════════════════════════════════════════╛'''.format(dum_att))
        if(hydg_hp < 1):
            coin = rand.randint(45,120)
            print('''
        ╓──────────────────╖
        ║ you got {} coins ║
        ╙──────────────────╜'''.format(coin))
            int(users[0])+coin
            time.sleep(1)
        

#====-Main Routine-====#

            
global player_hp
player_hp = 100
coin = ['0']
fg_hp = 60
ig_hp = 40
eg_hp = 80
hydg_hp = 160

intro()





            
