import pygame as pg
from .init_setup import character_speed, dt, character_x_pos, character_y_pos, to_x, to_y

def character(event): #캐릭터 움직임

    global to_x, to_y, character_speed

    # 키 다운 이벤트
    if event.type == pg.KEYDOWN:

        if event.key == pg.K_LEFT:
            to_x -= character_speed

        elif event.key == pg.K_RIGHT:
            to_x += character_speed

        elif event.key == pg.K_DOWN:
            to_y += character_speed

        elif event.key == pg.K_UP:
            to_y -= character_speed

        else: pass

    #키 업 이벤트
    if event.type == pg.KEYUP: 

        if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
            to_x = 0

        elif event.key == pg.K_UP or event.key == pg.K_DOWN:
            to_y = 0

        else: pass

    return None