import pygame
from pygame.sprite import Sprite

class Stars(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images\\star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def create_star(self):
        star.x = randint(0, self.settings.screen_width)
        star.rect.x = star.x
        star.y = randint(0, self.settings.screen_height)
        star.rect.y = star.y
        blitme()

    def blitme(self):
        for i in range(30):
            self.screen.blit(self.image, self.rect)

