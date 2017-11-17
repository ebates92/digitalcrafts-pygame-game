import pygame
import random

class Monster(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.change_direction = 150

    def update(self, width, height):

        self.x += self.speed_x
        self.y += self.speed_y
        if self.x > width:
            self.x = 0
        if self.x < 0:
            self.x = width
        if self.y > height:
            self.y = 0
        if self.y < 0:
            self.y = height
        self.change_direction -= 1
        if self.change_direction == 0:
            self.speed_x = random.randint(-1,1)
            self.speed_y = random.randint(-1,1)
            self.change_direction = 150

# class Hero(object):

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)
    hero_x = width/2 + 5
    hero_y = height/2
    monster_x = 0
    monster_y = 0
    change_countdown = 20

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization

    monster_list = [
        Monster(random.randint(0,width),random.randint(0,height)),
        Monster(random.randint(0,width),random.randint(0,height)),
        Monster(random.randint(0,width),random.randint(0,height)),
        Monster(random.randint(0,width),random.randint(0,height)),
        Monster(random.randint(0,width),random.randint(0,height)),
        Monster(random.randint(0,width),random.randint(0,height)),
        Monster(random.randint(0,width),random.randint(0,height)),
        Monster(random.randint(0,width),random.randint(0,height)),
        Monster(random.randint(0,width),random.randint(0,height)),
        Monster(random.randint(0,width),random.randint(0,height)),
        Monster(random.randint(0,width),random.randint(0,height)),
        Monster(random.randint(0,width),random.randint(0,height)),
    ]

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw pictures
        screen.fill(blue_color)
        backround_image = pygame.image.load('images/background.png').convert_alpha()
        hero_image = pygame.image.load('images/captain-america.png').convert_alpha()
        monster_image = pygame.image.load('images/kim-joung-un-cartoon.png').convert_alpha()

        # Game display
        screen.blit(backround_image, (0,0))
        screen.blit(hero_image,(hero_x,hero_y))

        for monsters in monster_list:
            monsters.update(width, height)
            screen.blit(monster_image, (monsters.x, monsters.y))
        pygame.display.update()
        clock.tick(60)
        print change_countdown


    pygame.quit()

if __name__ == '__main__':
    main()
