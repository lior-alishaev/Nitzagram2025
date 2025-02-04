import pygame
from Comment import *
from constants import *
from helpers import *

class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, username, location, description): #TODO: add parameters
        #TODO: write me!
        self.username = username
        self.location = location
        self.description = description
        self.counter_likes = 0
        self.comments = []
        self.comments_display_index = 0

    def add_like(self):
        self.counter_likes += 1

    def add_comment(self, text):
        self.comments.append(Comment(text))

    def display(self, screen):
        self.display_content(screen)
        self.display_header(screen)
        self.display_likes(screen)

    def display_content(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), (POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))

    def display_header(self, screen):
        font = pygame.font.Font(None, 36)
        location_text = font.render(f"{self.location}", True, (0, 0, 0))
        description_text = font.render(self.description, True, (0, 0, 0))

        screen.blit(location_text, (POST_X_POS + 10, POST_Y_POS - 30))
        screen.blit(description_text, (POST_X_POS + 10, POST_Y_POS + POST_HEIGHT + 10))

    def display_likes(self, screen):
        font = pygame.font.Font(None, 36)
        likes_text = font.render(f"Likes: {self.counter_likes}", True, (255, 0, 0))
        screen.blit(likes_text, (POST_X_POS + POST_WIDTH - 100, POST_Y_POS + POST_HEIGHT + 10))

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break
