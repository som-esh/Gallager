import sys
import pygame
import game_functions as gf
from ship import Ship
from settings import Settings

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship= Ship(ai_settings, screen)
    while True:
        screen.fill(ai_settings.bg_color)
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
