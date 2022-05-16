import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Memory")

def get_font(size):
    return pygame.font.Font(None, size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("Wybierz poziom trudności", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_EASY = Button(image=pygame.image.load("assets/button.png"), pos =(400, 150),
                           text_input="Łatwy", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_MEDIUM = Button(image=pygame.image.load("assets/button.png"), pos =(400, 350),
                           text_input="Średni", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_HARD = Button(image=pygame.image.load("assets/button.png"), pos =(400, 550),
                           text_input="Trudny", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_BACK = Button(image=None, pos=(400, 750),
                           text_input="WRÓĆ", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_EASY.changeColor(PLAY_MOUSE_POS)
        PLAY_EASY.update(SCREEN)
        PLAY_MEDIUM.changeColor(PLAY_MOUSE_POS)
        PLAY_MEDIUM.update(SCREEN)
        PLAY_HARD.changeColor(PLAY_MOUSE_POS)
        PLAY_HARD.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()


        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        OPTIONS_TEXT = get_font(45).render("Opcje", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 50))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(400, 750),
                              text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.fill("black")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(400, 250),
                             text_input="GRAJ", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(400, 400),
                                text_input="OPCJE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(400, 550),
                             text_input="WYJDŹ", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()