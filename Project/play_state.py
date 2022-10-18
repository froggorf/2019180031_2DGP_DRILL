import game_framework
from pico2d import *
import yoshi_character
import stage
import pause_state

X = 0
Y = 1
pressA = False
pressD = False
quit_game = False
gameMode = {"START":0, "SELECTSTAGE":1 ,"PLAYSTAGE":2}
yoshi =None
stageState = None

def enter():
    global X,Y
    X = 0
    Y = 1
    global pressA, pressD
    pressA = False
    pressD = False
    global gameMode, yoshi, stageState
    gameMode = {"START": 0, "SELECTSTAGE": 1, "PLAYSTAGE": 2}
    yoshi = yoshi_character.Yoshi()
    stageState = stage.StageState()
    global quit_game
    quit_game=False

def exit():
    global X, Y
    del X
    del Y
    global pressA, pressD
    del pressA
    del pressD
    global gameMode, yoshi, stageState
    del gameMode
    del yoshi
    del stageState
    global quit_game
    del quit_game

def update():
    yoshi.update()
    stageState.update()

def draw_world():
    stageState.draw(yoshi.x, yoshi.y)
    yoshi.draw()


def draw():
    clear_canvas()
    stageState.draw(yoshi.x,yoshi.y)
    yoshi.draw()
    # for rect in stageState.groundRect:
    #     pico2d.draw_rectangle(rect.left,rect.bottom, rect.right,rect.top)
    update_canvas()
    delay(0.01)

def handle_events():
    global pressA, pressD
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == 96:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_state)
        #A/a 키
        if event.key == SDLK_a:
            if event.type == SDL_KEYDOWN:
                if yoshi.motion != "RIGHT_WALK" and yoshi.motion != "RIGHT_RUN":
                    #if yoshi.motion != "LEFT_WALK":
                    pressA = True
                    yoshi.dir[X] -= 1
                    stageState.dir[X] -= 1
                    if yoshi.motion == "RIGHT_JUMP" or yoshi.motion=="LEFT_JUMP":
                        yoshi.change_motion("LEFT_JUMP")
                    elif yoshi.motion == "RIGHT_FALL" or yoshi.motion == "LEFT_FALL":
                        yoshi.change_motion("LEFT_FALL")
                    else:
                        yoshi.change_motion("LEFT_WALK")
            else:
                if pressA:
                    yoshi.dir[X] += 1
                    stageState.dir[X] += 1
                    if yoshi.motion != "RIGHT_JUMP" and yoshi.motion != "LEFT_JUMP" and yoshi.motion!="RIGHT_FALL" and yoshi.motion!="LEFT_FALL":
                        yoshi.change_motion("LEFT_IDLE_01")
                    pressA = False
        #D/d 키
        if event.key == SDLK_d:
            if event.type == SDL_KEYDOWN:
                if yoshi.motion != "LEFT_WALK" and yoshi.motion != "LEFT_RUN":
                    pressD = True
                    yoshi.dir[X] += 1
                    stageState.dir[X] += 1
                    if yoshi.motion == "RIGHT_JUMP" or yoshi.motion=="LEFT_JUMP":
                        yoshi.change_motion("RIGHT_JUMP")
                    elif yoshi.motion == "RIGHT_FALL" or yoshi.motion == "LEFT_FALL":
                        yoshi.change_motion("RIGHT_FALL")
                    else:
                        yoshi.change_motion("RIGHT_WALK")
            else:
                if pressD:
                    pressD = False
                    yoshi.dir[X] -= 1
                    stageState.dir[X] -= 1
                    if yoshi.motion != "RIGHT_JUMP" and yoshi.motion != "LEFT_JUMP" and yoshi.motion!="RIGHT_FALL" and yoshi.motion!="LEFT_FALL":
                        yoshi.change_motion("RIGHT_IDLE_01")
        #W/w 키
        if event.key == SDLK_w:
            if event.type == SDL_KEYDOWN:
                if yoshi.motion != "RIGHT_FALL" and yoshi.motion!="LEFT_FALL":
                    yoshi.pressJump += 1
                    if yoshi.motion == "RIGHT_IDLE_01" or yoshi.motion == "RIGHT_IDLE_02" or yoshi.motion == "RIGHT_WALK" or yoshi.motion == "RIGHT_RUN" or yoshi.motion == "RIGHT_JUMP":
                        yoshi.change_motion("RIGHT_JUMP")
                    else:
                        yoshi.change_motion("LEFT_JUMP")
            else:
                yoshi.pressJump = 0
                if yoshi.motion == "RIGHT_IDLE_01" or yoshi.motion == "RIGHT_IDLE_02" or yoshi.motion == "RIGHT_WALK" or yoshi.motion == "RIGHT_RUN" or yoshi.motion == "RIGHT_JUMP" or yoshi.motion == "RIGHT_FALL":
                    yoshi.change_motion("RIGHT_FALL")
                else:
                    yoshi.change_motion("LEFT_FALL")
        #S/s 키
        if event.key == SDLK_s:
            if event.type == SDL_KEYDOWN:
                pass
            else:
                pass
        #SHIFT 키
        if event.key == SDLK_LSHIFT:
            if event.type == SDL_KEYDOWN:
                if yoshi.motion == "LEFT_WALK":
                    yoshi.change_motion("LEFT_RUN")
                elif yoshi.motion == "RIGHT_WALK":
                    yoshi.change_motion("RIGHT_RUN")
            else:
                if yoshi.motion == "LEFT_RUN":
                    yoshi.change_motion("LEFT_WALK")
                elif yoshi.motion == "RIGHT_RUN":
                    yoshi.change_motion("RIGHT_WALK")

if __name__ == '__main__':
    print('실행중')

def on_quit_game():
    global quit_game
    quit_game=True

def resume():
    if quit_game == True:
        game_framework.pop_state()

def pause():
    pass