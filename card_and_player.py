class deck_building:

    """ all deck_buildig have :
    public elements:
            buildig_name,
            building_price,
            color_street, 
            is_mourtaged, 
            buildig_fee_globa, 
            players_on_building = []
            owner='Bank', 
            picture=None
    functions:
        __str__(self)
        mourtage_price(self)
        hotel(self) """

    def __init__(self, buildig_name,
                 building_price,
                 color_street,
                 is_mourtaged,
                 buildig_fee_globa,
                 players_on_building=[],
                 perhouse_price,
                 owner='Bank',
                 picture=None
                 ):

        self.buildig_name = buildig_name
        self.building_price = building_price
        self.color_street = color_street  # neighborhood po dobre vunshen
        self.is_mourtaged = is_mourtaged
        self.buildig_fee_globa = buildig_fee_globa
        self.players_on_building = players_on_building
        self.perhouse_price = perhouse_price
        self.owner = owner
        self.house_count = 0  # (4<= houses ,  5==hotel)!!!!!!!!
        self.picture = picture  # optional
        #kompromis za tochnost ne moga da namerq formulata ... 
        self.with_house_fee = [self.buildig_fee_globa,
                               5 * self.buildig_fee_globa, 
                               15 * self.buildig_fee_globa,
                               45 * self.buildig_fee_globa,
                               62 * self.buildig_fee_globa,
                               80 * self.buildig_fee_globa]

        
    def show_building_info(self):
        print('Name: ',self.buildig_name,'\n',
            'price: ',self.building_price,'\n',
            'mourtage: ',self.mourtage_price,'\n',
            'One house price: ',self.perhouse_price,'\n',
            'Rent: \n'
            'None one two tree four hotel ',self.with_house_fee,'\n')
        #return None 

    def mourtage_price(self):
        return self.building_price / 2

    def kak_da_namerq_liniq_ot_ulici(self):
        pass
    

    def get_building_name(self):
        return self.buildig_name


    def take_fee(self):
        return self.with_house_fee[self.house_count]


    def __str__(self):
        print(
            'Name of building: ', self.buildig_name, ', price is: ', self.building_price,
            ', color is:', self.color_street, '.\n', ' Mourtaged value is: ', self.is_mourtaged,
            ', owner is ', self.owner, ', house count is ', self.house_count, '.')
        return str(self.owner)