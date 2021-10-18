from pygame.event import event_name
from player import Player, Enemy, Bullet
from system import System
import random
import pygame
import pygame.freetype
pygame.init()
font = pygame.freetype.Font('segoe.ttf', 30)

screen = pygame.display.set_mode((800, 600))
system = System(800, 600)
# game title and icon

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)


isRunning = True


# player and enemy instances
player = Player("images/player.png", screen)
ships = []
for i in range(5):
    ships.append(Player("images/icon.png", screen))
for ship in ships:
    ship.x = random.randint(0, 600)
    ship.y = random.randint(-50, 0)
    ship.changeY = .5/random.randint(1, 10)
# enemy = Enemy("enemy.png", screen)

# declaring a list for the bullets
shots = []
count = 0
enemies = []
enemy_count = 5
for i in range(enemy_count):
    enemies.append(Enemy("images/enemy.png", screen))


# loading the background image
bg = pygame.image.load("images/background.png").convert()


# game loop
while isRunning:
    display_score, rect = font.render(
        f'Score: {system.score}', (255, 255, 200))

    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    system.blit(display_score, (675, 10))
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
                        Bullet(player.x, player.y, "images/bullet.png", screen))
                    shots[count].state = True
                    shots[count].x = player.x
                    shots[count].y = player.y
                    count += 1

                # if the last bullet is still firing, create a new instance instead
                elif shots[count-1].state:
                    shots.append(
                        Bullet(player.x, player.y, "images/bullet.png", screen))
                    shots[count].state = True
                    count += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                player.changeX = player.changeY = 0

    player.move()
    n = 0
    for enemy in enemies:
        enemy.move()
        if enemy.isOut():
            isRunning = False
        enemy.clamp()
        enemy.drawEnemy()
        n += 1
    n = 0
    for bullet in shots:

        if bullet.state:
            bullet.move()
            bullet.drawBullet(bullet.x, bullet.y)
        for enemy in enemies:
            if bullet.isColliding(enemy):
                bullet.state = False
                enemy.respawn()
                system.updateScore()
        if bullet.y <= 0 or bullet.state == False:
            shots.pop(n)
            count -= 1
            n += 1

    player.clamp()
    for ship in ships:
        ship.drawPlayer()
        ship.move()
        if ship.isColliding(player):
            isRunning = False
        if ship.y >= 600:
            ship.x = random.randint(0, 100)*6
            ship.y = 0
            ship.changeY = .5/random.randint(1, 10)
    player.drawPlayer()

    pygame.display.update()

score, rect = font.render(f'Score: {system.score}',  (0, 0, 0))

game_over, rect = font.render('Game Over!',  (0, 0, 0))
while system.isRunning():
    system.fill((255, 255, 255))
    system.blit(game_over, (320, 290))
    system.blit(score, (345, 325))
    system.getKey()
