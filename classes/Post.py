import pygame
from classes.Comment import Comment
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

    def view_more_comments(self):
        """
        Changes the 4 comments that the user see by changing the start index
        of comments.

        :return: None
        """
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            self.comments_display_index += NUM_OF_COMMENTS_TO_DISPLAY
            if self.comments_display_index >= len(self.comments):
                self.comments_display_index = 0

    def reset_comments_display_index(self):
        """
        Restart the comments display to show the first comments on the list
        Used when re-viewing the post.

        :return: None
        """
        self.comments_display_index = 0

    def display(self):
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()

    def display_content(self):
        #pygame.draw.rect(screen, (200, 200, 200), (POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))
        pass

    def display_header(self):
        font = pygame.font.Font('fonts/CRIALTRIAL.ttf', 36)
        location_text = font.render(self.location, True, BLACK)
        description_text = font.render(self.description, True, BLACK)
        username_text = font.render(self.username, True, BLACK)

        screen.blit(username_text, (USER_NAME_X_POS, USER_NAME_Y_POS))
        screen.blit(location_text, (POST_X_POS, POST_Y_POS))
        screen.blit(description_text, (POST_X_POS, POST_Y_POS + POST_HEIGHT))

    def display_likes(self):
        font = pygame.font.Font('fonts/CRIALTRIAL.ttf', 36)
        likes_text = font.render("Likes: " + str(self.counter_likes) ,True,   (255, 0, 0))
        screen.blit(likes_text, (POST_X_POS + POST_WIDTH, POST_Y_POS + POST_HEIGHT))

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.Font('fonts/CRIALTRIAL.ttf', COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break
