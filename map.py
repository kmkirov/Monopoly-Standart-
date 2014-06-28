import random

from building import *
from global_variables import LIST_OF_BUILDINGS
BANK = 'BANK'
CONST_HOUSE = 5
FORBIDDEN = [0, 2, 4, 7, 10, 17, 20, 22, 30, 33, 36, 38]


class mapa:

    def __init__(self):
        self._deck = list(LIST_OF_BUILDINGS)

    def __getitem__(self, i):
        return self._deck[i]

    # def get_building(self, building_position):
    #    return self._deck[building_position]

    def buy_building(self, building_index, player, auction):
        # print(player)
        """
        1)  за предпазване от странно поведени се проверява дали сградата не се притежава от играча
        2)  check if it is posible to buy a building (community, tax , cant be bought)
        3) bug first building change ownership and if succeed building is add to the list of buildings
        """
        if self._deck[building_index] in player.get_items():
            # else:
            return False  # zashtooooooooo ne raboti inacheee
        if building_index in FORBIDDEN:
            return False

        if self._deck[building_index].buy_building(player, auction):
            player.add_items(self._deck[building_index])
            return True
        return False

    def trade_buildings(self, offerer, offerer_buildings_index, offerer_money, receiver, receiver_buildings_index, receiver_money):
        """
        Много е важно да приема лист от сгради и ако няма сгради да се пише 0 вътре
        1) по подадения списък на сградите прави списък от обекти на тези сгради(индексите)
        2) проверява дали подадените сгради наистина принадлежат на съответния играч
        3) осъществява размяната на сградите и после на парите (ако имаше и карти и тях)
        """
        offerer_buildings = []
        receiver_buildings = []

        if 0 not in offerer_buildings_index:
                offerer_buildings = [self._deck[i]
                                     for i in offerer_buildings_index]
        if 0 not in receiver_buildings_index:
                receiver_buildings = [self._deck[i]
                                      for i in receiver_buildings_index]

        if not set(offerer_buildings).issubset(offerer.get_items()) or
            not set(receiver_buildings).issubset(receiver.get_items()):
            return False  # some of buildings are not owned  ...

        for building in offerer_buildings:
            receiver.get_items().append(building)
            self._deck[self._deck.index(building)].change_owner(receiver)
            offerer.get_items().remove(building)

        for building in receiver_buildings:
            offerer.get_items().append(building)
            # tell building about new owner
            self._deck[self._deck.index(building)].change_owner(offerer)
            receiver.get_items().remove(building)

        if offerer.player_budget() >= offerer_money and receiver.player_budget() >= receiver_money:
            offerer.add_money(receiver_money)
            offerer.pay_money(offerer_money)
            receiver.add_money(offerer_money)
            receiver.pay_money(receiver_money)
        else:
            return False
        return True

    # nqma proverka za jal zashtoto se vika ot chest i chance
    # return old position of the plar
    def move_player_by_roll(self, player, steps):
        player.move_from_to(steps)
        # self._deck[positions[0]].all_players().remove(player)  # ne go polzvam !
        # self._deck[positions[1]].all_players().append(player)  # ne go
        # polzvam !
        pass  # nenujna

    def move_player_to_position(self, player, position):  # chance and chest
        """
        The main idea is to give the number of steps between
         current position and new position+ without for go 200$ (can be go to jail steps)
        """
        positions = player.move_from_to(0)[0]
        counter = 0
        if positions == position:
            return True
        # self._deck[positions].remove(player)#ne go polzvam !
        # self._deck[position].append(player)

        if positions < position:
            self.move_player_by_roll(player, position - positions)
            return position - positions  # kolko stypki da mine gui
        elif positions > position:
            while positions != position:
                positions = (positions + 1) % len(self._deck)
                counter = counter + 1

            self.move_player_by_roll(player, counter - 1)
            #print(counter, 'mnogo podvejdasht counter')
            # return the number of positions to move ahead...
            return counter - 1
