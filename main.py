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
        TextPost("Hello", WHITE, BLACK, "Tamrat", "London", "Enjoying my time!"),

        ImagePost("Tamrat", "Ramla", "A beautiful day!", "images/ronaldo.jpg"),
        TextPost("hi", WHITE, BLACK, "Tamrat", "America", "Enjoying my day!")
    ]

    current_post_index = 0
    running = True

    like_button = Button(LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS, LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT)
    comment_button = Button(COMMENT_BUTTON_X_POST, COMMENT_BUTTON_Y_POS, COMMENT_BUTTON_WIDTH,
                                 COMMENT_BUTTON_HEIGHT)
    share_button = Button(SHARE_BUTTON_X_POST, SHARE_BUTTON_Y_POS, SHARE_BUTTON_WIDTH, SHARE_BUTTON_HEIGHT)
    next_post_button = Button(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

    while running:
        screen.fill((0, 0, 0))

        screen.blit(background, (0, 0))

        current_post = posts[current_post_index]
        current_post.display()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if like_button.x_pos <= mouse_pos[0] <= like_button.x_pos + like_button.width and \
                        like_button.y_pos <= mouse_pos[1] <= like_button.y_pos + like_button.height:
                    posts[current_post_index].add_like()

                elif comment_button.x_pos <= mouse_pos[0] <= comment_button.x_pos + comment_button.width and \
                        comment_button.y_pos <= mouse_pos[1] <= comment_button.y_pos + comment_button.height:
                    posts[current_post_index].add_comment(read_comment_from_user())

                elif share_button.x_pos <= mouse_pos[0] <= share_button.x_pos + share_button.width and \
                        share_button.y_pos <= mouse_pos[1] <= share_button.y_pos + share_button.height:
                    print("Post Shared!")
                elif view_more_comments_button.x_pos <= mouse_pos[0] <= view_more_comments_button.x_pos + view_more_comments_button.width and \
                        view_more_comments_button.y_pos <= mouse_pos[1] <= view_more_comments_button.y_pos + view_more_comments_button.height:
                    posts[current_post_index].view_more_comments()
                else:
                    current_post_index += 1
                    if current_post_index >= len(posts):
                        current_post_index = 0


        pygame.display.update()
        clock.tick(60)
    pygame.quit()
main()