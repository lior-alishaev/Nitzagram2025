from helpers import *
from buttons import *
from classes.ImagePost import ImagePost
from classes.TextPost import TextPost


def main():
    # Set up the game display, clock and headline
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('First Project - Instagram')
    clock = pygame.time.Clock()

    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,(WINDOW_WIDTH, WINDOW_HEIGHT))


    # TODO: add a post here

    posts = [
        ImagePost("lior", "Tel Aviv", "A beautiful sunset!", "images/noa_kirel.jpg"),
        TextPost("Hello", WHITE, BLACK, "Tamrat", "London", "Enjoying my time!")
    ]

    current_post_index = 0
    running = True

    while running:
        screen.fill(WHITE)
        current_post = posts[current_post_index]
        current_post.display()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if like_button.is_clicked():
                    current_post.add_like()
                elif click_post_button.is_clicked():
                    if current_post_index < len(posts) - 1:
                        current_post_index += 1
                    else:
                        current_post_index = 0

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
main()