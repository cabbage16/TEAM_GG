import pygame as pg
from package.initial_setup import *

pg.init()



running = True

while running:
    dt = clock.tick(user_display_frequency) #fps 설정
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        #키 다운 이벤트
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                to_x -= 0.5
            elif event.key == pg.K_RIGHT:
                to_x += 0.5
            elif event.key == pg.K_DOWN:
                to_y += 0.5
            elif event.key == pg.K_UP:
                to_y -= 0.5

        #키 업 이벤트
        if event.type == pg.KEYUP: 
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                to_x = 0
            elif event.key == pg.K_UP or event.key == pg.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #경계 설정
    if character_x_pos < 0:
        character_x_pos = 0

    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0

    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #화면 출력
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pg.display.update()
    
pg.quit()