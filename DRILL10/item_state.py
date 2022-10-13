from pico2d import *
import game_framework
import play_state
image = None
def enter():
    global image
    image = pico2d.load_image('add_delete_boy.png')
    pass

def exit():
    global image
    del image
    pass

def update():

    pass

def draw():
    global image
    pico2d.clear_canvas()
    play_state.draw_world()

    image.draw(400, 300)
    pico2d.update_canvas()
    pass

def handle_events():
    events = pico2d.get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == pico2d.SDL_KEYDOWN:
            #if event.key == pico2d.SDLK_ESCAPE:
            #    game_framework.pop_state()
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_0:
                    for boy in play_state.boys:
                        boy.item = 'None'
                    game_framework.pop_state()
                case pico2d.SDLK_1:
                    for boy in play_state.boys:
                        boy.item = 'Ball'
                    game_framework.pop_state()
                case pico2d.SDLK_2:
                    for boy in play_state.boys:
                        boy.item = 'BigBall'
                    game_framework.pop_state()

def test_self():
    import sys

    pico2d.open_canvas()
    game_framework.run(sys.modules['__main__'])
    pico2d.close_canvas()

if __name__ == '__main__':# 만약 단독 실행이라면
    test_self()
