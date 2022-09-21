from pico2d import *
import math

open_canvas()

player = load_image('character.png')
grass = load_image('grass.png')

player_x = 430
player_y = 90
player_radian = 270

flag_circle = True


goto = 'Right'
while(1):
    
    if flag_circle:
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(player_x,player_y)

        player_x = 400 + 210 * math.cos(player_radian / 360 * 2 * math.pi)
        player_y = 300 + 210 * math.sin(player_radian/360*2*math.pi)
        
        player_radian+=2
        if(player_radian>=360):
            player_radian-=360

        if (263<=player_radian) & (player_radian<=268):
            print(1)
            player_radian=270
            flag_circle=False
            player_x = 400
            player_y=90
            goto='Right'

        print(player_radian)
        delay(0.02)
    
    else:
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(player_x,player_y)
        if (goto == 'Right'):
            if( 380<=player_x) & (player_x<=395):
                player_x=400
                player_y=90
                flag_circle=True
                
            if(player_x+10>=800):
                player_x=800-player.w//2
                goto='Up'
            else: 
                player_x+=10
                
        elif(goto == 'Up'):
             if(player_y+10>=600):
                player_x=600-player.h//2
                goto='Left'
             else: 
                player_y+=10

        elif(goto == 'Left'):
            if(player_x-10<=0):
                player_x=player.w//2
                goto='Down'
            else: 
                player_x-=10

        elif(goto == 'Down'):
            if(player_y-10<=90):
                player_y=90
                goto='Right'
            else: 
                player_y-=10
            
        delay(0.02)
        

    
