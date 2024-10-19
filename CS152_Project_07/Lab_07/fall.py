# template written by Bruce A. Maxwell
# updated by <your name here>
# Fall 2019
# CS 152
# Project 8

import graphicsPlus as gr
import physics_objects as pho
import random
import time

# main function for implementing the test code
def main():

        # create a graphics window
        win = gr.GraphWin("Falling", 500, 500, False)

        # create a ball
        my_ball = pho.Ball(win)

        # move it to the center of the screen and draw it
        my_ball.setPosition(25,25)
        my_ball.draw()

        # give it a random velocity
        my_ball.setVelocity(random.random(),random.random())

        # set the acceleration to (0, -20)
        my_ball.setAcceleration(0,-20)

        #Block additions
        block1 = pho.Block(win,6,3)
        block2 = pho.Block(win,6,3)
        block3 = pho.Block(win,6,3)

        block1.setPosition(22,10)
        block2.setPosition(20,20)
        block3.setPosition(25,15)

        block1.draw()
        block2.draw()
        block3.draw()

        while True:
            # call the ball's update method with a dt of 0.033
            my_ball.update(.033)
            block1.update(.033)
            block2.update(.033)
            block3.update(.033)
            
            time.sleep( 0.033 ) # have the animation go at the same speed

            if win.checkKey() == 'q': # did the user type a 'q'?
                break
            
            if win.checkMouse(): # did the user click the mouse?
                break

            # if the ball is outside the window
            # reposition the ball to the center of the window
            # give it a random velocity

            ball_pos = my_ball.getPosition()
            if(ball_pos[0] > win.getWidth() or ball_pos[0] < 0 or ball_pos[1] > win.getHeight() or ball_pos[1] < 0):
                my_ball.setPosition(25,25)
                my_ball.setVelocity(random.random(),random.random())
            
            #Block collision check
            if(block1.collision(my_ball) == True):
                block1.undraw()
                block1.setPosition(100,100)
            if(block2.collision(my_ball) == True):
                block2.undraw()
                block2.setPosition(100,100)
            if(block3.collision(my_ball) == True):
                block3.undraw()
                block3.setPosition(100,100)

        win.close()

if __name__ == "__main__":
    main()