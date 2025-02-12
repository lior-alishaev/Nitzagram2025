from helpers import *
class Comment:
    def __init__(self, text_comment):
        self.text_comment = text_comment

    def display(self, position_index):
        comment_font = pygame.font.SysFont('fonts/CRIALTRIAL.ttf', COMMENT_TEXT_SIZE)
        comment_surface = comment_font.render(self.text_comment, True, BLACK)
        screen.blit(comment_surface, (FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + position_index * COMMENT_LINE_HEIGHT))