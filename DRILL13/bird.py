import random
from pico2d import *
import game_framework

PIXEL_PER_METER = (1.0/0.03)
FLY_SPEED_KPH = 40
FLY_SPEED_MPM = FLY_SPEED_KPH * 1000.0 / 60
FLY_SPEED_MPS = FLY_SPEED_MPM / 60.0
FLY_SPEED_PPS = FLY_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    size = [60,60]
    def __init__(self):
        self.x, self.y = random.randint(Bird.size[0],300), random.randint(get_canvas_height()-350,get_canvas_height()-Bird.size[1])
        self.frame = random.randint(0,FRAMES_PER_ACTION-1)
        self.face_dir = 1
        self.image = load_image('bird_animation.png')



    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.face_dir* FLY_SPEED_PPS * game_framework.frame_time
        if self.x + Bird.size[0]//2 > get_canvas_width():
            self.x = get_canvas_width()-Bird.size[0]//2
            self.face_dir=-1
        elif self.x-Bird.size[0]//2<0:
            self.x = Bird.size[0]//2
            self.face_dir= 1

    def draw(self):
        if self.face_dir == 1:  #오른쪽
            self.image.clip_draw(int(self.frame) * 180, 506-180, 180, 180, self.x, self.y,Bird.size[0],Bird.size[1])
        elif self.face_dir == -1:    #왼쪽
            self.image.clip_composite_draw(int(self.frame) * 180, 506-180, 180, 180,0,'h', self.x, self.y,Bird.size[0],Bird.size[1])



