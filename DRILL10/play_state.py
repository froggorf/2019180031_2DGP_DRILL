from pico2d import *
import game_framework
#import logo_state
import title_state
import item_state
import add_delete_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.ball_image= load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.item='None'

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 0.5
        if self.x > 800 :
            self.dir = -1
            self.x = 800
        elif self.x<0:
            self.dir = 1
            self.x = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

        if self.item=='BigBall':
            self.big_ball_image.draw(self.x+10,self.y+50)
        elif self.item=='Ball':
            self.ball_image.draw(self.x+10,self.y+50)


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                #game_framework.change_state(title_state)
                game_framework.quit()
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(add_delete_state)

boys = None
grass = None

# 초기화
def enter():
    global boys, grass
    boys = [Boy()]
    grass = Grass()

# 종료
def exit():
    global boys, grass
    del boys
    del grass

def update():
    for boy in boys:
        boy.update()

def draw():
    clear_canvas()
    grass.draw()
    for boy in boys:
        boy.draw()
    update_canvas()


def draw_world():  # item_state 에서 사용할 드로우
    grass.draw()
    for boy in boys:
        boy.draw()

def pause():
    pass

def resume():
    pass

def test_self():
    import sys

    pico2d.open_canvas()
    game_framework.run(sys.modules['__main__'])
    pico2d.close_canvas()

if __name__ == '__main__':# 만약 단독 실행이라면
    test_self()
