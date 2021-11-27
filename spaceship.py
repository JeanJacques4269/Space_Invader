import pygame.sprite

from constants import *


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = img_spaceship  # sprite attribute
        self.rect = self.surface.get_rect()  # sprite attribute

        self.pos = vec(WIDTH // 2, HEIGHT)
        self.vel = vec(0, 0)
        self.speed = 10 * blocksize // FPS

        self.firing_state = "ready"
        self.fired_missiles = pygame.sprite.Group()

    def move(self, info):
        if info == "right" and self.pos.x < WIDTH - size_spaceship[0]:
            self.vel = (self.speed, 0)
        elif info == "left" and self.pos.x > 0:
            self.vel = (-self.speed, 0)
        elif info == "fire":
            if self.firing_state:
                self.fire()

    def fire(self):
        self.fired_missiles.add(Missile(self.pos.x + size_spaceship[0] // 2, self.pos.y))

    def update_pos(self):
        self.pos += self.vel
        self.vel = vec(0, 0)  # You can try the program without that line to see what it does
        self.rect.bottomleft = self.pos


class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.surface = img_missile
        self.rect = self.surface.get_rect()

        self.speed = 8
        self.pos = vec(x, y - size_spaceship[0])
        self.vel = (0, self.speed)

    def update_pos(self):
        self.pos -= self.vel
        self.rect.midbottom = self.pos
