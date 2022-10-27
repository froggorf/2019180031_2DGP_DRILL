# 발판 블럭 이미지 클래스 변수로 수정하기
#
# play_state에 handle_event 요시쪽으로 옮기기
# 좌우 동시입력에대한 처리 비슷하게 처리해주기
#
# 발판 블럭에 대해서도 상태를 넣어서 해보기 (커진상태 일반상태)

from pico2d import *

#이벤트 정의
RD, LD, RU, LU = range(4)       #0,1,2,3

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,

}

#클래스를 이용해서 상태를 만든다.
class IDLE:
    @staticmethod
    def enter():
        print('enter - IDLE')
        pass
    @staticmethod
    def exit():
        print('exit - IDLE')
        pass
    @staticmethod
    def do():
        pass
    @staticmethod
    def draw():
        pass

class RUN:
    def enter():
        print('enter - RUN')
        pass

    def exit():
        print('exit - RUN')
        pass

    def do():
        pass

    def draw():
        pass

#상태에 대한 테이블
next_state = {
    #IDLE 상태에서 RU를 누르면 RUN 상태로 가고...
    IDLE: {RU:RUN, LU:RUN, RD:RUN,LD:RUN},  #좌우 키를 동시에 누르면 IDLE 상태인데 한쪽을 떼면 RUN으로 가야하니까
    RUN: {RU:IDLE, LU:IDLE, LD:IDLE,RD:IDLE}
}



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter()

    def update(self):
        self.cur_state.do()
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)


    def draw(self):
        self.cur_state.draw()
        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event): # 소년이 스스로 이벤트를 처리할 수 있도록
        # event 는 키이벤트, 이것을 내부 RD, LU 등으로 변환
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            self.add_event(key_event)   #변환된 내부 이벤트를 큐에 추가

        if self.q: # q에 뭔가 들어있다면,
            event = self.q.pop()    #이벤트를 가져오고,
            self.cur_state.exit()   #현재 상태를 나가고,
            self.cur_state = next_state[self.cur_state][event] #다음 상태를 계산하고,
            self.cur_state.enter()


        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        #
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1