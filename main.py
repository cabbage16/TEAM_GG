import pygame as pg
import game_pkg.move as mv, game_pkg.init_setup as setup

pg.init()

#사용자 모니터 주사율
setup.get_refresh_rate()

running = True

while running:

    setup.dt #fps 설정

    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            running = False

        mv.character(event)

    setup.character_x_pos += mv.to_x * setup.dt
    setup.character_y_pos += mv.to_y * setup.dt

    #경계 설정
    setup.boundary()

    #화면 출력
    setup.screen_output()
    
pg.quit()