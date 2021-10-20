from player import Player, Enemy, Bullet, Ship
from system import System
import random
import pygame.freetype
import pygame
clock = pygame.time.Clock()
pygame.init()
font = pygame.freetype.Font('segoe.ttf', 30)

screen = pygame.display.set_mode((800, 600))
system = System(800, 600)
# game title and icon

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

isRunning = True
elapsed = 0
seconds = 0.016
# player and enemy instances
player = Player("images/player.png", screen)
ships = []
for i in range(5):
    ships.append(Ship("images/icon.png", screen))
for ship in ships:
    ship.x = random.randint(1, 10)*60
    ship.y = random.randint(-50, 0)
    ship.changeY = random.randint(1, 10)*30
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


def game_over_screen():
    system.fill((255, 255, 255))
    system.blit(game_over, (320, 290))
    system.blit(score, (345, 325))


# game loop
while system.running:
    display_score, rect = font.render(
        f'Score: {system.score}', (255, 255, 200))

    system.fill((255, 255, 255))
    system.blit(bg, (0, 0))
    system.blit(display_score, (675, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            system.running = False
        # detecting movement input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.changeY = -300
            if event.key == pygame.K_s:
                player.changeY = 300
            if event.key == pygame.K_a:
                player.changeX = -600
            if event.key == pygame.K_d:
                player.changeX = 600
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
                elif shots[count - 1].state:
                    shots.append(
                        Bullet(player.x, player.y, "images/bullet.png", screen))
                    shots[count].state = True
                    count += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                player.changeX = player.changeY = 0
    if not player.restricted:

        player.clamp()
        player.move(seconds)
    n = 0
    score, rect = font.render(f'Score: {system.score}', (0, 0, 0))
    game_over, new_rect = font.render('Game Over!', (0, 0, 0))
    for enemy in enemies:
        enemy.move(seconds)
        if enemy.is_out():
            player.restrict()
            for i in ships:
                i.restrict()
            game_over_screen()
        else:
            enemy.clamp()
            enemy.draw_enemy()
            n += 1
    for ship in ships:
        if not ship.restricted:
            ship.draw_player()
            ship.move(seconds)
        else:
            for item in ships:
                item.restrict()
        if ship.is_colliding(player):
            ship.restrict()
            player.restrict()
            game_over_screen()
        if ship.y >= 600:
            ship.x = random.randint(1, 10) * 60
            ship.y = 0
            ship.changeY = random.randint(1, 10)*30
    n = 0
    for bullet in shots:

        if bullet.state:
            if not player.restricted:
                bullet.move(seconds)
                bullet.draw_bullet(bullet.x, bullet.y)
        for enemy in enemies:
            if bullet.is_colliding(enemy):
                bullet.state = False
                enemy.respawn()
                system.update_score()
        if bullet.y <= 0 or not bullet.state:
            shots.pop(n)
            count -= 1
            n += 1

    if not player.restricted:
        player.draw_player()
    elapsed = clock.tick(60)
    seconds = elapsed/1000.0
    pygame.display.update()
