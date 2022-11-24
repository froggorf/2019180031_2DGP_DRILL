from pico2d import *
import game_world
import server


class Ball:
    image = None
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = [21,21]

        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')

    def draw(self):
        bx = self.x - server.background.window_left
        by = self.y - server.background.window_bottom
        Ball.image.draw(bx,by)
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        if group == 'boy:balls':
            game_world.remove_object(self)

    def update(self):
        pass