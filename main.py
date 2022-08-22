import random
import pygame
import sys

pygame.init()

SIZE = WIDTH, HEIGHT = 640, 460
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Asteroid Dodge Game")

CLOCK = pygame.time.Clock()
PLAYERSPEED = 2
ENEMYSPEED = 1
BLACK = (0, 0, 0)

PLAYER = pygame.image.load("images/square.png")
PLAYERRECT = PLAYER.get_rect(center=(WIDTH/2, HEIGHT/2))

ENEMY = pygame.image.load("images/enemy.png")
ENEMYRECT = ENEMY.get_rect()


class Player():
    def __init__(self, PLAYERRECT, PLAYERSPEED):
        self.rect = PLAYERRECT
        self.speed = PLAYERSPEED

    def movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.rect.move_ip(0, -self.speed)
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.rect.move_ip(0, +self.speed)
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.move_ip(-self.speed, 0)
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.move_ip(+self.speed, 0)


class Enemy():
    def __init__(self):
        ENEMY = pygame.image.load("images/enemy.png")
        # ENEMYRECT = ENEMY.get_rect()
        self.count = []

    def spawn(self):
        for i in range(5):
            i = ENEMY
            pos_x = random.randint(0, WIDTH)
            rect = i.get_rect(center=(pos_x, -HEIGHT))
            SCREEN.blit(i, rect)

            # ENEMYRECT.move_ip(0, self.speed)


def drawGame():
    p = Player(PLAYERRECT, PLAYERSPEED)
    e = Enemy()

    while True:
        CLOCK.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        p.movement()

        SCREEN.fill(BLACK)
        SCREEN.blit(PLAYER, PLAYERRECT)
        e.spawn()
        # SCREEN.blit(ENEMY, ENEMYRECT)
        pygame.display.update()


drawGame()
