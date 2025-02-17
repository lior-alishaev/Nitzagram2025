from classes.Post import Post
import pygame
from constants import *
from  helpers import *
class TextPost(Post):
    def __init__(self, text, text_color, background_color, username, location, description,):
        super().__init__(username, location, description)
        self.text_array = from_text_to_array(text)
        self.text_color = text_color
        self.background_color = background_color

    def display(self):
        pygame.draw.rect(screen, self.background_color, pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))
        font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
        for i, line in enumerate(self.text_array):
            text_surface = font.render(line, True, self.text_color)
            screen.blit(text_surface, center_text(len(self.text_array), text_surface, i))
        super().display()