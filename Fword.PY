import pygame
from pygame.locals import *

FPS = 30 # frames per second to update the screen
WINWIDTH = 800 # width of the program's window, in pixels
WINHEIGHT = 600 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

# The total width and height of each tile in pixels.
TILEWIDTH = 50
TILEHEIGHT = 20
TILEFLOORHEIGHT = 20

done = False    
player.pos = Rect(0,0,10,10)

BRIGHTBLUE = (  0, 170, 255)
WHITE      = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage

   pygame.init()
   FPSCLOCK = pygame.time.Clock()
   
   DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('FWORD')
      BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
      
      # Change names
          IMAGESDICT = {'uncovered goal': pygame.image.load('RedSelector.png'),
                  'covered goal': pygame.image.load('Selector.png'),
                  'star': pygame.image.load('Star.png'),
                  'corner': pygame.image.load('Wall_Block_Tall.png'),
                  'wall': pygame.image.load('Wood_Block_Tall.png'),

          TILEMAPPING = {'x': IMAGESDICT['corner'],
                   '#': IMAGESDICT['wall'],
                   'o': IMAGESDICT['inside floor'],
                   ' ': IMAGESDICT['outside floor']}
                          
                              currentImage = 0
    PLAYERIMAGES = [IMAGESDICT['princess'],
                    IMAGESDICT['boy'],
                    IMAGESDICT['catgirl'],
                    IMAGESDICT['horngirl'],
                    IMAGESDICT['pinkgirl']]
                    
                                    elif event.key == K_p:
                    # Change the player image to the next one.
                    currentImage += 1
                    if currentImage >= len(PLAYERIMAGES):
                        # After the last player image, use the first one.
                        currentImage = 0
                    mapNeedsRedraw = True
                    
                          DISPLAYSURF.fill(BGCOLOR)
                          map Needs Redraw = True
                        
                        
                          
while not done:
    for event in pygame.event.get():
        # any other key event input
        if event.type == QUIT:
            done = True        
        elif event.type == KEYDOWN:
            if event.key == K_ESC:
                done = True

    # get key current state
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player.pos.left -= 10
    if keys[K_RIGHT]:
        player.pos.left += 10
    if keys[K_UP]:
        player.pos.top -= 10
    if keys[K_DOWN]:
        player.pos.left += 10
    if keys[K_Z]: 
        print 'punch'
        if keys[K_X]: 
        print 'kick'
        if keys[K_C]: 
        print 'spec'
        
        
def terminate():
    pygame.quit()
    sys.exit()
