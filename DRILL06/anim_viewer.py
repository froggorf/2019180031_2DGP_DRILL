from pico2d import *
#이미지에는 오프셋이 44/38 이라고 적혀있으나, 테스트 결과 이미지의 크기가 너무 작은것 같아 88/76으로 2배 변환 하였습니다.

open_canvas(1000, 750)
background = load_image('background.png')
bunny = load_image('bunny.png')

x, y, frame, speed=500, 375, 1, 12
dict = {'STAY': 8, 'LEFT': 7, 'RIGHT': 6, 'UP': 5, 'DOWN': 4, 'LEFT_UP': 3, 'RIGHT_UP': 2, 'LEFT_DOWN': 1, 'RIGHT_DOWN': 0}
state = dict['STAY']

def draw(x, y):
    background.draw(500, 375)
    bunny.clip_draw(frame * 88, state*76, 88, 76, x, y)

def check_state(key):
    global motion, dict, state, frame
    if state != dict[key]:
        frame = 0
        state = dict[key]
        
def check_out_of_range():
    global x, y
    if x < 44: x = 44
    if x > 1000 - 44: x = 1000 - 44
    if y > 750 - 38:  y = 750 - 38
    if y < 38: y = 38

def motion(motion):
    global x, y, frame, state, speed
    if motion == 'STAY':
        check_state('STAY')
        frame = (frame + 1) % 5

    elif motion == 'LEFT':
        check_state('LEFT')
        frame = (frame + 1) % 6
        x -= speed

    elif motion == 'RIGHT':
        check_state('RIGHT')
        frame = (frame + 1) % 6
        x += speed

    elif motion == 'UP':
        check_state('UP')
        frame = (frame+1) % 8
        y += speed

    elif motion == 'DOWN':
        check_state('DOWN')
        frame = (frame+1) % 8
        y -= speed

    elif motion == 'LEFT_UP':
        check_state('LEFT_UP')
        frame = (frame+1) % 7
        x -= speed
        y += speed

    elif motion == 'RIGHT_DOWN':
        check_state('RIGHT_DOWN')
        frame = (frame + 1) % 7
        x += speed
        y -= speed

    elif motion == 'RIGHT_UP':
        check_state('RIGHT_UP')
        frame = (frame + 1) % 7
        x += speed
        y += speed

    elif motion == 'LEFT_DOWN':
        check_state('LEFT_DOWN')
        frame = (frame + 1) % 7
        x -= speed
        y -= speed

    check_out_of_range()
    draw(x, y)
    update_canvas()
    delay(0.1)
    get_events()


again=20
while True:
    clear_canvas()
    for i in range(again): motion('STAY')
    for i in range(again): motion('LEFT')
    for i in range(again): motion('RIGHT')
    for i in range(again): motion('UP')
    for i in range(again): motion('DOWN')
    for i in range(again): motion('LEFT_UP')
    for i in range(again): motion('RIGHT_DOWN')
    for i in range(again): motion('RIGHT_UP')
    for i in range(again): motion('LEFT_DOWN')

close_canvas()



