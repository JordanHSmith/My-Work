'''
Jordan Smith
11/23/21
CS 152B
This file creates a scene with multiple balls and rotating blocks
To run the file type "python3 extension.py" in the terminal
'''

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


    block2 = pho.RotatingBlock(win, 40, 40, 10, 5)
    block2.draw()
    block2.setRotVelocity(64)

    block3 = pho.RotatingBlock(win, 10, 35, 5, 10)
    block3.draw()
    block3.setRotVelocity(146)

    ball = pho.Ball(win)
    ball.setPosition(10, 45)
    ball.setAcceleration(0, -10)
    ball.draw()

    ball2 = pho.Ball(win)
    ball2.setPosition(30, 45)
    ball2.setAcceleration(-10, -3)
    ball2.draw()

    ball3 = pho.Ball(win)
    ball3.setPosition(10, -10)
    ball3.setAcceleration(0, 10)
    ball3.draw()

    ball4 = pho.Ball(win)
    ball4.setPosition(-5, 25)
    ball4.setAcceleration(10, 0)
    ball4.draw()

    ball5 = pho.Ball(win)
    ball5.setPosition(-5, 10)
    ball5.setAcceleration(10, 10)
    ball5.draw()

    # execute an update loop, checking for collisions
    dt = 0.02
    for i in range(400):
        block.update(dt)
        block2.update(dt)
        block3.update(dt)
        
        #Expanded collision detection for ball on ball collisions
        if coll.collision(ball, block, dt) or coll.collision(ball, block2, dt) or coll.collision(ball, block3, dt) or coll.collision(ball, ball2, dt) or coll.collision(ball, ball3, dt) or coll.collision(ball, ball4, dt) or coll.collision(ball, ball5, dt):
            print('collision')
        else:
            ball.update(dt)

        if coll.collision(ball2, block, dt) or coll.collision(ball2, block2, dt) or coll.collision(ball2, block3, dt) or coll.collision(ball2, ball, dt) or coll.collision(ball2, ball3, dt) or coll.collision(ball2, ball4, dt) or coll.collision(ball2, ball5, dt):
            print('collision')
        else:
            ball2.update(dt)

        if coll.collision(ball3, block, dt) or coll.collision(ball3, block2, dt) or coll.collision(ball3, block3, dt) or coll.collision(ball3, ball, dt) or coll.collision(ball3, ball2, dt) or coll.collision(ball3, ball4, dt) or coll.collision(ball3, ball5, dt):
            print('collision')
        else:
            ball3.update(dt)

        if coll.collision(ball4, block, dt) or coll.collision(ball4, block2, dt) or coll.collision(ball4, block3, dt) or coll.collision(ball4, ball, dt) or coll.collision(ball4, ball2, dt) or coll.collision(ball4, ball3, dt) or coll.collision(ball, ball5, dt):
            print('collision')
        else:
            ball4.update(dt)

        if coll.collision(ball5, block, dt) or coll.collision(ball5, block2, dt) or coll.collision(ball5, block3, dt) or coll.collision(ball5, ball, dt) or coll.collision(ball5, ball2, dt) or coll.collision(ball5, ball3, dt) or coll.collision(ball5, ball4, dt):
            print('collision')
        else:
            ball5.update(dt)

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