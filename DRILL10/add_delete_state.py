from pico2d import *
import play_state
import game_framework

image = None
def enter():
    global image
    image = load_image('add_delete_boy.png')

def exit():
    global image
    del image

def update():
    pass
def draw():
    global image
    pico2d.clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    pico2d.update_canvas()

def handle_events():
    events = pico2d.get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == pico2d.SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case 61:    #SDLK_PLUS / SDLK_KP_PLUS 전부 작동하지 않아 직접 값을 찾아 넣었습니다.
                    play_state.boys += [play_state.Boy()]
                    game_framework.pop_state()
                case 45:
                    if len(play_state.boys)!=1 :
                        del play_state.boys[len(play_state.boys)-1]
                    game_framework.pop_state()

def pause():
    pass
def resume():
    pass
