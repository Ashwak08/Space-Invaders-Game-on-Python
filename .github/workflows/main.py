import pygame
import random
import math

# intializing the pygame

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# backgroung
backgroung = pygame.image.load('spacebg.png')

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('management.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('gaming.png')
playerX = 370
playerY = 480
playerX_change = 0
# enemy
enemyImg = pygame.image.load('people.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

# bullet
bulletImg = pygame.image.load('security.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score :"+ str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop

running = True
while running:
    # RGB-Red,Green,Blue
    screen.fill((0, 0, 0))
    screen.blit(backgroung, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    # bullet moment
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(textX, textY)
    pygame.display.update()
