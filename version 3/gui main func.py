import pygame, sys
from pygame.locals import *
from tkinter import *
import threading
from game import Game
main_game = Game()
from tkinter import *

JAIL =10
eq_counter = 0

def buy_property():

    root = Tk()
    root.title("BUY BUILDING")
    def building():
        return 'garata br'
    text1="BUY BUILDING:" + 'building' + '\n' "price" +str(25)
    a=Label(text=text1).pack()
    def Buy():
        return 1
        root.destroy()
    def Auction():
        root.destroy()
        return 2
    b = Button(root, text="Buy", command=Buy)
    b.pack()
    a= Button(root, text="Auction", command=Auction)
    a.pack()
    root.mainloop()





        


def end_turner():
    eq_counter = 0 # broqch za chiftove
    main_game.next_player_turn() # sledvashtiq igrach e na hod
    register.status(True)
    
def roll_once():
    root = Tk()
    root.title("ROLL DICE")
    player_index = main_game.get_current_playing_index()
    dice = main_game.roll_dice()
    player_name = main_game.get_playername_by_index(player_index)
    Label(text="ROLL DICE ONCE " + dice[0] ).pack()
    old_position = main_game.player_position(player_name)
    new_position = 0
    if dice[1] == True:
        eq_counter = eq_counter + 1
        if  eq_counter == 3 :
            main_game.new_position(JAIL)
            new_position = JAIL
            move_icon(old_position,JAIL, icon)#animation
            root.distroy()#krai        
             
    else :
       main_game.move_player_by_rolled(dice[0],player_name)
       new_position=main_game.player_position(player_name)
       move_icon(old_position,new_position, icon)#animation
       check_position = main_game.check_position(self, new_position, player_name)
       if check_position == 'O':
           pass
       elif check_position == 'R': pass
       elif check_position == 'B': pass 
       elif check_position == 'cc' or check_position == 'c': pass
       elif check_position == 'P' : pass
    
    if not dice[1] : # zabranqva zarcheto ako ne e chift :) 
        register.status(False)    
    root.mainloop()
    root.distroy()
    #b = Button(root,text = 'zdsadasd') ne raboti !!! ?
     #b.pack()
    #def roll():
     #   return 1
    #def button1():
    #    return roll()
# ------------------------ ======== roll dice ====== -------------- 
DICT_NAME_PICTURE={'player1':1,'Player2':2}
LIST_PICS=['kartinka 1', 'kartinka2']

#-----======== important function for animation
def saver():
    pygame.image.save(DISPLAYSURF,'C:/Python33/pictures/resized.bmp')        

def find_position_x_y(position):
    picx = go_player_picturex
    picy = go_player_picturey
    for a in range(position):
        if picx > end_trip and picy >start_trip:
            
            picx = picx - step_trip
            picy = picy 
            
            
        elif picx <end_trip and picy >end_trip:
              
            picx = picx 
            picy = picy - step_trip
            
        elif picx < start_trip - magic_trip and picy <end_trip:
            picx = picx + step_trip
            picy = picy
        else :
            picx = picx 
            picy = picy + step_trip
    return (picx,picy)


def move_icon(old_poss, new_pos,catImg1):   
    picx,picy = find_position_x_y(old_poss)
    mousex = 0
    mousey= 0
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((760, 555), 0, 32)
    for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
    for a in range(new_pos):
        if picx > end_trip and picy >start_trip:
            
            picx = picx - step_trip
            picy = picy 
            
            
        elif picx <end_trip and picy >end_trip:
              
            picx = picx 
            picy = picy - step_trip
            
        elif picx < start_trip - magic_trip and picy <end_trip:
            picx = picx + step_trip
            picy = picy
        else :
            picx = picx 
            picy = picy + step_trip
            
        DISPLAYSURF.blit(catImg1,(0, 0))
        DISPLAYSURF.blit(catImg, (picx,picy))
        fpsClock.tick(FPS)
        pygame.display.update()
        #pygame.save(get_surface(),'C:/Python33/pictures/resized.bmp')
        fpsClock.tick(FPS)



#-------========









from buttons import *

FPS = 15 # frames per second setting
go_player_picturex = 497
go_player_picturey = 501

WHITE = (255, 255, 255)
start_trip = 500
end_trip = 50
step_trip = 46
magic_trip = 20 #bez popravkata ne e krasivo :)

from multiprocessing import Process, Value

def f():
    FPS = 15
    picx = go_player_picturex
    picy = go_player_picturey
    global DISPLAYSURF, fpsClock
    pygame.init()
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((760, 555), 0, 32)
    #windowSurface = pygame.display.set_mode((500, 400),0,32)
    pygame.display.set_caption('Hello ddddddddd world!')
    catImg1 = pygame.image.load('pictures/resized.bmp')
    catImg = pygame.image.load('pictures/dog.gif')
    #end of main pictures
    DISPLAYSURF.blit(catImg1,(0, 0))
    DISPLAYSURF.blit(catImg, (picx,picy))
    
    # buttons on the screen 

    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 600
    y_position = 100
    text_lenght = 150
    x_text_border = 30
    y_text_border =40   

    roll_button = Button()
    roll_button.create_button(DISPLAYSURF,bg_color, x_position ,y_position,text_lenght,x_text_border,y_text_border,'Roll',text_color)
    #                       range(start, end)   step
    y_position =(i for i in range(150,500) if i % 40 == 0)
    
    end_turn = Button()
    end_turn.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'end_turn',text_color)
    
processes = Process(target=f, )


 

# monopoly picture with players
def main():
    FPS = 15
    picx = go_player_picturex
    picy = go_player_picturey
    global DISPLAYSURF, fpsClock
    pygame.init()
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((760, 555), 0, 32)
    #windowSurface = pygame.display.set_mode((500, 400),0,32)
    pygame.display.set_caption('Hello ddddddddd world!')
    catImg1 = pygame.image.load('pictures/resized.bmp')
    catImg = pygame.image.load('pictures/dog.gif')
    #end of main pictures
    DISPLAYSURF.blit(catImg1,(0, 0))
    DISPLAYSURF.blit(catImg, (picx,picy))
    
    # buttons on the screen 

    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 600
    y_position = 100
    text_lenght = 150
    x_text_border = 30
    y_text_border =40   

    roll_button = Button()
    roll_button.create_button(DISPLAYSURF,bg_color, x_position ,y_position,text_lenght,x_text_border,y_text_border,'Roll',text_color)
    #                       range(start, end)   step
    y_position =(i for i in range(150,500) if i % 40 == 0)
    
    end_turn = Button()
    end_turn.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'end_turn',text_color)
    mourtage = Button()
    mourtage.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'mourtage',text_color)
    unmourtage = Button()
    unmourtage.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'unmourtage',text_color)
    trade = Button()
    trade.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'trade',text_color)
    sell = Button()
    sell.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'sell',text_color)
    build = Button()
    build.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'build',text_color)
    rules = Button()
    rules.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'rules',text_color)
    register= Button()
    register.create_button(DISPLAYSURF,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'register',text_color)
    
    #end of buttons
    
    pygame.display.update()
    while True:
        
        mousex = 0
        mousey= 0
        #pionkax = 30
        #pionkay = 20
        
        for event in pygame.event.get(): # event handling loop
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mousex, mousey = event.pos
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if roll_button.pressed([mousex,mousey]):
                        print('rolled pressed',roll_button.stat)
                        roll_once()
                        
                    if end_turn.pressed([mousex,mousey]):
                        print('end_turn pressed',end_turn.stat)
                    if mourtage.pressed([mousex,mousey]):
                        print('mourtage pressed')
                    if unmourtage.pressed([mousex,mousey]):
                        print('unmourtage pressed')
                    if trade.pressed([mousex,mousey]):
                        print('trade pressed')
                    if sell.pressed([mousex,mousey]):
                        print('sell pressed')
                        processes.start()
                    if build.pressed([mousex,mousey]):
                        print('build pressed')
                        buy_property()
                    if rules.pressed([mousex,mousey]):
                        print('rules pressed')
                        
                    if register.pressed([mousex,mousey]):#works but buggy
                        print('register pressed',register.stat)
                        register_player()
                        register.status(False)
                        
                    mouseClicked = True
        pygame.display.update()
        
main()



