import pygame as pg

pg.init()

screen_width = 1280
screen_height = 720
pg.display.set_mode((screen_width, screen_height))

pg.display.set_caption("Good Game")

pg_icon = pg.image.load('#Enter the image')
pg.display.set_icon(pg_icon)

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.update()
    
pg.quit()