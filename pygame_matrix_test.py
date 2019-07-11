import sys
import pygame
from pygame.sprite import Sprite
from random import randint

class Raindrop():
    """Overall class to manage rain drops.""" 

    def __init__(self):
        pygame.init()
        
        self.screen_width = 600
        self.screen_height = 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Raindrops")

        self.bg_color = (7, 0, 88)
        self.rains = pygame.sprite.Group()
        self._create_rain_row()
        print(f"Initial Rain Numbers: {len(self.rains)}")

        self.let_rain = True

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_rain()
            self._update_screen()
            print(f"Rain Numbers: {len(self.rains)}")

    def _create_rain_row(self):
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        avaialbe_space_x = self.screen_width - 2 * rain_width
        rain_number_x = avaialbe_space_x // (2 * rain_width)
        for rain_number in range(rain_number_x):
            self._create_raindrop(rain_number)
    
    def _create_raindrop(self, rain_number):
        rain = Rain(self)
        rain_width = rain.rect.width
        rain.rect.x = rain_width + 2 * rain_number * rain_width
        self.rains.add(rain)

    def _update_rain(self):
        self._check_rain_edges()
        self.rains.update()

        if self.let_rain:
            for rain in self.rains.sprites():
                if rain.rect.top == self.screen.get_rect().centery:
                    self._create_rain_row()
                    self.let_rain = False
                    break

    def _check_rain_edges(self):
        for rain in self.rains.copy():
            if rain.check_edges():
                self.rains.remove(rain)
                if len(self.rains) < 500:
                    self.let_rain = True

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        for rain in self.rains.sprites():
            rain.draw_rain()
        pygame.display.flip()


class Rain(Sprite):
    """Represent rain behaviour"""

    def __init__(self, raindrop_game):
        super().__init__()
        self.screen = raindrop_game.screen

        random_number = randint(0, 1)
        # self.rect = pygame.Rect(0, 0, 5, 5)
        # self.y = float(self.rect.y)
        self.text_color = (130, 130, 130)
        self.bg_color = raindrop_game.bg_color
        
        self.rain_speed = randint(1, 5)
        self.prep_number(random_number)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True

    def update(self):
        self.y += self.rain_speed
        self.rect.y = self.y

    def prep_number(self):
        number_str = str(self.random_number)
        number_img = self.font.render(number_img, True, self.text_color, self.bg_color)

        self.rect = number_img.get_rect()
        self.rect.top = self.screen.top
        self.rect.x = randint(self.screen.right)

    def draw_rain(self):
        # pygame.draw.rect(self.screen, (113, 255, 255), self.rect)
        


if __name__ == "__main__":
    rd = Raindrop()
    rd.run_game()