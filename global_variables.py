#Community Chest list:

COMMUNITY_CHEST = {'Advance to Go (Collect $200)': 200,
                   'Bank error in your favor – collect $75': 75,
                   'Doctor\'s fees – Pay $50': 50,
                   'Get out of jail free – this card may be kept until needed, or sold': card_collection + 1
                   'Go to jail – go directly to jail – Do not pass Go, do not collect $200': 200
                   'It is your birthday Collect $10 from each player': 10,
                   'Grand Opera Night – collect $50 from every player for opening night seats': 50
                   'Income Tax refund – collect $20': 20
                   'Life Insurance Matures – collect $100': 100,
                   'Pay Hospital Fees of $100': 100,
                   'Pay School Fees of $50': ,
                   'Receive $25 Consultancy Fee': 25,
                   'You are assessed for street repairs – $40 per house, $115 per hotel': perhotel,
                   'You have won second prize in a beauty contest– collect $10': 10,
                   'You inherit $100': 100,
                   'From sale of stock you get $50': 50,
                   'Holiday Fund matures - Receive $100': 100
                   }

#Chance list:

CHANCE = {'Advance to Go (Collect $200)': 200,
          'Advance to Illinois Ave.': index[ave],
          'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned,\
              throw dice and pay owner a total ten times the amount thrown.': 2x,
          'Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled.\
             If Railroad is unowned, you may buy it from the Bank. (There are two of these.)': 2x,
          'Advance to St. Charles Place – if you pass Go, collect $200': 200,
          'Bank pays you dividend of $50': 50,
          'Get out of Jail free – this card may be kept until needed, or traded/sold': jail,
          'Go back 3 spaces', cur[index - 3],
          'Go directly to Jail – do not pass Go, do not collect $200': 200,
          'Make general repairs on all your property – for each house pay $25 – for each hotel $100': perhotel,
          'Pay poor tax of $15': 15,
          'Take a trip to Reading Railroad – if you pass Go collect $200': 200 + indexdetect,
          'Take a walk on the Boardwalk – advance token to Boardwalk': index,
          'You have been elected chairman of the board – pay each player $50': 50 each
          'Your building loan matures – collect $150': 150,
          'You have won a crossword competition - collect $100 ': 100}


list_of buildings = [
    deck_building('GO', 'FREE', 0, 0, 0),
    deck_building('Mediterranean Ave.',  'Purple', 60,
                  50, 2, 10,     30,     90,  160,   250),
    deck_building('Comunity Chest', 'FREE', 0, 0)
    deck_building('Baltic Ave.',         'Purple', 60,
                  50, 4, 20,     60,    180,  320,   450),
    deck_building('Income Tax', 200)
    deck_building('READING RAILROAD', 'station', 200, 25)
    deck_building('Oriental Ave.',       'Light-Green', 100,
                  50, 6, 30,     90,   270,  400,   550),
    deck_building('CHANCE', 'FREE', 0, 0)
    deck_building('Vermont Ave.',      'Light-Green', 100,
                  50, 6, 30,     90,  270,  400,   550),
    deck_building('Connecticut Ave.',    'Light-Green', 120,
                  50, 8, 40,     100,  300,  450,   600),
    deck_building('JUST VISITING', 'FREE', 0, 0)
    deck_building('St. Charles Place',   'Violet', 140,
                  100, 10, 50,     150,   450,   625,    750),
    deck_building('Electronic Company', 'utility', 150, row)
    deck_building('States Ave.',  'Violet', 140,
                  100, 10, 50,      150,   450,   625,   750),
    deck_building('Virginia Ave.', 'Violet', 160,
                  100, 12, 60,      180,   500,   700,   900),
    deck_building('PENSYLVANIA R.R.', 'station', 200, 25)
    deck_building('St. James Place', 'Orange', 180,
                  100, 14, 70,      200,   550,   750,   950),
    deck_building('Comunity Chest', 'FREE', 0, 0)
    deck_building('Tennessee Ave.', 'Orange', 180,
                  100, 14, 70,      200,   550,   750,   950),
    deck_building('New York Ave.', 'Orange',  200,
                  100, 16, 80,   220,  600,  800,  1000),
    deck_building('Free Parking', 'FREE', 0, 0, 0)
    deck_building('Kentucky Ave.', 'Red',  220,
                  150, 18, 90,   250, 700, 875, 1050),
    deck_building('Indiana Ave.', 'Red',  220,
                  150, 18, 90,     250,  700,  875,  1050),
    deck_building('Illinois Ave.', 'Red',  240,
                  150, 20, 100,     300,  750,  925,  1100),
    deck_building('B. & O. RAILROAD', 'station', 200, 25)
    deck_building('Atlantic Ave.', 'Yellow',  260,
                  150, 22, 110,     330,  800,   975, 1150),
    deck_building('Ventnor Ave.', 'Yellow',  260,
                  150, 22, 110,     330,  800,   975,  1150),
    deck_building('Water Work', 'utility', 150, row)
    deck_building('Marvin Gardens', 'Yellow', 280,
                  150, 22, 120,     360,  850,   1025,  1200),
    deck_building('JAIL', 'FREE', 0, 0)
    deck_building('Pacific Ave.', 'Dark-Green',   300,
                  200, 26, 130,     390,  900,   1100,  1275),
    deck_building('North Carolina Ave.', 'Dark-Green',    300,
                  200, 26, 130,     390,  900,   1100, 1275),
    deck_building('Comunity Chest', 'FREE', 0, 0)
    deck_building('Pennsylvania Ave.', 'Dark-Green',     320,
                  200, 28, 150,     450,  1000,   1200, 1400),
    deck_building('SHORT LINE R.R.',  'station', 200, 25)
    deck_building('CHANCE', 'FREE', 0, 0)
    deck_building('Park Place', 'Dark-Blue',      350,
                  200, 35, 175,     500,  1100,   1300, 1500),
    deck_building('Luxyry Tax', 75)
    deck_building('Boardwalk', 'Dark-Blue',       400,
                  200, 50, 200,     600,  1400,    1700, 2000)
]


#groups of buildings

can_build_groups = [['Mediterranean Ave.', 'Baltic Ave.'],
                    ['Oriental Ave.', 'Vermont Ave.', 'Connecticut Ave.'],
                    ['St. Charles Place', 'States Ave.', 'Virginia Ave.'],
                    ['St. James Place', 'Tennessee Ave.', 'Pentonville Road'],
                    ['The Angel Islington', 'Euston Road', 'New York Ave.'],
                    ['Kentucky Ave.', 'Indiana Ave.', 'Illinois Ave.'],
                    ['Atlantic Ave.', 'Ventnor Ave.', 'Marvin Gardens'],
                    ['Pacific Ave.', 'North Carolina Ave.',
                        'Pennsylvania Ave.'],
                    ['Park Place', 'Boardwalk']
                    ]






"""


deck_building('B. & O. RAILROAD', 'station', 200, 25)
deck_building('SHORT LINE R.R.',  'station', 200, 25)
deck_building('READING RAILROAD', 'station', 200, 25)
deck_building('PENSYLVANIA R.R.', 'station', 200, 25)
deck_building('Water Work', 'utility',150,row)
deck_building('Electronic Company', 'utility',150,row)

deck_building('Free Parking', 'FREE',0,0,0)
deck_building('GO', 'FREE',0,0,0)
deck_building('CHANCE', 'FREE',0,0)
deck_building('Comunity Chest', 'FREE',0,0)
deck_building('JAIL', 'FREE',0,0)
deck_building('JUST VISITING', 'FREE',0,0)
deck_building('Income Tax',200)
deck_building('Luxyry Tax',75)


        property            color     value_purchase    value_house   rent_base    rent_house1  rent house2 rent_house3  rent house4 house5=hotel 

        Mediterranean Ave.  Purple          60      50      2   10      30      90      160     250
        Baltic Ave.         Purple          60      50      4   20      60      180     320     450
        Oriental Ave.       Light-Green     100     50      6   30      90      270     400     550
        Vermont Ave.        Light-Green     100     50      6   30      90      270     400     550  
        Connecticut Ave.    Light-Green     120     50      8   40      100     300     450     600
        St. Charles Place   Violet          140     100      10  50      150     450     625     750
        States Ave.         Violet          140     100      10  50      150     450     625     750
        Virginia Ave.       Violet          160     100      12  60      180     500     700     900
        St. James Place     Orange          180     100      14  70      200     550     750     950
        Tennessee Ave.      Orange          180     100      14  70      200     550     750     950
        New York Ave.       Orange          200     100     16  80      220     600     800     1000
        Kentucky Ave.       Red             220     150     18  90      250     700     875     1050
        Indiana Ave.        Red             220     150     18  90      250     700     875     1050
        Illinois Ave.       Red             240     150     20  100     300     750     925     1100
        Atlantic Ave.       Yellow          260     150     22  110     330     800     975     1150
        Ventnor Ave.        Yellow          260     150     22  110     330     800     975     1150
        Marvin Gardens      Yellow          280     150     22  120     360     850     1025    1200
        Pacific Ave.        Dark-Green      300     200     26  130     390     900     1100    1275
        North Carolina Ave. Dark-Green      300     200     26  130     390     900     1100    1275
        Pennsylvania Ave.   Dark-Green      320     200     28  150     450     1000    1200    1400
        Park Place          Dark-Blue       350     200     35  175     500     1100    1300    1500
        Boardwalk           Dark-Blue       400     200     50  200     600     1400    1700    2000

"""


