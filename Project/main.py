from pico2d import *
import yoshi_character
import stage
X = 0
Y = 1

# 함수 정의
pressA = False
pressD = False
def handle_events():
    global pressA, pressD
    global gameRunning
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT or event.key == 96:
            gameRunning=False
        #A/a 키
        if event.key == SDLK_a:
            if event.type == SDL_KEYDOWN:
                if yoshi.motion != "RIGHT_WALK" and yoshi.motion != "RIGHT_RUN":
                    #if yoshi.motion != "LEFT_WALK":
                    pressA = True
                    yoshi.dir[X] -= 1
                    stageState.dir[X] -= 1
                    yoshi.change_motion("LEFT_WALK")
            else:
                if pressA:
                    yoshi.dir[X] += 1
                    stageState.dir[X] += 1
                    yoshi.change_motion("LEFT_IDLE_01")
                    pressA = False
        #D/d 키
        if event.key == SDLK_d:
            if event.type == SDL_KEYDOWN:
                if yoshi.motion != "LEFT_WALK" and yoshi.motion != "LEFT_RUN":
                    pressD = True
                    yoshi.dir[X] += 1
                    stageState.dir[X] += 1
                    yoshi.change_motion("RIGHT_WALK")
            else:
                if pressD:
                    pressD = False
                    yoshi.dir[X] -= 1
                    stageState.dir[X] -= 1
                    yoshi.change_motion("RIGHT_IDLE_01")
        #W/w 키
        if event.key == SDLK_w:
            if event.type == SDL_KEYDOWN:
                    stageState.dir[Y] += 1
            else:
                stageState.dir[Y] -= 1
        #S/s 키
        if event.key == SDLK_s:
            if event.type == SDL_KEYDOWN:
                    stageState.dir[Y] -= 1
            else:
                stageState.dir[Y] += 1
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


# initialization code (초기화 단계)
width,height = 1600,900
open_canvas(width,height)
gameMode = {"START":0, "SELECTSTAGE":1 ,"PLAYSTAGE":2}
gameRunning = True
yoshi = yoshi_character.Yoshi()
stageState = stage.StageState()


# game main loop code
while(gameRunning):
    #get_event
    handle_events()

    #game_logic
    yoshi.update()
    stageState.update()

    #game drawing
    clear_canvas()
    stageState.draw()
    yoshi.draw()

    update_canvas()

    delay(0.01)


# finalization code




