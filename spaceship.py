from constants import *


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = img_spaceship  # sprite attribute
        self.rect = self.surface.get_rect()  # sprite attribute

        self.pos = vec(0, HEIGHT)
        self.vel = vec(0, 0)
        self.speed = 10 * blocksize // FPS

    def move(self, info):
        if info == "right":
            self.vel = (self.speed, 0)
        elif info == "left":
            self.vel = (-self.speed, 0)

    def update_pos(self):
        self.pos += self.vel
        self.vel = vec(0, 0)  # You can try the program without that line
        self.rect.midbottom = self.pos
