import pygame as pg
import win32api, win32con

pg.init()

#사용자 모니터 주사율 받아오는 함수
def get_refresh_rate() -> int:
    dm = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    return dm.DisplayFrequency

#창 사이즈 설정
screen_width = 1280
screen_height = 720
pg.display.set_mode((screen_width, screen_height))
screen = pg.display.set_mode((screen_width, screen_height))

#사용자 모니터 주사율
user_display_frequency = get_refresh_rate()

#캐릭터 이동 좌표
to_x = 0
to_y = 0

#캐릭터 이동 속도
charcter_speed = 1

#게임 타이틀 설정
pg.display.set_caption("Good Game")

pg_icon = pg.image.load('#Enter the image')
pg.display.set_icon(pg_icon)
#게임 아이콘 설정
# pg_icon = pg.image.load('#Enter the image')#<----- 이미지 파일 첨부
# pg.display.set_icon(pg_icon)

#fps 설정
clock = pg.time.Clock()

#배경 설정
background = pg.image.load("./img/background/main_background.png")#<----- 이미지 파일 첨부

#캐릭터 설정
character = pg.image.load("./img/character/583231-1.png")#<----- 이미지 파일 첨부
character_size = character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1]


#캐릭터 좌표 설정
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

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