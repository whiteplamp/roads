import pygame as pygame

from src.without_optimization.structures import RoadMap


class Visualizer:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, _map: RoadMap):
        self.map = _map
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Map")

    def draw(self):
        running = True

        while running:
            self.screen.fill(self.WHITE)

            for road in self.map.roads:
                pygame.draw.circle(self.screen, self.BLACK, (road.a.pos_x, road.a.pos_y), 4)
                pygame.draw.circle(self.screen, self.BLACK, (road.b.pos_x, road.b.pos_y), 4)
                pygame.draw.line(self.screen, self.BLACK, (road.a.pos_x, road.a.pos_y), (road.b.pos_x, road.b.pos_y), 2)

            pygame.display.flip()

            for event in pygame.event.get():
                # проверить закрытие окна
                if event.type == pygame.QUIT:
                    running = False
