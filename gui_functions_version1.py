from game import Game
from multiprocessing import Process, Value
import time
from buttons import *

#ot internet!!!
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + ''.join(current_string))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
      a =str(question) + ": " + ''.join(current_string)
    display_box(screen,a )
  return ''.join(current_string)

"""
def main():
  screen = pygame.display.set_mode((320,240))
  #game register
  az = ask(screen, "Name")
  print(az)
  print( " was entered")
  pygame.quit()
if __name__ == '__main__': main()

"""
















game = Game()
a = []


 # frames per second setting
go_player_picturex = 497
go_player_picturey = 501

WHITE = (255, 255, 255)
start_trip = 500
end_trip = 50
step_trip = 46
magic_trip = 20 #bez popravkata ne e krasivo :)
"""
pygame.font.init()
    font = pygame.font.Font( pygame.font.get_default_font(), 12 )
    text = font.render( string, False, color )
    text.blit( text, picture, ( x, y ) )
    pygame.font.quit()
"""
#------------- register player just view ----------
def register_player(game):
    pygame.init()
    window = pygame.display.set_mode((400, 200), 0, 32)
    
    pygame.display.set_caption('Registration')
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,(0, 0))

    font = pygame.font.Font(None, 30)
    textImg = font.render( "   Register player (type and pres enter)", 1, (255,0,0))
    window.blit( textImg, (0,0) )# za da e nai otgore

    pygame.display.update()
    pygame.font.quit()

    kom = ask(window,'name')#vyvejdaneto
    print(kom)
    pygame.quit()

#register_player(game)
#----------------=== end register player =======-----------

# --------==== mourtage house =======----------

def trade(game):
    pygame.init()
    window = pygame.display.set_mode((400, 200), 0, 32)
    
    pygame.display.set_caption('Registration')
    background = pygame.image.load('pictures/bG.jpg')
    window.blit(background,(0, 0))

    font = pygame.font.Font(None, 30)
    textImg = font.render( "   Register player (type and pres enter)", 1, (255,0,0))
    window.blit( textImg, (0,0) )# za da e nai otgore

    pygame.display.update()
    pygame.font.quit()
    #smenqt se posledovatelno :)
    kom = ask(window,'list of oferer')#vyvejdaneto
    kom1 = ask(window,'list of oferer1')#vyvejdaneto
    kom2 = ask(window,'list of oferer2')#vyvejdaneto
    kom3 = ask(window,'list of oferer3')#vyvejdaneto
    print(kom,kom1,kom2,kom3)
    pygame.quit()
trade(game)






















def d(a):
    pygame.init()
    a.append(1)
    

    #text
    
    catImg1 = pygame.image.load('pictures/bG.jpg')
    
    print(5)
    FPS = 15
    picx = go_player_picturex
    picy = go_player_picturey
       
    
    #pygame.init()
    
    pp = pygame.display.set_mode((400, 200), 0, 32)
    
    font = pygame.font.Font(None, 30)
    textImg = font.render( "   Register player (type and pres enter)", 1, (255,0,0))
    
    #windowSurface = pygame.display.set_mode((500, 400),0,32)
    pygame.display.set_caption('ACTION')
    catImg1 = pygame.image.load('pictures/bG.jpg')
    #catImg = pygame.image.load('pictures/dog.gif')
    #end of main pictures
    pp.blit(catImg1,(0, 0))
    #pp.blit(catImg, (picx,picy))
    
    # buttons on the screen 

    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 0
    y_position = 0
    text_lenght = 150
    x_text_border = 30
    y_text_border =40
    
    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 40
    y_position = 100
    text_lenght = 150
    x_text_border = 30
    y_text_border =40   
    y_position =(i for i in range(1,500) if i % 40 == 0)
    
    rules = Button()
    rules.create_button(pp,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'Buy',text_color)
    register= Button()
    register.create_button(pp,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'Auction',text_color)
    pp.blit( textImg, (0,0) )# za da e nai otgore
    pygame.display.update()
    time.sleep(2)
    pygame.font.quit()
    mousex = 0
    mousey= 0
    kom = ask(pp,'name')
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if rules.pressed([mousex,mousey]):
                print('d')
            
            if register.pressed([mousex,mousey]):
                print('d4')
    pygame.quit()

#--------- original
def d(a):
    pygame.init()
    a.append(1)
    

    #text
    
    catImg1 = pygame.image.load('pictures/bG.jpg')
    
    print(5)
    FPS = 15
    picx = go_player_picturex
    picy = go_player_picturey
       
    
    #pygame.init()
    
    pp = pygame.display.set_mode((400, 200), 0, 32)
    
    font = pygame.font.Font(None, 30)
    textImg = font.render( "   Register player (type and pres enter)", 1, (255,0,0))
    
    #windowSurface = pygame.display.set_mode((500, 400),0,32)
    pygame.display.set_caption('ACTION')
    catImg1 = pygame.image.load('pictures/bG.jpg')
    #catImg = pygame.image.load('pictures/dog.gif')
    #end of main pictures
    pp.blit(catImg1,(0, 0))
    #pp.blit(catImg, (picx,picy))
    
    # buttons on the screen 

    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 0
    y_position = 0
    text_lenght = 150
    x_text_border = 30
    y_text_border =40
    
    bg_color = (255, 255, 255)
    text_color = (255,   0,   0)
    #windowBgColor = WHITE
    x_position = 40
    y_position = 100
    text_lenght = 150
    x_text_border = 30
    y_text_border =40   
    y_position =(i for i in range(1,500) if i % 40 == 0)
    
    rules = Button()
    rules.create_button(pp,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'Buy',text_color)
    register= Button()
    register.create_button(pp,bg_color, x_position ,next(y_position),text_lenght,x_text_border,y_text_border,'Auction',text_color)
    pp.blit( textImg, (0,0) )# za da e nai otgore
    pygame.display.update()
    time.sleep(2)
    pygame.font.quit()
    mousex = 0
    mousey= 0
    kom = ask(pp,'name')
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if rules.pressed([mousex,mousey]):
                print('d')
            
            if register.pressed([mousex,mousey]):
                print('d4')
    pygame.quit()





























#text oprosten
"""

pygame.init()
window = pygame.display.set_mode( (424,440) )#suzdava prozorec
pygame.display.set_caption( 'Example Game' )#zaglavie
font = pygame.font.Font(None, 30)
textImg = font.render( "Press SPACE BAR to start", 1, (255,0,0))
window.blit( textImg, (0,0) )

pygame.display.update()

"""


"""
pygame.init()
window = pygame.display.set_mode( (424,440) )
pygame.display.set_caption( 'Example Game' )
background = pygame.Surface( window.get_size() )
background.fill( (0,0,0) )
font = pygame.font.Font(None, 30)
textImg = font.render( "Press SPACE BAR to start", 1, (255,0,0))
background.blit( textImg, (0,0) )
window.blit( background, (0,0) )
pygame.display.flip()
backSprites = pygame.sprite.RenderUpdates()
frontSprites = pygame.sprite.RenderUpdates()
time.sleep(2)  
pygame.quit()"""
