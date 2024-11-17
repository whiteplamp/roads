import pygame


class BaseGameObject:
    def __init__(self, pos_x: int, pos_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y


class Button(BaseGameObject):
    BASE_COLOR = (128, 251, 0)
    BASE_WIDTH = 140
    BASE_HEIGHT = 60

    def __init__(self, label: str, pos_x: int, pos_y: int):
        self.label = label

        super().__init__(pos_x, pos_y)

    def draw(self, surface: pygame.Surface, font):
        text_surface = font.render('Some Text', False, (0, 0, 0))
        pygame.draw.rect(surface, self.BASE_COLOR, (self.pos_x, self.pos_y, self.BASE_WIDTH, self.BASE_HEIGHT), 0)
        surface.blit(text_surface, (self.pos_x, self.pos_y))
