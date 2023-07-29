import pygame as pg
import win32api, win32con

#스크린 설정 - 해상도
screen_width = 1280
screen_height = 720
screen = pg.display.set_mode((screen_width, screen_height))

#스크린 설정 - 타이틀
pg.display.set_caption("Good Game")

#스크린 설정 - 주사율
user_display_frequency = 60
clock = pg.time.Clock()
dt = clock.tick(user_display_frequency)

#사진 불러오기
character = pg.image.load("./img/character/583231-1.png") #주요 캐릭터
background = pg.image.load("./img/background/main_background.png")#게임 배경
# pg_icon = pg.image.load('#Enter the image')#<----- 이미지 파일 첨부
# pg.display.set_icon(pg_icon)

#캐릭터 설정
to_x = 0
to_y = 0
character_size = character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
character_speed = 0.5


def boundary(): #경계 설정

    global character_x_pos, character_y_pos, screen_height, screen_width

    if character_x_pos < 0:
        character_x_pos = 0
        
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0

    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    return None


def get_refresh_rate(): #사용자 모니터 주사율 받아오는 함수

    global user_display_frequency

    dm = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    user_display_frequency = dm.DisplayFrequency

    return None


def screen_output():

    global character_x_pos, character_y_pos, character, background, screen

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pg.display.update()

    return None