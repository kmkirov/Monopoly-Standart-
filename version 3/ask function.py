
# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

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

def main():
  screen = pygame.display.set_mode((320,240))
  #game register
  az = ask(screen, "Name")
  print(az)
  print( " was entered")
  pygame.quit()
if __name__ == '__main__': main()











"""from PyQt4 import QtGui,QtCore
from aaa import MyWindow

from tkinter import *
def roll_once():
    root = Tk()
    root.title("ROLL DICE")
    Label(text="ROLL DICE ONCE").pack()
    def roll():
        return 1
    def button1():
        return roll()


    b = Button(root,text = 'zdsadasd', command = button1)
    b.pack()

    root.mainloop()

roll_once()


class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.myWidget=MyWindow()
        self.myWidget.vbox.setMargin(0)
        self.button = QtGui.QPushButton('&smeni nadpisa')
        mainBox = QtGui.QVBoxLayout()
        mainBox.addWidget(self.myWidget)
        mainBox.addWidget(self.button)
        self.setLayout(mainBox)
        self.connect(self.button, QtCore.SIGNAL('clicked()'),
                     self.on_clicked)

    def on_clicked(self):
        self.myWidget.label.setText('nov nadpis')
        self.button.setDisabled(True)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle('oo still neshto si')
    window.resize(300,100)
    window.show()
    sys.exit(app.exec_())
"""
