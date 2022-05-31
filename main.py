import random

import pygame, sys
from button import Button
from box import InputBox
from Modules import pygame_textinput

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Memory")
BG = pygame.image.load("assets/tło projekt.png")
GAME_BG = pygame.image.load("assets/gameplay.png")


def get_font(size):
    return pygame.font.Font(None, size)


def game(mode, lang):
    clock = pygame.time.Clock()
    textinput = pygame_textinput.TextInputVisualizer()
    number = random.randrange(0, 24)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    points = 0
    timer = 5
    dt = 0

    if mode == 3 and lang == 1:
        file = open("words/polish_hard.txt", encoding="utf-8").read().splitlines()
    elif mode == 2 and lang == 1:
        file = open("words/polish_medium.txt", encoding="utf-8").read().splitlines()
    elif mode == 1 and lang == 1:
        file = open("words/polish_easy.txt", encoding="utf-8").read().splitlines()
    elif mode == 3 and lang == 2:
        file = open("words/english_hard.txt", encoding="utf-8").read().splitlines()
    elif mode == 2 and lang == 2:
        file = open("words/english_medium.txt", encoding="utf-8").read().splitlines()
    elif mode == 1 and lang == 2:
        file = open("words/english_easy.txt", encoding="utf-8").read().splitlines()
    words = []
    for line in file:
        words.append(line)

    SCREEN.blit(GAME_BG, (0, 0))
    while True:
        GAME_MOUSE_POS = pygame.mouse.get_pos()
        base_font = pygame.font.Font(None, 50)
        events = pygame.event.get()
        textinput.update(events)
        text_surface_out = base_font.render(words[number], True, (0, 0, 0))
        points_surface_out = base_font.render(str(points), True, (0, 0, 0))

        timer -= dt
        print(timer)

        SCREEN.blit(GAME_BG, (0, 0))
        if timer > 0:
            SCREEN.blit(text_surface_out, (300, 200))
        if timer < 0:
            SCREEN.blit(textinput.surface, (300, 600))
        SCREEN.blit(points_surface_out, (700, 100))

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and timer < 0:
                if textinput.value == words[number]:
                    points += 1
                else:
                    points = 0
                timer = 5
                textinput.value = ''
                number = random.randrange(0, 24)
        if timer > 0:
            textinput.value = ''

        pygame.display.update()
        dt = clock.tick(30) / 1000

def play(lang):
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(45).render("Wybierz poziom trudności", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_EASY = Button(image=pygame.image.load("assets/przycisk.png"), pos =(100, 250),
                           text_input="Łatwy", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_MEDIUM = Button(image=pygame.image.load("assets/przycisk.png"), pos =(100, 400),
                           text_input="Średni", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_HARD = Button(image=pygame.image.load("assets/przycisk.png"), pos =(100, 550),
                           text_input="Trudny", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_BACK = Button(image=pygame.image.load("assets/przycisk.png"), pos=(100, 700),
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

        PLAY_BUTTON = Button(image=pygame.image.load("assets/przycisk.png"), pos=(100, 250),
                             text_input="GRAJ", font=get_font(75), base_color="WHITE", hovering_color="GREEN")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/przycisk.png"), pos=(100, 400),
                             text_input="OPCJE", font=get_font(75), base_color="WHITE", hovering_color="GREEN")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/przycisk.png"), pos=(100, 550),
                             text_input="WYJDŹ", font=get_font(75), base_color="WHITE", hovering_color="GREEN")

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