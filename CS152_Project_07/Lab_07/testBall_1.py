# Bruce A. Maxwell
# Fall 2015
# CS 151S Project 8
#
# Physics simulation project
# Test file for the Ball class
#
# modified Spring '19 by Eric Aaron

# test the get/set methods
# test the setPosition method
#
import graphicsPlus as gr
import physics_objects as pho
import time
import random

def main():

        # creates a GraphWin
        win = gr.GraphWin( "Ball test", 500, 500, False)

        # creates a default Ball object and draws it into the window
        ball = pho.Ball(win)
        p = ball.getPosition()
        print( 'Position:', p[0], p[1])

        v = ball.getVelocity()
        print( 'Velocity:', v[0], v[1])

        ball.setVelocity( 10, 10 )
        
        v = ball.getVelocity()
        print( 'New Velocity:', v[0], v[1])

        #additional test for function
        ball.setAcceleration(2,2)
        a = ball.getAcceleration()
        print( 'New Acceleration:', a[0], a[1])

        print( 'Velocity:', v[0], v[1])

        ball.setMass(15)
        m = ball.getMass()
        print("New Mass:", m)

        p = ball.getPosition()
        print( 'Position:', p[0], p[1])

        r = ball.getRadius()
        print( 'Radius:', r)
        
        
        # moves the ball to the center of the screen
        ball.setPosition( 25, 25 )
        p = ball.getPosition()
        print( 'New Position:', p[0], p[1])

        
        ball.draw()

        #Makes the ball move
        dt = 0.1
        while win.checkMouse() == None:
            ball.update(dt)
            time.sleep(dt)
            ball.setVelocity( random.randint(-10,10), random.randint(-10,10) )
            win.update()

        win.getMouse()
        win.close()


if __name__ == "__main__":
	main()