from pico2d import *
import random

yoshi_state = {"MARIO": 0 , "NOMARIO":1, "MARIO_SWALLOW":2, "NOMARIO_SWALLOW":3}
yoshi_motion = {"RIGHT_IDLE_01":0, "LEFT_IDLE_01":1,"RIGHT_IDLE_02":2,"LEFT_IDLE_02":3, "RIGHT_WALK":4,"LEFT_WALK":5, "RIGHT_RUN":6, "LEFT_RUN":7, "RIGHT_JUMP":10, "LEFT_JUMP":11, "RIGHT_FALL":12, "LEFT_FALL":13}
yoshi_offset = [
    [(int(62*1.6),int(66*1.6)),(int(62*1.6),int(66*1.6)),(int(62*1.6),int(64*1.6)),(int(62*1.6),int(64*1.6)),(int(64*1.6),int(66*1.6)),(int(64*1.6),int(66*1.6)),(int(72*1.6),int(1.6*68)),(int(72*1.6),int(1.6*68)),(),(),(int(60*1.6),int(72*1.6)),(int(60*1.6),int(72*1.6)),(int(58*1.6),int(62*1.6)),(int(58*1.6),int(62*1.6))],
    [5],
    [5],
    [5]
]
yoshi_delay = [8,8,10,10,8,8,8,8,8,0,0,0,0,0,0]
yoshi_motion_num = [8,8,5,5,8,8,2,2,0,0,1,1,1,1]
X = 0
Y = 1
GRAVITY = 5
MAXJUMPTIME = 12
jump_delay = 0

class Yoshi:
    def __init__(self):
        self.image = [load_image("yoshi_mario.png")]
        #위치 관련
        self.x = 253
        self.y = 320

        #상태 관련
        self.state = "MARIO"
        self.motion = "RIGHT_IDLE_02"
        self.frame = 0
        self.delay = 0
        self.offset = yoshi_offset[yoshi_state[self.state]][yoshi_motion[self.motion]]

        #이동 관련
        self.dir = [0, 0]
        self.speed = 5
        self.gravity = -5

        #카메라 관련
        self.camera = [0,0]

        #점프 관련
        self.pressJump = False

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

            # elif self.x>
            self.image[yoshi_state[self.state]].clip_draw(
                self.offset[0]*self.frame,
                160*yoshi_motion[self.motion],
                self.offset[0],
                self.offset[1],
                self.camera[X]+self.offset[0]//2,
                self.camera[Y]+self.offset[1]//2
            )



    def update(self):
        self.offset = yoshi_offset[yoshi_state[self.state]][yoshi_motion[self.motion]]
        #if self.dir[X] == 1:

        self.sprite_update()
        self.check_jump()
        self.calc_gravity()
        self.move()
        self.check_camera()

    def check_camera(self):
        from play_state import stageState
        if self.state == "MARIO":
            self.camera[X] = stageState.cameraSize[X] // 2
            self.camera[Y] = stageState.cameraSize[Y] // 2
            if self.x < stageState.cameraSize[X] // 2:  # 맵 왼편
                self.camera[X] = self.x
            if self.y < stageState.cameraSize[Y] // 2:  # 맵 아래편
                self.camera[Y] = self.y

            # 맵 오른편 위편
            if self.x > stageState.image[stageState.selectStage].w - stageState.cameraSize[X] // 2:
                self.camera[X] = stageState.cameraSize[X] - (stageState.image[stageState.selectStage].w - self.x)
            if self.y > stageState.image[stageState.selectStage].h - stageState.cameraSize[Y] // 2:
                self.camera[Y] = stageState.cameraSize[Y] - (stageState.image[stageState.selectStage].h - self.y)

    def change_motion(self, c_motion):
        self.motion = c_motion
        self.delay = 0
        self.frame = 0

    def calc_gravity(self):

        global GRAVITY
        self.y += self.gravity
        if self.gravity != -GRAVITY:
            self.gravity -= GRAVITY
            if self.gravity < -GRAVITY:
                self.gravity = -GRAVITY
        from play_state import stageState
        for rect in stageState.groundRect:
            if self.myIntersectRect(rect):
                self.y = rect.top
                if self.motion == "RIGHT_FALL" or self.motion == "LEFT_FALL":
                    self.check_fall()
        for rect in stageState.stairRect:
            if self.myIntersectRect(rect):
                self.y = rect.top
                if self.motion == "RIGHT_FALL" or self.motion == "LEFT_FALL":
                    self.check_fall()

    def check_fall(self):
        if self.motion == "RIGHT_FALL":
            self.change_motion("RIGHT_IDLE_01")
        elif self.motion == "LEFT_FALL":
            self.change_motion("LEFT_IDLE_01")


    from stage import myRect
    def myIntersectRect(self, rect = myRect(-1,0,0,0)):
        if rect.left == -1: return
        bVertical = False
        bHorizontal = False

        if self.x < rect.right and self.x+self.offset[X] > rect.left:
            bHorizontal=True

        if self.y+self.offset[Y] > rect.bottom and self.y < rect.top:
            bVertical = True

        if bVertical and bHorizontal:
            return True
        else:
            return False

    def move(self):
        self.x += self.dir[X] * self.speed
        if yoshi_motion == "RIGHT_RUN" or yoshi_motion == "LEFT_RUN":
            self.x += self.dir[X] * self.speed
        from play_state import stageState
        for rect in stageState.groundRect:
            if self.myIntersectRect(rect):
                if self.dir[X] == 1:
                    self.x = rect.left - self.offset[X]
                elif self.dir[X] == -1:
                    self.x = rect.right
        if self.x<0:
            self.x = 0
        if self.y<0:
            self.y=0

    def check_jump(self):
        global GRAVITY,MAXJUMPTIME, jump_delay
        if self.pressJump != 0:
            if self.pressJump <=MAXJUMPTIME:
                if jump_delay == 0:
                    self.gravity += GRAVITY*3
                    self.pressJump+=1
                jump_delay = (jump_delay+1) % 3
            else:
                if self.motion == "LEFT_JUMP":
                    self.change_motion("LEFT_FALL")
                elif self.motion == "RIGHT_JUMP":
                    self.change_motion("RIGHT_FALL")


