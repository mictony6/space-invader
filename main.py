from pygame.event import event_name
from player import Player, Enemy, Bullet
import random
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# game title and icon

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


isRunning = True


# player and enemy instances
player = Player("player.png", screen)
enemy = Enemy("enemy.png", screen)

# declaring a list for the bullets
shots = []
count = 0

# loading the background image
bg = pygame.image.load("background.png").convert()


# game loop
while isRunning:
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        # detecting movement input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.changeY = -.5
            if event.key == pygame.K_s:
                player.changeY = .5
            if event.key == pygame.K_a:
                player.changeX = -.5
            if event.key == pygame.K_d:
                player.changeX = .5
            if event.key == pygame.K_SPACE:
                # have multiple bullet instances using a list

                if count == 0:
                    shots.append(
                        Bullet(player.x, player.y, "bullet.png", screen))
                    shots[count].state = True
                    shots[count].x = player.x
                    shots[count].y = player.y
                    count += 1

                # if the last bullet is still firing, create a new instance instead
                elif shots[count-1].state:
                    shots.append(
                        Bullet(player.x, player.y, "bullet.png", screen))
                    shots[count].state = True
                    count += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                player.changeX = player.changeY = 0

    player.move()
    enemy.move()

    for bullet in shots:

        if bullet.state:
            bullet.move()
            bullet.drawBullet(bullet.x, bullet.y)
        if bullet.isColliding(enemy):
            bullet.state = False
            enemy.respawn()
            player.score += 1
            print("SCORE:", player.score)
        if bullet.y <= 0 or bullet.state == False:
            shots.pop(shots.index(bullet))
            count -= 1

    if enemy.isOut():
        enemy = Enemy("enemy.png", screen)

    enemy.clamp()
    player.clamp()

    player.drawPlayer()
    enemy.drawEnemy()

    pygame.display.update()
