import pygame
import sys
import os

sprite_sheet = pygame.image.load(os.path.join("resources", "Swordsman", "Walk.png"))
sprite_images = [
    sprite_sheet.subsurface(pygame.Rect(i * 128, 0, 128, 128)) for i in range(5)
]

WIDTH = 900
HEIGHT = 600
FPS = 60
FLOOR = HEIGHT-6*HEIGHT/165+2

background_image = pygame.image.load(r"resources\Фон.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = sprite_images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.virtulal_index = 0
        self.direction = "RIGHT"
        self.x = self.rect.x
        self.y = self.rect.y
        self.v_x = 0
        self.v_y = 1
        self.a = 0.1

    def status(self):
        print(self.x, self.y, self.v_x, self.v_y)

    def update(self):
        # Cycle through the images to create the walking animation
        if self.direction == "LEFT":
            self.image = pygame.transform.flip(self.images[self.index], True, False)
        else:
            self.image = self.images[self.index]

        if self.rect.height + self.y < FLOOR:
            self.y += self.v_y
            self.v_y += self.a
        else:
            self.v_y = 0
            self.y = FLOOR - self.rect.height

        self.rect.x = self.x
        self.rect.y = self.y

    def move_left(self):
        self.virtulal_index = (self.virtulal_index + 1) % (10 * len(self.images))
        self.index = self.virtulal_index // 10
        self.x -= 2
        self.direction = "LEFT"

    def move_right(self):
        self.virtulal_index = (self.virtulal_index + 1) % (10 * len(self.images))
        self.index = self.virtulal_index // 10
        self.x += 2
        self.direction = "RIGHT"

    def move_up(self):
        self.v_y = -5
        self.y -= 5

    def move_down(self):
        pass


def main():
    pygame.init()

    # Set up some constants

    # Create the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Set up the clock for a consistent frame rate
    clock = pygame.time.Clock()

    # Create the player
    player = Player()
    all_sprites = pygame.sprite.Group(player)

    # Game loop
    running = True
    while running:
        # Keep the loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # Check for closing the window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move_up()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            player.move_left()
        if keys_pressed[pygame.K_RIGHT]:
            player.move_right()
        # if keys_pressed[pygame.K_UP]:
        #     player.move_up()
        if keys_pressed[pygame.K_DOWN]:
            player.move_down()

        # Update

        # Draw / render
        screen.blit(background_image, (0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()