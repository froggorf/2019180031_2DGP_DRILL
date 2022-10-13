from pico2d import *
import random

yoshi_state = {"MARIO": 0 , "NOMARIO":1, "MARIO_SWALLOW":2, "NOMARIO_SWALLOW":3}
yoshi_motion = {"RIGHT_IDLE_01":0, "LEFT_IDLE_01":1,"RIGHT_IDLE_02":2,"LEFT_IDLE_02":3, "RIGHT_WALK":4,"LEFT_WALK":5, "RIGHT_RUN":6, "LEFT_RUN":7}
yoshi_offset = [
    [(int(62*1.6),int(66*1.6)),(int(62*1.6),int(66*1.6)),(int(62*1.6),int(64*1.6)),(int(62*1.6),int(64*1.6)),(int(64*1.6),int(66*1.6)),(int(64*1.6),int(66*1.6)),(int(72*1.6),int(1.6*68)),(int(72*1.6),int(1.6*68))],
    [5],
    [5],
    [5]
]
yoshi_delay = [8,8,10,10,8,8,8,8,8]
yoshi_motion_num = [8,8,5,5,8,8,2,2]
X = 0
Y = 1


class Yoshi:
    def __init__(self):
        self.image = [load_image("yoshi_mario.png")]
        #위치 관련
        self.x = 150
        self.y = 150

        #상태 관련
        self.state = "MARIO"
        self.motion = "RIGHT_IDLE_02"
        self.frame = 0
        self.delay = 0
        self.offset = yoshi_offset[yoshi_state[self.state]][yoshi_motion[self.motion]]

        #이동 관련
        self.dir = [0, 0]
        self.speed = 5

    #그리기 관련 함수
    def sprite_update(self):
        if self.delay >= yoshi_delay[yoshi_motion[self.motion]] :
            self.frame = (self.frame+1)%yoshi_motion_num[yoshi_motion[self.motion]]
            self.delay = 0
            if (self.motion == "RIGHT_IDLE_01" or self.motion == "RIGHT_IDLE_02") and self.frame == 0:
                if random.randint(0, 3) == 0:
                    self.change_motion("RIGHT_IDLE_02")
                else:
                    self.change_motion("RIGHT_IDLE_01")
            elif (self.motion == "LEFT_IDLE_01" or self.motion == "LEFT_IDLE_02") and self.frame == 0:
                if random.randint(0, 3) == 0:
                    self.change_motion("LEFT_IDLE_02")
                else:
                    self.change_motion("LEFT_IDLE_01")
        else:
            self.delay += 1

    def draw(self):
        if self.state == "MARIO":
            self.image[yoshi_state[self.state]].clip_draw(
                self.offset[0]*self.frame,
                160*yoshi_motion[self.motion],
                self.offset[0],
                self.offset[1],
                self.x+self.offset[0]//2,
                self.y+self.offset[1]//2
            )

    def move(self):
        self.x += self.dir[X] * self.speed
        if yoshi_motion == "RIGHT_RUN" or yoshi_motion == "LEFT_RUN":
            self.x += self.dir[X] * self.speed


    def update(self):
        self.offset = yoshi_offset[yoshi_state[self.state]][yoshi_motion[self.motion]]
        #if self.dir[X] == 1:

        self.sprite_update()
        #self.move()



    def change_motion(self, c_motion):
        self.motion = c_motion
        self.delay = 0
        self.frame = 0


