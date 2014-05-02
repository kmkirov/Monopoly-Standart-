class Player:
    def __init__(self, player_name,picture=None):
        self.player_name = player_name
        self.budget = 1500
        self.houses = 0
        self.list_of_items = []
        self.picture = picture
        self.in_jail = False
        self.list_cards = []
        self.position = 0
        self.is_bancrupt = False

    def can_pay(price):
        return price <= self.budget


    def name(self):
        return self.player_name


    def is_playing(self):
        return self.is_bancrupt == False




\#globalen////\\\\
deck_buldings_ordered=[  deck_building('start',0,'BLACK',0 ),
        deck_building('Old Kent Road',60,'brown',False, 2 ),
        deck_building('Whitechapel Road',60,'brown',False, 4 ),
        deck_building( 'Take Card',0,'BLACK',False, 0),
        deck_building('Station',200,'BLACK',False, 25 ),
        deck_building('cheshma',150,'BLACK',False, 0 ),
        deck_building( 'Old Kent Road',200,'red',False, 10),
        deck_building('Old Kent Road',600,'red',False, 200 ),
        deck_building( 'Old Kent Road',300,'red',False, 20),
]
        
chance_index_arr = [('vzemam 30',30),('str',value) ] #da gi razmesvam predi igra
comunity_chest



