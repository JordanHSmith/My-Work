# Bruce A. Maxwell
# Fall 2015
# CS 151S Project 10
#
# third test function for RotatingBlock, testing collisions
#
# Updated for Python3 by Caitrin Eaton
# 15 November 2017
#
# Modified by Eric Aaron, Fall 2018, Spring 2019
# Modified by Bruce Maxwell, Fall 2019

import graphicsPlus as gr
import new_physics_objects as pho
import new_collision as coll
import math
import time

            
def test():
    # Create a window, rotating block, and ball
    win = gr.GraphWin('rotator', 500, 500, False)

    block = pho.RotatingBlock(win, 25, 25, 20, 10)
    block.draw()
    block.setRotVelocity(108)

    ball = pho.Ball(win)
    ball.setPosition(30, 45)
    ball.setAcceleration(0, -10)
    ball.draw()


    block2 = pho.RotatingBlock(win, 40, 40, 10, 5)
    block2.draw()
    block2.setRotVelocity(64)

    block3 = pho.RotatingBlock(win, 10, 35, 5, 10)
    block3.draw()
    block3.setRotVelocity(146)

    # execute an update loop, checking for collisions
    dt = 0.02
    for i in range(400):
        block.update(dt)
        block2.update(dt)
        block3.update(dt)
        
        if coll.collision(ball, block, dt) or coll.collision(ball, block2, dt) or coll.collision(ball, block3, dt):
            print('collision')
        else:
            ball.update(dt)

        if i % 10:
            win.update()
            time.sleep(0.01)
            
        if win.checkMouse() != None:
            break

    # wait for a mouse click to quit
    win.getMouse()
    win.close()

if __name__ == "__main__":
    test()
    
