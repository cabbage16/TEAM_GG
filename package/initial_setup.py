import pygame as pg
import win32api, win32con

#screen setting
def get_refresh_rate() -> int:
    dm = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    return dm.DisplayFrequency

user_display_frequency = get_refresh_rate()

screen_width = 1280
screen_height = 720
screen = pg.display.set_mode((screen_width, screen_height))

#chatacter setting
to_x = 0
to_y = 0

charcter_speed = 1

character = pg.image.load("./img/character/octocat_removebg.png")
character = pg.transform.scale(character, (100, 100))
character_size = character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1]

character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

#game setting
pg.display.set_caption("Good Game")
pg_icon = pg.image.load('./img/icon/gg.png')
pg.display.set_icon(pg_icon)
clock = pg.time.Clock()

#background setting
background = pg.image.load("./img/background/game_background.png")