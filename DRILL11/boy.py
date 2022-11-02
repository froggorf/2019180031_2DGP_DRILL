# 발판 블럭 이미지 클래스 변수로 수정하기
#
# play_state에 handle_event 요시쪽으로 옮기기
# 좌우 동시입력에대한 처리 비슷하게 처리해주기
#
# 발판 블럭에 대해서도 상태를 넣어서 해보기 (커진상태 일반상태)

from pico2d import *

#이벤트 정의
RD, LD, RU, LU, TIMER, AD, AU = range(7)       #0,1,2,3

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): AD,
    (SDL_KEYUP, SDLK_a): AU
}

class SLEEP:
    @staticmethod
    def enter(self, event):
        print('enter - SLEEP')
        self.dir = 0
        pass
    @staticmethod
    def exit(self):
        print('exit - SLEEP')
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame+1)%8
        pass
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            #self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            self.image.clip_composite_draw(self.frame*100,300,100,100,3.141592/2,'',self.x-25,self.y-25,100,100)
        else:
            #self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)

        pass


#클래스를 이용해서 상태를 만든다.
class IDLE:
    @staticmethod
    def enter(self, event):
        print('enter - IDLE')
        self.dir = 0
        self.timer = 1000

        pass
    @staticmethod
    def exit(self):
        print('exit - IDLE')
        IDLE.check_error = 0
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame+1)%8
        self.timer-=1
        if self.timer == 0 :
            #이벤트를 발생시키기 TIMER 이벤트
            #self.q.insert(0,TIMER)  #q를 직접 액세스 하므로 객체 지향 프로그래밍 위배.
            self.add_event(TIMER)   #객치제항적 방법

        pass
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

        pass

class RUN:
    def enter(self, event):
        print('enter - RUN')
        if event == RD :
            self.dir += 1

        elif event == LD: self.dir -= 1
        elif event == RU: self.dir -= 1
        elif event == LU: self.dir += 1


    def exit(self):
        print('exit - RUN')
        #run 을 나가서, idle로 갈 때 run의 방향을 알려줄 필요가 있다.
        self.face_dir = self.dir
        pass

    def do(self):
        self.frame  =(self.frame+1)%8
        self.x += self.dir
        self.x = clamp(0,self.x,800)

        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

class AUTO_RUN:
    def enter(self, event):
        print('enter - AUTO_RUN')
        self.dir = self.face_dir


        pass

    def exit(self):
        print('exit - AUTO_RUN')
        #run 을 나가서, idle로 갈 때 run의 방향을 알려줄 필요가 있다.
        #self.face_dir = self.dir
        self.dir = 0
        pass

    def do(self):
        self.frame  =(self.frame+1)%8
        self.x += self.dir
        #self.x = clamp(0,self.x,800)
        if self.x<0:
            self.face_dir = 1
            self.dir = 1
            self.x = 0
        elif self.x>800:
            self.face_dir=-1
            self.dir=-1
            self.x = 800


    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y+25,200,200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y+25,200,200)
        pass

#상태에 대한 테이블
next_state = {
    #IDLE 상태에서 RU를 누르면 RUN 상태로 가고...

    IDLE: {RU:RUN, LU:RUN, RD:RUN,LD:RUN, TIMER:SLEEP, AD:AUTO_RUN, AU:IDLE},
    RUN: {RU:IDLE, LU:IDLE, LD:IDLE,RD:IDLE, AD: AUTO_RUN, AU:RUN},
    AUTO_RUN: {RU:RUN, LU:RUN, RD:RUN, LD:RUN, AD:IDLE, AU:AUTO_RUN},
    SLEEP: {RU:RUN, LU:RUN, RD: RUN, LD: RUN,AD:SLEEP, AU:SLEEP} # SLEEP : ERROR_STATE
}



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

        if self.q: # q에 뭔가 들어있다면,
            event = self.q.pop()    #이벤트를 가져오고,
            self.cur_state.exit(self)   #현재 상태를 나가고,
            self.cur_state = next_state[self.cur_state][event] #다음 상태를 계산하고,
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

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