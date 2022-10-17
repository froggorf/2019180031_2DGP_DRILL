from pico2d import *
import game_framework
import title_state

running = True
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('tukorea_logo.png')

def exit():
    global image
    del image


def update():
    global logo_time
    delay(0.01)
    logo_time += 0.01
    if logo_time > 1.0:
        logo_time=0
        game_framework.change_state(title_state)

def draw():
    clear_canvas()
    image.clip_draw(0,0,800,600,get_canvas_width()//2,get_canvas_height()//2,get_canvas_width(),get_canvas_height())
    update_canvas()

def handle_events():
    events = get_events()

