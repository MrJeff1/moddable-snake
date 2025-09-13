import pygame
from game import Game
from mod_loader import ModLoader

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Moddable Snake")
    clock = pygame.time.Clock()

    game = Game(screen, clock)
    loader = ModLoader(game)
    loader.load_mods()  # loads mods from mods/ folder

    game.run()

if __name__ == '__main__':
    main()
