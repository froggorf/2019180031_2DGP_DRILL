from pico2d import *
import game_framework
import play_state
image = None
select = None
handImage = None
def enter():
    global image,select,handImage
    image = load_image('pause.png')
    select = 0
    handImage=load_image('hand.png')

def exit():
    global image,select,handImage
    del image
    del select
    del handImage

def handle_events():
    global select
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()
        elif event.type==SDL_KEYDOWN and event.key == SDLK_LEFT:
            select -=1
            if select<0:
                select = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            select += 1
            if select > 1:
                select = 0
        elif event.type == SDL_KEYDOWN and (event.key == SDLK_SPACE or event.key == 13):    #스페이스바 or 엔터
            if select == 0:
                game_framework.pop_state()
            elif select == 1:
                play_state.on_quit_game()
                game_framework.pop_state()



def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(get_canvas_width()//2,get_canvas_height()//2)
    if select == 0:
        handImage.draw(get_canvas_width()//2+184+50-image.w//2,get_canvas_height()//2+14+50-image.h//2)
    elif select == 1:
        handImage.draw(get_canvas_width()//2+418+50-image.w//2,get_canvas_height()//2+14+50-image.h//2)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass


