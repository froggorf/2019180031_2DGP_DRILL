from pico2d import *
import yoshi_character
X = 0
Y = 1




class StageState:
    def __init__(self):
        #카메라(화면출력) 관련
        self.cameraPos = [0,0]
        #from main import width, height
        self.cameraSize = [1600,900]
        self.dir = [0,0]
        self.cameraSpeed = 5

        #이미지 관련
        self.image = [load_image("stage1.png")]

        #스테이지 구분 관련
        self.selectStage = 0

        #스테이지마다 다르게 갖는 변수
        groundRect = list()

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
        self.image[self.selectStage].clip_draw_to_origin

    #업데이트
    def update(self):
        self.cameraMove()
        pass

    def cameraMove(self):
        self.cameraPos[X] += self.dir[X]*self.cameraSpeed
        self.cameraPos[Y] += self.dir[Y]*self.cameraSpeed
        if self.cameraPos[X] < 0: self.cameraPos[X] = 0
        if self.cameraPos[Y] < 0: self.cameraPos[Y] = 0
        if self.cameraPos[X] + self.cameraSize[X] > self.image[self.selectStage].w: self.cameraPos[X] = self.image[self.selectStage].w - self.cameraSize[X]
        if self.cameraPos[Y] + self.cameraSize[Y] > self.image[self.selectStage].h: self.cameraPos[Y] = self.image[self.selectStage].h - self.cameraSize[Y]



class myRect:
    def __init__(self, g_left, g_bottom, g_right, g_top):
        self.left = g_left
        self.bottom = g_bottom
        self.right = g_right
        self.top = g_top

    def myIntersectRect(self, y_left, y_bottom, y_width, y_height):     #y_ = yoshi_
        bVertical = bool()
        bHorizontal = bool()

        #if self.left < y_left+y_width and self.right

    def printRect(self):
        print(self.left, " ",self.right)