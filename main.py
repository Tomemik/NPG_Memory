import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Memory")
BG = pygame.image.load("assets/tło projekt.png")


def get_font(size):
    return pygame.font.Font(None, size)


def game(mode, lang):
    if mode == 3 and lang == 1:
        file = open("words/polish_hard.txt")
    elif mode == 2 and lang == 1:
        file = open("words/polish_medium.txt")
    elif mode == 1 and lang == 1:
        file = open("words/polish_easy.txt")
    elif mode == 3 and lang == 2:
        file = open("words/english_hard.txt")
    elif mode == 2 and lang == 2:
        file = open("words/english_medium.txt")
    elif mode == 1 and lang == 2:
        file = open("words/english_easy.txt")
    words = []
    for line in file:
        words.append(line)


def play(lang):
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(45).render("Wybierz poziom trudności", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)


        PLAY_MEDIUM = Button(image=pygame.image.load("assets/button.png"), pos =(400, 350),
                           text_input="Średni", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_HARD = Button(image=pygame.image.load("assets/button.png"), pos =(400, 550),
                           text_input="Trudny", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_BACK = Button(image=None, pos=(400, 750),
                           text_input="WRÓĆ", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_EASY = Button(image=pygame.image.load("assets/button.png"), pos =(400, 150),
                           text_input="Łatwy", font=get_font(75), base_color="White", hovering_color="Green")

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
                    main_menu(lang)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_EASY.checkForInput(PLAY_MOUSE_POS):
                    mode = 1
                    game(mode, lang)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_MEDIUM.checkForInput(PLAY_MOUSE_POS):
                    mode = 2
                    game(mode, lang)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_HARD.checkForInput(PLAY_MOUSE_POS):
                    mode = 3
                    game(mode, lang)

        pygame.display.update()


def options():
    while True:

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(45).render("Opcje", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 50))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(400, 750),
                              text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")
        OPTIONS_POL = Button(image=pygame.image.load("assets/button.png"), pos =(400, 150),
                           text_input="POL", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_ANG = Button(image=pygame.image.load("assets/button.png"), pos =(400, 300),
                           text_input="ANG", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_POL.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_POL.update(SCREEN)
        OPTIONS_ANG.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_ANG.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_POL.checkForInput(OPTIONS_MOUSE_POS):
                    lang = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_ANG.checkForInput(OPTIONS_MOUSE_POS):
                    lang = 2
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    if 'lang' in vars():
                        main_menu(lang)
                    else:
                        main_menu(1)

        pygame.display.update()


def main_menu(lang):
    while True:
        SCREEN.blit(BG, (0, 0))

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
                    play(lang)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu(1)