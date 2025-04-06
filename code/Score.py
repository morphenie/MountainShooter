import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.DBProxy import DBProxy
from code.const import C_LIGHT, SCORE_POS, MENU_OPTION, C_VIOLET, C_WHITE, WIN_WIDTH


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)  # cria-se um retângulo

        pass

    def save(self, menu_return: str, player_score: list[int]):
        pygame.mixer.music.load(f'./asset/Score.mp3')
        pygame.mixer.music.play(-1, fade_ms=2000)
        pygame.mixer.music.set_volume(0.6)
        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(40, 'YOU WON!!', C_LIGHT, SCORE_POS['Title'])

            if menu_return == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter your name (4 characters): '
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():  # para fechar janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:  # para escrever e salvar o score
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, C_VIOLET, SCORE_POS['Name'])

            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer.music.load(f'./asset/Score.mp3')
        pygame.mixer.music.play(-1, fade_ms=2000)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_WHITE, [WIN_WIDTH / 2, 50])
        self.score_text(20, 'NAME    SCORE       DATE   ', C_LIGHT, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'      {name}    {score:05d}     {date}', C_VIOLET,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():  # para fechar janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:  # para voltar ao menu
                    if event.key == K_ESCAPE:
                        return

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):  # texto do menu
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
