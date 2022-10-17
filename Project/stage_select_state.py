from pico2d import *
import game_framework
import play_state

select_stage_image = None
icon_image = None
icon_size = None
playable_stage = None
icon_pos = None
X,Y = None,None

def enter():
    global select_stage_image, icon_image
    global icon_size
    global playable_stage
    global icon_pos
    global X,Y
    select_stage_image = load_image('stage_select.png')
    icon_image = load_image('stage_icon.png')
    icon_size=[110,120]
    playable_stage = 1
    icon_pos = [[],[50,186],[240,186], [431,186],[625,186]]
    X,Y = 0,1


def exit():
    global select_stage_image, icon_image, icon_size
    global playable_stage, icon_pos, X,Y
    del select_stage_image
    del icon_image
    del icon_size
    del playable_stage
    del icon_pos
    del X
    del Y




def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            #game_framework.push_state(play_state)
        elif event.type==SDL_KEYDOWN and event.key == SDLK_1:
            game_framework.push_state(play_state)


def update():
    pass


def draw():
    global icon_image
    global icon_size
    clear_canvas()
    select_stage_image.draw(get_canvas_width()//2,get_canvas_height()//2)
    for i in range(1,5):
        if playable_stage >= i:
            icon_image.clip_draw(icon_size[X]*(i-1),0,icon_size[X],icon_size[Y],icon_pos[i][X]+icon_size[X]//2,get_canvas_height()-(icon_pos[i][Y]+icon_size[Y]//2))


    update_canvas()
