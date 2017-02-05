from microbit import *
import random

player = 2
enemy = random.randint((player - 1), (player + 1))
enemyFly = 0
score = 0
difficulty = 220
level = 1

frame1 = Image("00000:"
               "00000:"
               "00000:"
               "00000:"
               "00900")
               
frame2 = Image("00000:"
               "00000:"
               "00000:"
               "09990:"
               "00900")
 
frame3 = Image("00000:"
               "00000:"
               "99999:"
               "09990:"
               "00900") 

frame4 = Image("00000:"
               "99999:"
               "99999:"
               "09990:"
               "00900") 

frame5 = Image("99999:"
               "99999:"
               "99999:"
               "09990:"
               "00900")  
               
explosion = [frame1, frame2, frame3, frame4, frame5]

display.scroll("Level " + str(level))

while True:
    
    # causes the display to update
    display.clear()
    
    # sets up the player
    # led_x = x
    display.set_pixel(player, 4, 9)
    
    # if x is less than 0, the player cannot move out of the playfield
    if button_a.was_pressed() and player > 0:
        player = player - 1

    # if x is more than 0, the player cannot move out of the playfield
    if button_b.was_pressed() and player < 4:
        player = player + 1
        
    # init the enemy object
    if enemy == -1:
        display.set_pixel((enemy + 1), enemyFly, 5)
    elif enemy == 5:
        display.set_pixel((enemy - 1), enemyFly, 5)
    else:
        display.set_pixel(enemy, enemyFly, 5)
    
    if enemyFly < 4:
        enemyFly = enemyFly + 1
    else:
        enemyFly = 0
        enemy = random.randint((player - 1), (player + 1))
        score = score + 1
        
    if (enemy == player) and (enemyFly == 4):
        display.show(explosion, delay=200, wait=True, loop=False, clear=True)
        display.scroll("Score: " + str(score) + "  Game Over!")
        break
        
    if ((score % 11) == 0) and (score != 0):
        difficulty = difficulty - 20
        level = level + 1
        display.scroll("level " + str(level))
        score = score + 1
    
        


    sleep(difficulty)