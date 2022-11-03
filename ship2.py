import pygame


class Ship:
    """A class to manage the bird."""

    def __init__(self, bb_game):
        """Initialize the bird and set its starting position."""
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()

        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new bird at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
