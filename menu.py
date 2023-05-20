import pygame
import pygame_menu
import sys
from game import Game
# def values in case of empty loads on some of the fields
x = 8
y = 8
probability = 0.15

pygame.init()
surface = pygame.display.set_mode((800, 600))


def start_the_game():
    mainmusic = pygame.mixer.Sound("game.ogg")
    mainmusic.set_volume(0.1)
    mainmusic.play()

    size = int(x), int(y)
    prob = float(probability)
    g = Game(size, prob)
    g.run()


def set_difficulty(value, difficulty):
    global probability
    if(difficulty==1):
        probability = 0.15
    if(difficulty==2):
        probability = 0.2
    if(difficulty==3):
        probability = 0.3

def boardsizex(value):
    global x
    x = value

def boardsizey(value):
    global y
    y = value

img = pygame_menu.baseimage.BaseImage("images/nfactorial.png")
img.scale(0.2,0.2)


menu = pygame_menu.Menu('Welcome to Minesweeper!', 800, 600,
                       theme=pygame_menu.themes.THEME_SOLARIZED)

menu.add.image(image_path=img.copy())
menu.add.text_input('Name :', default='Arman Suleimenov')
menu.add.text_input('Board  Size (x) : ', maxchar= 2, default=8, onchange=boardsizex)
menu.add.text_input('Board  Size (y) : ', maxchar= 2, default=8, onchange=boardsizey)
menu.add.selector('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)