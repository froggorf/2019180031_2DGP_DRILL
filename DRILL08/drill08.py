from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280,1024

def handle_events():
    global running
    global dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type==SDL_QUIT:
                running = False
        elif event.type == SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

def check_out_of_range():
    global x, y
    if x - 50 < 0:
        x = 50
    elif x + 50 > TUK_WIDTH:
        x = TUK_WIDTH - 50
    if y - 50 < 0:
        y = 50
    elif y + 50 > TUK_HEIGHT:
        y = TUK_HEIGHT - 50

def change_player_motion():
    global player_status, dir_x, dir_y
    if player_status == "LEFT_IDLE":
        if dir_x == -1:
            player_status = "LEFT_RUN"
        elif dir_x == 1:
            player_status = "RIGHT_RUN"
        elif dir_y != 0:
            player_status = "LEFT_RUN"

    elif player_status == "RIGHT_IDLE":
        if dir_x == -1:
            player_status = "LEFT_RUN"
        elif dir_x == 1:
            player_status = "RIGHT_RUN"
        elif dir_y != 0:
            player_status = "RIGHT_RUN"

    elif player_status == "LEFT_RUN":
        if dir_x == 0 and dir_y == 0:
            player_status = "LEFT_IDLE"
        elif dir_x == 1:
            player_status = "RIGHT_RUN"

    elif player_status == "RIGHT_RUN":
        if dir_x == 0 and dir_y == 0:
            player_status = "RIGHT_IDLE"
        elif dir_x == -1:
            player_status = "LEFT_RUN"


open_canvas(TUK_WIDTH, TUK_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
player = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
status = {"LEFT_RUN": 0, "RIGHT_RUN": 1,"LEFT_IDLE": 2, "RIGHT_IDLE": 3}
player_status = "RIGHT_IDLE"
dir_x, dir_y = 0, 0


hide_cursor()
while running:
    clear_canvas()
    kpu_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    player.clip_draw(frame * 100, 100 * status[player_status], 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    x += dir_x * 1
    y += dir_y * 1
    change_player_motion()
    check_out_of_range()
    handle_events()

close_canvas()




