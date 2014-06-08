COMMUNITY_CHEST = [['Advance to Go (collect $200)', [200, 0]],
                   ['Go to jail – go directly to jail – Do not pass Go, do not collect $200', [0,10]],
                   ['You are assessed for street repairs – $40 per house, $115 per hotel', [40,115]],
                   
                   
                   
                   
                   ['Get out of jail free' , []], 
                   
                   
                   ['It is your birthday Collect $10 from each player', [10]],
                   ['Grand Opera Night – Collect $50 from every player for opening night seats', [50]],
                   
                                      
                   ['Pay Hospital Fees of $100', [100]],
                   ['Pay School Fees of $50', [50]] ,
                   ['Doctor\'s fees – Pay $50', [50]],

                   ['Income Tax refund – collect $20',[ 20]],
                   ['Bank error in your favor – collect $75', [75]],
                   ['Life Insurance Matures – collect $100', [100]],
                   ['Receive $25 Consultancy Fee (collect)', [25]],                   
                   ['You have won second prize in a beauty contest– collect $10', [10]],
                   ['You inherit $100 (collect )', [100]],
                   ['From sale of stock you get $50 (collect)', [50]],
                   ['Holiday Fund matures - Receive $100 (collect)', [100]]
                ]
#– this card may be kept until needed, or sold' 333333
lucky_regex = {'Get_money':r'collect',
               'Pay_money':r'Collect',
               'Jail_free':r'Get out of jail free',
               'Jail_in ':r'Go to jail',
               'Pay': r'Pay',
               'Hotel_pay':r'hotel', 
               'Go_option':'Advance',
               'Each':r'each',
               'utility' : r'utility',
               'pay_each' :r'pay each player',
               'Spaces' : r'back 3 spaces'
              }     

BANK='BANK'
CHANCE = [ ['Advance to Go (collect $200)', [200,0]],
           ['Advance to Illinois Ave.', [200,24]],
           ['Take a walk on the Boardwalk – advance token to Boardwalk', [0,39]],
           ['Go directly to Jail – do not pass Go, do not collect $200', [0,10]],
           ['Advance to St. Charles Place – if you pass Go, collect $200', [200,11]],
           ['Take a trip to Reading Railroad – if you pass Go collect $200', [200,  5]],
           
           ['Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned,\
              throw dice and pay owner a total ten times the amount thrown.', [12,28,10]],
           
           ['Advance token to the nearest Railroad and pay owner twice the rental to which she is otherwise entitled.\
             If Railroad is unowned, you may buy it from the Bank. (There are two of these.)', [5,15,25,35]],
           ['Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled.\
             If Railroad is unowned, you may buy it from the Bank. (There are two of these.)',[5,15,25,35]],   
           

           ['Go back 3 spaces', [-3]],
          
   
           ['Get out of Jail free – this card may be kept until needed, or traded/sold', []],
           
           ['Make general repairs on all your property – for each house pay $25 – for each hotel $100', [25,100]],

           ['Pay poor tax of $15', [15]],
          
           ['Bank pays you dividend of $50 (collect)', [50]],
           ['You have been elected chairman of the board – pay each player $50', [50]],
           ['Your building loan matures collect $150', [150] ],
           ['You have won a crossword competition - collect $100 ', [100]]
           ]
GO_MONEY =200
#if da e duma, ne e napraveno
lucky_regex = {'Get_money':r'collect',
               'nearest' :r'nearest',
               'If':r'if',               
               'Jail_free':r'Get out of jail free',
               'Jail_in':r'Go to jail',
               'Pay': r'Pay',
               'Hotel_pay':r'hotel', 
               'Go_option':r'Advance',
               'Each':r'(each|every)',
               'utility' : r'utility',
               'pay_each' :r'pay each player',
               'Spaces' : r'back 3 spaces',
                'Collect' : 'Collect'
              }



DICT_OF_COLORS = {'Purple':2, 'Light-Green':3, 'Violet':3, 'Orange':3,
                  'Red':3 , 'Yellow':3, 'Dark-Green':3, 'Dark-Blue':2}











from building import *
LIST_OF_BUILDINGS = [
    building('GO', 'FREE', 0, 0, 0),   
    building('Mediterranean Ave.',  'Purple', 60,
                  50, 2, 10,     30,     90,  160,   250),
    building('Comunity Chest', 'CC', 0, 0),
    building('Baltic Ave.',         'Purple', 60,
                  50, 4, 20,     60,    180,  320,   450),
    building('Income Tax','TAX', 0,0,200),
    building('READING RAILROAD', 'STATION', 200, 25),
    building('Oriental Ave.',       'Light-Green', 100,
                  50, 6, 30,     90,   270,  400,   550),
    building('CHANCE', 'C', 0, 0),
    
    building('Vermont Ave.',      'Light-Green', 100,
                  50, 6, 30,     90,  270,  400,   550),
    building('Connecticut Ave.',    'Light-Green', 120,
                  50, 8, 40,     100,  300,  450,   600),
    building('JUST VISITING', 'FREE', 0, 0),
    building('St. Charles Place',   'Violet', 140,
                  100, 10, 50,     150,   450,   625,    750),
    building('Electronic Company', 'utility', 150),
    building('States Ave.',  'Violet', 140,
                  100, 10, 50,      150,   450,   625,   750),
    building('Virginia Ave.', 'Violet', 160,
                  100, 12, 60,      180,   500,   700,   900),
    building('PENSYLVANIA R.R.', 'STATION', 200, 25),
    building('St. James Place', 'Orange', 180,
                  100, 14, 70,      200,   550,   750,   950),
    building('Comunity Chest', 'CC', 0, 0),
    building('Tennessee Ave.', 'Orange', 180,
                  100, 14, 70,      200,   550,   750,   950),
    building('New York Ave.', 'Orange',  200,
                  100, 16, 80,   220,  600,  800,  1000),
    building('Free Parking', 'FREE', 0, 0, 0),
    building('Kentucky Ave.', 'Red',  220,
                  150, 18, 90,   250, 700, 875, 1050),
    building('CHANCE', 'C', 0, 0),
    building('Indiana Ave.', 'Red',  220,
                  150, 18, 90,     250,  700,  875,  1050),
    building('Illinois Ave.', 'Red',  240,
                  150, 20, 100,     300,  750,  925,  1100),
    building('B. & O. RAILROAD', 'STATION', 200, 25),
    building('Atlantic Ave.', 'Yellow',  260,
                  150, 22, 110,     330,  800,   975, 1150),
    building('Ventnor Ave.', 'Yellow',  260,
                  150, 22, 110,     330,  800,   975,  1150),
    building('Water Work', 'utility', 150),
    building('Marvin Gardens', 'Yellow', 280,
                  150, 22, 120,     360,  850,   1025,  1200),
    building('JAIL', 'JAIL', 0, 0),
    building('Pacific Ave.', 'Dark-Green',   300,
                  200, 26, 130,     390,  900,   1100,  1275),
    building('North Carolina Ave.', 'Dark-Green',    300,
                  200, 26, 130,     390,  900,   1100, 1275),
    building('Comunity Chest', 'CC', 0, 0),
    building('Pennsylvania Ave.', 'Dark-Green',     320,
                  200, 28, 150,     450,  1000,   1200, 1400),
    building('SHORT LINE R.R.',  'STATION', 200, 25),
    building('CHANCE', 'C', 0, 0),
    building('Park Place', 'Dark-Blue',      350,
                  200, 35, 175,     500,  1100,   1300, 1500),
    building('Luxyry Tax','TAX',0,0 ,75),
    building('Boardwalk', 'Dark-Blue',       400,
                  200, 50, 200,     600,  1400,    1700, 2000),
]
#BUILDING_NAMEORDER = [building.get_name() for building in LIST_OF_BUILDINGS]





