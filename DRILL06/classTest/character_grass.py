from pico2d import *        #using namespace 같은것

open_canvas()

# fill here
grass = load_image('grass.png')
character= load_image('character.png')

grass.draw_now(400,30)
player_x = 0
character.draw_now(player_x,90)

'''
for i in range(10):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(player_x,90)
    player_x+=10
    delay(0.1)
'''

while(player_x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(player_x,90)
    player_x+=2
    delay(0.01)

delay(0.5)
close_canvas()
