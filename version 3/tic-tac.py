import pygame, sys,time
from pygame.locals import *
import threading
from game import Game
main_game = Game()
from tkinter import *
from buttons import *
from multiprocessing import Process, Value


def d(a):#GUI FUNCTIONS







"""
# Memory Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, pygame, sys
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
BOXSIZE = 40 # size of box height & width in pixels
GAPSIZE = 10 # size of gap between boxes in pixels
BOARDWIDTH = 10 # number of columns of icons
BOARDHEIGHT = 7 # number of rows of icons
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None # stores the (x, y) of the first box clicked.

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True: # main game loop
        mouseClicked = False

        DISPLAYSURF.fill(BGCOLOR) # drawing the window
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            #elif event.type == MOUSEMOTION:#bezmisleno osven ako ne e za ishoda
             #   mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            # The mouse is currently over a box.
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy) #markira samo !!! :) 
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True # set the box as "revealed"
                if firstSelection == None: # the current box was the first box clicked
                    firstSelection = (boxx, boxy)
                else: # the current box was the second box clicked
                    # Check if there is a match between the two icons.
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        # Icons don't match. Re-cover up both selections.
                        pygame.time.wait(1000) # 1000 milliseconds = 1 sec
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes): # check if all pairs found
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        # Reset the board
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        # Show the fully unrevealed board for a second.
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        # Replay the start game animation.
                        startGameAnimation(mainBoard)
                    firstSelection = None # reset firstSelection variable

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes


def getRandomizedBoard():
    # Get a list of every possible shape in every possible color.
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append( (shape, color) )

    random.shuffle(icons) # randomize the order of the icons list
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) # calculate how many icons are needed
    icons = icons[:numIconsUsed] * 2 # make two of each
    random.shuffle(icons)

    # Create the board data structure, with randomly placed icons.
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] # remove the icons as we assign them
        board.append(column)
    return board


def splitIntoGroupsOf(groupSize, theList):
    # splits a list into a list of lists, where the inner lists have at
    # most groupSize number of items.
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])
    return result


def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)


def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def drawIcon(shape, color, boxx, boxy):
    quarter = int(BOXSIZE * 0.25) # syntactic sugar
    half =    int(BOXSIZE * 0.5)  # syntactic sugar

    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords
    # Draw the shapes
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))


def getShapeAndColor(board, boxx, boxy):
    # shape value for x, y spot is stored in board[x][y][0]
    # color value for x, y spot is stored in board[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]


def drawBoxCovers(board, boxes, coverage):
    # Draws boxes being covered/revealed. "boxes" is a list
    # of two-item lists, which have the x & y spot of the box.
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0: # only draw the cover if there is an coverage
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))
    pygame.display.update()
    FPSCLOCK.tick(FPS)


def revealBoxesAnimation(board, boxesToReveal):
    # Do the "box reveal" animation.
    for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
        drawBoxCovers(board, boxesToReveal, coverage)


def coverBoxesAnimation(board, boxesToCover):
    # Do the "box cover" animation.
    for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
        drawBoxCovers(board, boxesToCover, coverage)


def drawBoard(board, revealed):
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                # Draw the (revealed) icon.
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)


def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)


def startGameAnimation(board):
    # Randomly reveal the boxes 8 at a time.
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append( (x, y) )
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)

    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup)
        coverBoxesAnimation(board, boxGroup)


def gameWonAnimation(board):
    # flash the background color when the player has won
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR

    for i in range(13):
        color1, color2 = color2, color1 # swap colors
        DISPLAYSURF.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)


def hasWon(revealedBoxes):
    # Returns True if all the boxes have been revealed, otherwise False
    for i in revealedBoxes:
        if False in i:
            return False # return False if any boxes are covered.
    return True


if __name__ == '__main__':
    main()
"""
"""   
    a.append(1)
    
    print(5)
    FPS = 15
    picx = go_player_picturex
    picy = go_player_picturey
    from buttons import Button   
    
    pygame.init()
    
    pp = pygame.display.set_mode((200, 200), 0, 32)
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
    pygame.display.update()
    time.sleep(2)
    mousex = 0
    mousey= 0
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
            print('d')
    pygame.quit()
    
def f(a):
    
    a.append(1)
    print(a)
    print(5)
    FPS = 15
    picx = go_player_picturex
    picy = go_player_picturey
    from buttons import Button   
    
    pygame.init()
    
    pp = pygame.display.set_mode((200, 200), 0, 32)
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
    pygame.display.update()
    time.sleep(2)
    mousex = 0
    mousey= 0
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
        if rules.pressed([mousex,mousey]):
            print('rolled pressed')
            processes = Process(target=d(a))
            processes.start()
            processes.join()
        if register.pressed([mousex,mousey]):
            print('end_turn pressed')
    print(a)
    pygame.quit()
    
    

def d(a):
    
    a.append(1)
    
    print(5)
    FPS = 15
    picx = go_player_picturex
    picy = go_player_picturey
    from buttons import Button   
    
    pygame.init()
    
    pp = pygame.display.set_mode((200, 200), 0, 32)
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
    pygame.display.update()
    time.sleep(2)
    mousex = 0
    mousey= 0
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
        if rules.pressed([mousex,mousey]):
            print('rolled pressed')
            
        if register.pressed([mousex,mousey]):
            print('end_turn pressed')
    pygame.quit()



FPS = 15 # frames per second setting
go_player_picturex = 497
go_player_picturey = 501

WHITE = (255, 255, 255)
start_trip = 500
end_trip = 50
step_trip = 46
magic_trip = 20 #bez popravkata ne e krasivo :)




 

# monopoly picture with players
def main():
    a = list()
    processes = Process(target=f(a), args = a)
    processes.start()
    processes.join()
    print(a)
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
    pygame.display.update()
    
    """    # buttons on the screen 

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
    """   
    
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






f([])
#main()

#
























"""from tkinter import *

root  = Tk()
root.title('Button App')
root.Label(text="Player Registration").pack(pady=2)
Label(text = 'I am a button').pack(pady = 150)

def quitapp():
    root.destroy()

Button(text='Quit',command = quitapp).pack(side=BOTTOM)
root.mainloop()
"""
"""
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value=float(feet.get())
        meters.set((0.3048 * value * 1000.0+0,5)/1000)
    except ValueError:
        pass
root = Tk()
root.title('Feet to Meters')
mainframe = ttk.frame(root, padding="3 3 12 12")
mainframe.grid(column=0,row=0,sticky=(N, W, E, S) )
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2,row =1, sticky=(W,E))

ttk.Label(mainframe, textvarable=meters).grid(column=2,row=2, sticky=(W,E))
ttk.Button(mainframe,text='Calculate',command = calculate).grid(column=3,row=3,side=BOTTOM)

ttk.label(mainframe, text='feet').grid(column=3,row=1, sticky=W)
ttk.Label(mainframe, text='is equivalent to').grid(column=1,row=1)
ttk.Label(mainframe, text="metters").grid(colimn=3,row=2)


for child in mainframe.winfo_children():child.grid_configuration()

feet_entry.focus()
root.bind('<Return>',calculate)
root.mainloop()
"""



"""
from tkinter import *

root = Tk()
root.title("Player Registration")
root.Label(text="Player Registration").pack()
text = Text()
text1 = Text()

text1.config(width=15, height=1)
text1.pack(pady = 20)

def button1():
    #print(text1)
    text.insert(END, text1.get("1.0",END))
    print(text1.get("1.0",END))

b = Button(root, text="Enter", width=10, height=2, command=button1)
b.pack()


text.config(width=20, height=6)
text.pack(side=LEFT, fill=Y)

"""

"""
from tkinter import *

root = Tk()
root.title("fn")

Label(text="Trade").pack()
text = Text(width=10, height=1)
text.pack(side=LEFT)
Label(text="money").pack(side=RIGHT)


def Bid():
    return 1
    root.destroy()
def Fold():
    
    root.destroy()
    return 2
    
var = IntVar()  
c = Checkbutton(root, text="Expand", variable=var)
c.pack()



a= Button(root, text="Fold", width=5, height=1, command=Fold)
a.pack()
b = Button(root, text="Bid", width=5, height=1, command=Bid)
b.pack()

"""






"""
from tkinter import *

root = Tk()
root.title("fn")

Label(text="Trade").pack()
text = Text(width=10, height=1)
text.pack(side=LEFT)
Label(text="money").pack(side=RIGHT)


def Bid():
    return 1
    root.destroy()
def Fold():
    
    root.destroy()
    return 2
    
var = IntVar()  
c = Checkbutton(root, text="Expand", variable=var)
c.pack()



a= Button(root, text="Fold", width=5, height=1, command=Fold)
a.pack()
b = Button(root, text="Bid", width=5, height=1, command=Bid)
b.pack()

from tkinter import *

root = Tk()
root.title("fn")

Label(text="Chest !:"+building() +'\n' "price" +str(25)).pack()



from tkinter import *

root = Tk()
root.title("Auctuon")
def building():
    return 'garata br'
Label(text="BUY BUILDING:"+building() +'\n' "price" +str(25)).pack()


def Bid():
    return 1
    root.destroy()
def Fold():
    
    root.destroy()
    return 2
    
    

b = Button(root, text="Bid", width=5, height=1, command=Bid)
b.pack(side=LEFT)
a= Button(root, text="Fold", width=5, height=1, command=Fold)
a.pack(side=RIGHT)


from tkinter import *

root = Tk()
root.title("BUY BUILDING")
def building():
    return 'garata br'
a=Label(text="BUY BUILDING:"+building() +'\n' "price" +str(25)).pack()


def Buy():
    return 1
    root.destroy()
def Auction():
    
    root.destroy()
    return 2
    
    

b = Button(root, text="Buy", width=5, height=1, command=Buy)
b.pack()
a= Button(root, text="Auction", width=5, height=1, command=Auction)
a.pack()






from tkinter import *

root = Tk()
root.title("Player Registration")
Label(text="Player Registration").pack()
text = Text()

def roll():
    return 1
def button1():
    
    text.insert(END, str(roll()))
    

b = Button(root, text="Roll", width=5, height=1, command=button1)
b.pack()


text.config(width=2, height=11)
text.pack(side=BOTTOM, fill=Y)




from tkinter import *
root  = Tk()
root.title('Player registration')
Label(text = 'Please enter player_name (6-14 symbols, check the name before submit)').pack(pady = 10)
text = Text()
feet = StringVar()
text.config(width=20, height=1)

text.pack()


def submita():
    #register player
    print(text.get("1.0",END))
    
def quitapp():
    b.config(state=DISABLED)
    #root.destroy()

b = Button(text='Submit',command = submita)
b.pack(side=RIGHT)

Button(text='Quit',command = quitapp).pack(side=LEFT)

root.mainloop()


"""





