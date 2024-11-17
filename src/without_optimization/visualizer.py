import pygame as pygame

from src.without_optimization.game_structures import Button
from src.without_optimization.structures import RoadMap


class Visualizer:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.font = pygame.font.SysFont('Comic Sans MS', 10)

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Map")
        self.button = Button(pos_x=200, pos_y=200, label="Создать")

    def draw(self):
        self.button.draw(self.screen, self.font)

    def main(self):
        running = True

        while running:
            self.screen.fill(self.WHITE)

            self.draw()

            pygame.display.flip()

            for event in pygame.event.get():
                # проверить закрытие окна
                if event.type == pygame.QUIT:
                    running = False

