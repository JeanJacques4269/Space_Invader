import platform
from colors import *
import pygame.math
from screeninfo import get_monitors

# Start of default code
# Get monitor size and find the set WIDTH and HEIGHT for your game
if platform.system() == "Windows":
    main = get_monitors()[0]  # Get screens size
    for m in get_monitors()[1:]:
        if m.width > main.width:
            main = m
    WIDTH, _ = main.width, main.height
else:
    WIDTH, _ = 1920, 1080
ratio = 3 / 4  # corresponds to the place I want my window to take. For example, 1 will be fullscreen.
WIDTH, HEIGHT = int(WIDTH * ratio), int(WIDTH * ratio * 9 / 16)
# End of default code

vec = pygame.math.Vector2

# sprites
blocksize = HEIGHT // 8  # arbitrary size that depends on the screen size

x, y = pygame.image.load("assets/s.png").get_size()
img_spaceship = pygame.transform.smoothscale(pygame.image.load("assets/s.png"), (blocksize, int(blocksize * y / x)))
size_spaceship = img_spaceship.get_size()

x, y = pygame.image.load("assets/enemy.png").get_size()
img_ennemy = pygame.transform.smoothscale(pygame.image.load("assets/enemy.png"), (blocksize, int(blocksize * y / x)))

x, y = pygame.image.load("assets/bullet.png").get_size()
img_missile = pygame.transform.smoothscale(pygame.image.load("assets/bullet.png"),
                                           (int(x / y * int(size_spaceship[0] / 2)), int(size_spaceship[0] / 2)))
# game
FPS = 60
