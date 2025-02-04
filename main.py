import pygame
from constants import *
from helpers import *
from buttons import *
from classes.ImagePost import ImagePost
from classes.TextPost import TextPost


def main():
    # Set up the game display, clock and headline
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()


    # Change the title of the window
    pygame.display.set_caption('First Project - Instagram')

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,(WINDOW_WIDTH, WINDOW_HEIGHT))


    # TODO: add a post here

    posts = [
        ImagePost("lior", "Tel Aviv", "A beautiful sunset!", "images/noa_kirel.jpg"),
        TextPost("user2", "London", "Hello World!", (255, 255, 255), (0, 0, 0), "hi")
    ]
    current_post_index = 0
    running = True
    while running:
        screen.fill((255, 255, 255))  # רקע לבן
        current_post = posts[current_post_index]
        current_post.display()
        pygame.display.flip()
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if like_button.is_clicked(event.pos):
                    current_post.like_add()
                elif click_post_button.is_clicked(event.pos):
                    if current_post_index < len(posts) - 1:
                        current_post_index += 1
                    else:
                        current_post_index = 0

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
