from pico2d import *

import game_framework
#import play_state
import stage_select_state
image = None

def enter():
    # fill here
    global image
    image = load_image('title.png')

def exit():
    global image
    del image

def handle_events():
    # fill here
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(stage_select_state)


def draw():
    clear_canvas()
    image.clip_draw(0,0,800,600,get_canvas_width()//2,get_canvas_height()//2,get_canvas_width(),get_canvas_height())
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass


