# encoding=utf-8

# pygameHelloWorld.py

# 17. Graphics and Animation
# - Invent Your Own Computer Games with Python 3e, IAl Sweigart
#   - http://inventwithpython.com/chapter17.html
#   - http://inventwithpython.com/pygameHelloWorld.py
#   - http://inventwithpython.com/animation.py

# Topics Covered In This Chapter:
# ·        Installing Pygame
# ·        Colors and Fonts in Pygame
# ·        Aliased and Anti-Aliased Graphics
# ·        Attributes
# ·        The pygame.font.Font, pygame.Surface, pygame.Rect, and pygame.PixelArray Data Types
# ·        Constructor Functions
# ·        Pygame’s Drawing Functions
# ·        The blit() Method for Surface Objects
# ·        Events
# ·        Animation


import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
    # Initialize a window or screen for display
    # - set_mode(resolution=(0,0), flags=0, depth=0) -> Surface
pygame.display.set_caption('Hello world!')
    # Set the current window caption
    # - set_caption(title, icontitle=None) -> None

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up fonts
basicFont = pygame.font.SysFont(None, 48)
    # create a Font from the system fonts
    # - SysFont(name, size, bold=False, italic=False) -> Font

# set up the text
text = basicFont.render('Hello world!', True, WHITE, BLUE)
    # draw text on a new Surface
    # - render(text, antialias, color, background=None) -> Surface
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# draw the white background onto the surface
windowSurface.fill(WHITE)

# draw a green polygon onto the surface
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
    # draw a shape with any number of sides
    # - polygon(Surface, color, pointlist, width=0) -> Rect

# draw some blue lines onto the surface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
    # draw a straight line segment
    # - line(Surface, color, start_pos, end_pos, width=1) -> Rect
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# draw a blue circle onto the surface
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)
    # draw a circle around a point
    # - circle(Surface, color, pos, radius, width=0) -> Rect

# draw a red ellipse onto the surface
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)
    # draw a round shape inside a rectangle
    # - ellipse(Surface, color, Rect, width=0) -> Rect

# draw the text's background rectangle onto the surface
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))
    # draw a rectangle shape
    # - rect(Surface, color, Rect, width=0) -> Rect

# get a pixel array of the surface
pixArray = pygame.PixelArray(windowSurface)
    # pygame object for direct pixel access of surfaces
    # - PixelArray(Surface) -> PixelArray
pixArray[480][380] = BLACK
del pixArray

# draw the text onto the surface
windowSurface.blit(text, textRect)
    # draw one image onto another
    # - blit(source, dest, area=None, special_flags = 0) -> Rect

# draw the window onto the screen
pygame.display.update()
    # Update portions of the screen for software displays
    # - update(rectangle=None) -> None
    # - update(rectangle_list) -> None

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()