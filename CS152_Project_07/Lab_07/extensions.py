'''
Jordan Smith
11/2/21
CS 152B
This file creates a perimeter of multi-colored blocks in which a color-changing ball bounces.
    The color of the blocks is also changed if it is hit by the ball.
To run the file type "python3 extensions.py" in the terminal
'''

import graphicsPlus as gr
import physics_objects as pho
import random
import time


def main():
        drawing = False

        #Creates a graphics window
        win = gr.GraphWin("Falling", 500, 500, False)
        my_ball = pho.Ball(win)

        #Prepares the block setup
        block1 = pho.Block(win,3,20)
        block2 = pho.Block(win,3,20)
        block3 = pho.Block(win,3,20)
        block4 = pho.Block(win,3,20)
        block5 = pho.Block(win,41.8,3)
        block6 = pho.Block(win,41.8,3)

        block1.setPosition(1,0.1)
        block2.setPosition(1,30)
        block3.setPosition(46,0.1)
        block4.setPosition(46,30)
        block5.setPosition(4.1,46)
        block6.setPosition(4.1,1)

        block1.draw()
        block2.draw()
        block3.draw()
        block4.draw()
        block5.draw()
        block6.draw()

        while True:
            if(win.checkKey() == "space"):
                #Creates ball when space bar clicked and let's the program know the ball is being drawn
                my_ball.draw()
                drawing = True
                my_ball.setPosition(25,25)

                #assigns random values for the magnitude and direction of the velocity
                x_vel = random.random()
                y_vel = random.random()
                rand_dir_list = [-1, 1]
                x_dir = random.choice(rand_dir_list)
                y_dir = random.choice(rand_dir_list)

                my_ball.setVelocity(x_vel*x_dir,y_vel*y_dir) 

                #Makes it so that x and y accelerations are the same but in same direction as velocity
                rand_nums = random.random()
                my_ball.setAcceleration(rand_nums*x_dir,rand_nums*y_dir)

            #Changes color of ball
            if(drawing):
                my_ball.color()

            my_ball.update(.033)
            
            time.sleep( 0.033 )

            if win.checkKey() == 'q':
                break
            
            if win.checkMouse():
                break

            #Flips the direction of the ball if it hits a block
            if(block1.collision(my_ball) == True or block2.collision(my_ball) == True
            or block3.collision(my_ball) == True or block4.collision(my_ball) == True):
                ball_vel = my_ball.getVelocity()
                my_ball.setVelocity(-ball_vel[0],ball_vel[1])
                ball_acc = my_ball.getAcceleration()
                my_ball.setAcceleration(-ball_acc[0],ball_acc[1])

                #Extension
                #Changes color of the blocks if hit
                ball_pos = my_ball.getPosition()
                if(block1.collision(my_ball) == True and ball_pos[0] != 0):
                    block1.undraw()
                    block1.draw()

                if(block2.collision(my_ball) == True):
                    block2.undraw()
                    block2.draw()

                if(block3.collision(my_ball) == True):
                    block3.undraw()
                    block3.draw()

                if(block4.collision(my_ball) == True):
                    block4.undraw()
                    block4.draw()

            elif(block5.collision(my_ball) == True or block6.collision(my_ball) == True):
                ball_vel = my_ball.getVelocity()
                my_ball.setVelocity(ball_vel[0],-ball_vel[1])
                ball_acc = my_ball.getAcceleration()
                my_ball.setAcceleration(ball_acc[0],-ball_acc[1])

                #Extension
                #Changes color of the blocks if hit
                if(block5.collision(my_ball) == True):
                    block5.undraw()
                    block5.draw()

                if(block6.collision(my_ball) == True):
                    block6.undraw()
                    block6.draw()
            
        win.close()

if __name__ == "__main__":
    main()