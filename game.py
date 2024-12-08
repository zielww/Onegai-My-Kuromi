import sys

import pygame

from scripts.utils import load_image, load_images, Animation
from scripts.entities import PhysicsEntity, Player
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds


class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        # Change window name
        pygame.display.set_caption('Kuromi Legends')

        # Change window resolution
        self.screen = pygame.display.set_mode((640, 480))

        # Initialize second surface for rendering (used for asset scaling)
        self.display = pygame.Surface((320, 240))

        # initialize game clock
        self.clock = pygame.time.Clock()

        # Movement variable
        self.movement = [False, False]

        # Initialize Assets
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds'),
            'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
            'player/run': Animation(load_images('entities/player/run'), img_dur=4),
            'player/jump': Animation(load_images('entities/player/jump')),
            'player/slide': Animation(load_images('entities/player/slide')),
            'player/wall_slide': Animation(load_images('entities/player/wall_slide')),
        }

        # Define Clouds
        self.clouds = Clouds(self.assets['clouds'], count=16)

        # Define Player
        self.player = Player(self, (50, 50), (8, 15))

        # Define Tile Map
        self.tilemap = Tilemap(self, tile_size=16)

        # Add Camera
        self.scroll = [0, 0]

    def run(self):
        while True:
            # Clear the Screen
            self.display.blit(self.assets['background'], (0, 0))

            # Position the camera in the center of the screen (player)
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            # Remove jittery shit
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            # Render Clouds
            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll )

            # Render tile map
            self.tilemap.render(self.display, offset=render_scroll)

            # Update pos
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            # Render Player
            self.player.render(self.display, offset=render_scroll)

            # Loop for All type of Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            # Blit the display into the screen
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            # Method to update the screen every frame
            pygame.display.update()
            self.clock.tick(60)


# Initialize the Game
Game().run()
