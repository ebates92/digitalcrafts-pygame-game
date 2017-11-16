import pygame

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)
    monster_x = width/2 + 5
    monster_y = height/2

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        if monster_x > 512:
            monster_x = 0

        # Draw pictures
        backround_image = pygame.image.load('images/background.png').convert_alpha()
        screen.fill(blue_color)
        hero_image = pygame.image.load('images/hero.png').convert_alpha()

        # Game display
        screen.blit(backround_image, (0,0))
        screen.blit(hero_image,(monster_x,monster_y))
        pygame.display.update()
        clock.tick(60)


    pygame.quit()

if __name__ == '__main__':
    main()
