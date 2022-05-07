import pygame

WIDTH, HEIGHT = 300, 300
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

background_colour = (BLACK)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Memory')


def draw_window():
    screen.fill(BLACK)
    pygame.display.update()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()