import pygame
import random

background_color = (0, 0, 0)

width = 1280
height = 720

player_Speed = 10

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")
running = True

clock = pygame.time.Clock()
timer_Event = pygame.USEREVENT + 1
delay = 10
pygame.time.set_timer(timer_Event, delay)

box_left = pygame.Rect(10, 0, 30, 500)
box_right = pygame.Rect(width - 40, 0, 30, 500)

player_X = width / 2
player_Y = height / 2

player_X_Dir = 1
player_Y_Dir = 1

while running:
    clock.tick(60)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == timer_Event:
            if player_X == box_right.x:
                player_X_Dir = -1
                player_Y_Dir = random.randint(-1, 1)
                if player_Y_Dir == 0:
                    player_Y_Dir = random.randint(-1, 1)

            elif player_X == box_left.x:
                player_X_Dir = 1
                player_Y_Dir = random.randint(-1, 1)
                if player_Y_Dir == 0:
                    player_Y_Dir = random.randint(-1, 1)

            if player_Y == 0:
                player_Y_Dir = 1

            if player_Y == height:
                player_Y_Dir = -1

            player_X += 1 * player_X_Dir
            player_Y += 1 * player_Y_Dir

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        box_left.y -= 10

    if keys[pygame.K_s]:
        box_left.y += 10

    if keys[pygame.K_UP]:
        box_right.y -= 10

    if keys[pygame.K_DOWN]:
        box_right.y += 10

    screen.fill(background_color)
    pygame.draw.rect(screen, (255, 0, 0), box_left)
    pygame.draw.rect(screen, (0, 255, 0), box_right)

    #player
    player_Pos = player_X , player_Y
    pygame.draw.circle(screen, (0, 0, 255), player_Pos, 10)

    pygame.display.flip()