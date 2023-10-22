import random
import pygame

def main():
    pygame.init()

    background_color = (0, 0, 0)
    text_Font = pygame.font.SysFont("Arial", 30)

    width = 1000
    height = 600

    circle_Speed = 2
    circle_Max_Speed = 5
    platform_Speed = 7

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("PingPong")
    screen.fill(background_color)

    clock = pygame.time.Clock()
    timer_Event = pygame.USEREVENT + 1
    delay = 10
    pygame.time.set_timer(timer_Event, delay)

    running = True

    platform_Rect = pygame.Rect((width - 40), 10, 30, 300)
    platform_Min_Size = 50

    pos_X = width / 2
    pos_Y = height / 2

    circle_Pos = pos_X, pos_Y

    circle_X_Dir = 1
    circle_Y_Dir = 1

    point = 0

    get_Point = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == timer_Event:
                pos_X += 1 * circle_Speed * circle_X_Dir
                pos_Y += 1 * circle_Speed * circle_Y_Dir

        collider = platform_Rect.collidepoint(circle_Pos)
        if collider:
            if get_Point == True:
                point += 1
            if platform_Rect.height > platform_Min_Size:
                platform_Rect.height -= 10
            if circle_Speed < circle_Max_Speed:
                circle_Speed += 0.5

            get_Point = False
            circle_X_Dir = -1
            circle_Y_Dir = random.randint(-1, 1)

        if (pos_X <= 0):
            get_Point = True
            circle_X_Dir = 1
            circle_Y_Dir = random.randint(-1, 1)

        if pos_X > width:
            pygame.quit()

        if circle_Y_Dir == 0:
            circle_Y_Dir = 1

        if pos_Y < 10:
            circle_Y_Dir = 1

        if pos_Y > height - 10:
            circle_Y_Dir = -1

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if platform_Rect.y > 0:
                platform_Rect.y -= 1 * platform_Speed

        if keys[pygame.K_DOWN]:
            if platform_Rect.y + platform_Rect.height < height:
                platform_Rect.y += 1 * platform_Speed

        screen.fill(background_color)

        pygame.draw.rect(screen, (0, 255, 0), platform_Rect)

        circle_Pos = pos_X, pos_Y
        pygame.draw.circle(screen, (255, 0, 0), circle_Pos, 10)

        point_Text = text_Font.render(str(point), True, (0, 255, 0))
        screen.blit(point_Text, (width / 2 - point_Text.get_width() / 2, 30))

        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()