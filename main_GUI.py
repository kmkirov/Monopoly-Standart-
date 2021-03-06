import pygame
import sys
from pygame.locals import *
import threading
from multiprocessing import Process, Value
import time
import pygame
import pygame.font
import pygame.event
import pygame.draw
import string

from game import Game
from gui_functions import *
BUY = 0
MOURTAGE = 1
HOUSE = 2
MOVE = 3


def f(game):

    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 600
    y_position = 0
    text_lenght = 150
    x_text_border = 30
    y_text_border = 40

    roll_button = Button()
    roll_button.create_button(DISPLAYSURF, bg_color, x_position, y_position,
                              text_lenght, x_text_border, y_text_border, 'Roll', text_color)
    #                       range(start, end)   step
    y_position = (i for i in range(10, 550) if i % 45 == 0)

    end_turn = Button()
    end_turn.create_button(DISPLAYSURF, bg_color, x_position, next(
        y_position), text_lenght, x_text_border, y_text_border, 'end_turn', text_color)
    mourtage = Button()
    mourtage.create_button(DISPLAYSURF, bg_color, x_position, next(
        y_position), text_lenght, x_text_border, y_text_border, 'mourtage', text_color)
    unmourtage = Button()
    unmourtage.create_button(DISPLAYSURF, bg_color, x_position, next(
        y_position), text_lenght, x_text_border, y_text_border, 'unmourtage', text_color)
    trade = Button()
    trade.create_button(DISPLAYSURF, bg_color, x_position, next(y_position),
                        text_lenght, x_text_border, y_text_border, 'trade', text_color)
    sell = Button()
    sell.create_button(DISPLAYSURF, bg_color, x_position, next(y_position),
                       text_lenght, x_text_border, y_text_border, 'sell', text_color)
    build = Button()
    build.create_button(DISPLAYSURF, bg_color, x_position, next(y_position),
                        text_lenght, x_text_border, y_text_border, 'build', text_color)
    rules = Button()
    rules.create_button(DISPLAYSURF, bg_color, x_position, next(
        y_position), text_lenght, x_text_border, y_text_border, 'rules', text_color)
    register = Button()
    register.create_button(DISPLAYSURF, bg_color, x_position, next(
        y_position), text_lenght, x_text_border, y_text_border, 'rules', text_color)
    bancrupt = Button()
    bancrupt.create_button(DISPLAYSURF, bg_color, x_position, next(
        y_position), text_lenght, x_text_border, y_text_border, 'bancrupt', text_color)
    # pygame.image.save(pygame.display.get_surface(),'C:/Python33/pictures/resized.bmp')
    #name= Button()
    #name.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,name,text_color)
    pygame.display.update()
#processes = Process(target=f, )

"""
players_move_icons = {}
players_buy_icons = {}
players_mortage_icons = {}


players_buy_icons[1]= pygame.image.load( 'players_icons/car - own.gif')
players_mortage_icons[1]= pygame.image.load('players_icons/car - mortage.gif')
players_move_icons[1]= pygame.image.load('players_icons/car.gif')

players_buy_icons[2]=pygame.image.load('players_icons/dog - own.gif')
players_mortage_icons[2]=pygame.image.load('players_icons/dog - mortage.gif')
players_move_icons[2]=pygame.image.load('players_icons/dog.gif')

players_buy_icons[3]=pygame.image.load('players_icons/ship - own.gif')
players_mortage_icons[3]=pygame.image.load('players_icons/ship - mortage.gif')
players_move_icons[3]=pygame.image.load('players_icons/ship.gif')

players_buy_icons[0]=pygame.image.load('players_icons/hat - own.gif')
players_mortage_icons[0]=pygame.image.load('players_icons/hat - mortage.gif')
players_move_icons[0]=pygame.image.load('players_icons/hat.gif')
"""
from buttons import *

FPS = 15  # frames per second setting
go_player_picturex = 497
go_player_picturey = 501

WHITE = (255, 255, 255)
start_trip = 500
end_trip = 50
step_trip = 46
magic_trip = 20  # bez popravkata ne e krasivo :)


def main():
    game = Game()
    game.register_player('goshko')
    game.register_player('kirakis')
    FPS = 15
    picx = go_player_picturex
    picy = go_player_picturey
    global DISPLAYSURF, fpsClock
    pygame.init()
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((760, 580), 0, 32)
    #windowSurface = pygame.display.set_mode((500, 400),0,32)
    pygame.display.set_caption('Monopoly Standard Edition')
    background = pygame.image.load('pictures/resized.bmp')
    DISPLAYSURF.blit(background, (0, 0))
    pygame.display.update()
    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 600
    y_position = 0
    text_lenght = 150
    x_text_border = 30
    y_text_border = 40

    roll_button = Button()
    roll_button.create_button(DISPLAYSURF, bg_color, x_position, y_position,
                              text_lenght, x_text_border, y_text_border, 'Roll', text_color)
    #                       range(start, end)   step
    y_position = (i for i in range(10, 550) if i % 45 == 0)

    end_turn = Button()
    end_turn.create_button(DISPLAYSURF, bg_color, x_position, next(
        y_position), text_lenght, x_text_border, y_text_border, 'end_turn', text_color)
    mourtage = Button()
    mourtage.create_button(DISPLAYSURF, bg_color, x_position, next(
        y_position), text_lenght, x_text_border, y_text_border, 'mourtage', text_color)
    unmourtage = Button()
    unmourtage.create_button(DISPLAYSURF, bg_color, x_position, next(
        y_position), text_lenght, x_text_border, y_text_border, 'unmourtage', text_color)
    trade = Button()
    trade.create_button(DISPLAYSURF, bg_color, x_position, next(y_position),
                        text_lenght, x_text_border, y_text_border, 'trade', text_color)
    sell = Button()
    sell.create_button(DISPLAYSURF, bg_color, x_position, next(y_position),
                       text_lenght, x_text_border, y_text_border, 'sell', text_color)
    build = Button()
    build.create_button(DISPLAYSURF, bg_color, x_position, next(y_position),
                        text_lenght, x_text_border, y_text_border, 'build', text_color)
    rules = Button()
    rules.create_button(DISPLAYSURF, bg_color, x_position, next(
        y_position), text_lenght, x_text_border, y_text_border, 'rules', text_color)
    register = Button()
    register.create_button(DISPLAYSURF, bg_color, x_position, next(
        y_position), text_lenght, x_text_border, y_text_border, 'register', text_color)
    bancrupt = Button()
    bancrupt.create_button(DISPLAYSURF, bg_color, x_position, next(
        y_position), text_lenght, x_text_border, y_text_border, 'bancrupt', text_color)
    # pygame.image.save(pygame.display.get_surface(),'C:/Python33/pictures/resized.bmp')
    pygame.display.update()

    mousex = 0
    mousey = 0
    #move_icon(0, 30,0,DISPLAYSURF)
    # move_icon(0,5,0,DISPLAYSURF)
    while True:
        for event in pygame.event.get():

            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                display_current_player(
                    DISPLAYSURF, game, (600, 500), (600, 530))
                mousex, mousey = event.pos

                if game.has_winner():
                    winner(DISPLAYSURF, game)  # ne znam kak da zavurshi

                if roll_button.pressed([mousex, mousey]):
                    roll_dices(game, DISPLAYSURF)
                    game.take_fee()
                    print('izleze ot roll ')
                    display_centre(DISPLAYSURF)
                    players_render(DISPLAYSURF, game)
                    f(game)

                if end_turn.pressed([mousex, mousey]):
                    end_turner(DISPLAYSURF)
                    display_centre(DISPLAYSURF)
                    game.end_turn()
                    players_render(DISPLAYSURF, game)
                    f(game)
                    print('end_turn pressed')

                if mourtage.pressed([mousex, mousey]):
                    print('mourtage pressed')
                    mourtager(game, DISPLAYSURF)
                    display_centre(DISPLAYSURF)
                    players_render(DISPLAYSURF, game)
                    f(game)

                if unmourtage.pressed([mousex, mousey]):
                    print('unmourtage pressed')
                    unmourtager(game, DISPLAYSURF)
                    display_centre(DISPLAYSURF)
                    players_render(DISPLAYSURF, game)
                    f(game)

                if trade.pressed([mousex, mousey]):
                    print('trade pressed')
                    trader(game, 'kirakis', DISPLAYSURF)
                    display_centre(DISPLAYSURF)
                    players_render(DISPLAYSURF, game)
                    f(game)

                if sell.pressed([mousex, mousey]):
                    print('sell pressed')
                    sell_houser(game, "player_name", DISPLAYSURF)
                    display_centre(DISPLAYSURF)
                    players_render(DISPLAYSURF, game)
                    f(game)

                if build.pressed([mousex, mousey]):
                    print('build pressed')
                    build_houser(game, "player_name", DISPLAYSURF)
                    display_centre(DISPLAYSURF)
                    players_render(DISPLAYSURF, game)
                    f(game)

                if rules.pressed([mousex, mousey]):
                    print('rules pressed')

                    display_centre(DISPLAYSURF)
                    players_render(DISPLAYSURF, game)
                    f(game)

                if register.pressed([mousex, mousey]):  # works but buggy
                    print('register pressed', register.stat)
                    register_player(game, DISPLAYSURF)
                    pygame.display.update()
                    display_centre(DISPLAYSURF)
                    players_render(DISPLAYSURF, game)
                    f(game)
                    print(game.all_player())

                    # da dobavq centralna kartinka

                if bancrupt.pressed([mousex, mousey]):  # works but buggy
                    print('bancrupt pressed', register.stat)
                    game.bancrupt()
                    players_render(DISPLAYSURF, game)
                    f(game)
                    # self.other(DISPLAYSURF,game)
                    # display_centre(DISPLAYSURF)
                    # register_player()
                    # register.status(False)
                pygame.display.update()
                mouseClicked = True

        pygame.display.update()


main()


"""
                    roll logic !!!!
                    action = game.roll_dice#(game, game.current_player_index(),DISPLAYSURF)
                    position = game.current_position()
                    player_id = game.current_player_index()
                    if len(action) == 1:
                        result = Jail(game,DISPLAYSURF,action[0])
                        if len(reuslt) == 2:
                            Buyer(game, position,DISPLAYSURF)
                            print('free from jail + pay 50')
                    elif len(action) == 2 :                        
                        move_icon(position,position + action[0],player_id,MOVE,DISPLAYSURF )
                    elif len(action)  == 3:
                        rezult = Buyer(game, player_id, DISPLAYSURF)
                        if rezult == 'buy' :
                            buy_or_mortage_property(player_id, position ,BUY,DISPLAYSURF)
                        else :
                            auctioner(game, position,DISPLAYSURF)
                    elif len(action) == 4:
                        game.end_turn()  """
"""print('rolled pressed')    
                    if not game.player_Free() :
                        a = jail()
                        if a == 'free':
                            game.jail_decision(50)
                        else:
                            break #svoboden
                    roll = roll_dices(game,DISPLAYSURF) #hvyrlq zarove
                    if len(roll)<2: 
                        display_centre(DISPLAYSURF)
                        break
                    #move_icon(roll[0], roll[1],game.current_player_index(),,DISPLAYSURF)#mesti igracha
                    fee_result = game.take_fee()
                    display_centre(DISPLAYSURF)
                    if fee_result == 'buy':
                        result = Buyer(game,roll[1],DISPLAYSURF)
                        display_centre(DISPLAYSURF)
                        if result =='buy':
                            #picx,picy = move_icon(roll[0], roll[1],game.current_player_index(),DISPLAYSURF)
                            buy_or_mortage_property(game.current_player_index(), roll[1],BUY,DISPLAYSURF)
                    else:
                        print('ogromen problem!!!!!! acution e cuknat') 
                        #auctioner()
                        display_centre(DISPLAYSURF)                        
                    print('render')"""

        #pionkax = 30
        #pionkay = 20
        #player_name = 'goshko'
        #player_budget = 400
         # player name coord (20,558) and budget(400,558)
        # display_current_player(DISPLAYSURF,'goshko',500,(20,558),(400,558))
        #blank_names(DISPLAYSURF, 1,(0,558))
        # display_current_player(DISPLAYSURF,'gosaddsashko',5200,(20,558),(400,558))
