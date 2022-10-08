from pico2d import *
import yoshi_character
X = 0
Y = 1

class StageState:
    def __init__(self):
        #카메라(화면출력) 관련
        #from main import width, height
        self.cameraPos = [0,0]
        self.cameraSize = [800,600]
        self.dir = [0,0]
        self.cameraSpeed = 5

        #이미지 관련
        self.image = [load_image("stage1.png")]

        #스테이지 구분 관련
        self.selectStage = 0

    #그리기 관련 함수
    def draw(self):
        self.image[self.selectStage].clip_draw(
            self.cameraPos[X],
            self.cameraPos[Y],
            self.cameraSize[X],
            self.cameraSize[Y],
            self.cameraSize[X]//2,
            self.cameraSize[Y]//2
        )

    #업데이트
    def update(self):
        self.cameraMove()
        pass

    def cameraMove(self):
        self.cameraPos[X] += self.dir[X]*self.cameraSpeed
        self.cameraPos[Y] += self.dir[Y]*self.cameraSpeed