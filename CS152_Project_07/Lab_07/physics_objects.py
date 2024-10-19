'''
Jordan Smith
11/2/21
CS 152B
This file creates a Ball and Block class to simulate these objects in a visual format
To run the file type "python3 physics_objects.py" in the terminal
'''

import graphicsPlus as gr
import random

class Ball:

    
    def __init__(self,win):
        '''
        Takes self and win as parameters but no return value
        Constructs a Ball object
        '''
        self.mass = 1
        self.radius = 1
        self.position = [0,0]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.win = win

        self.red_val = random.randint(0,255)
        self.green_val = random.randint(0,255)
        self.blue_val = random.randint(0,255)
        self.red_val_dir = 1
        self.green_val_dir = 1
        self.blue_val_dir = 1

        self.scale = 10
        self.vis = [gr.Circle(gr.Point(self.position[0]*self.scale, self.win.getHeight()-(self.position[1]*self.scale)), self.radius * self.scale)]

    
    def draw(self):
        '''
        Takes self as a paramter but no return value
        Draws a colored Ball object
        '''
        for item in self.vis:
            item.setFill(gr.color_rgb(self.red_val,self.green_val,self.blue_val))
            item.draw(self.win)

    
    def color(self):
        '''
        Takes self as a paramter but no return value
        Continually slightly alters the color of the ball
        '''
        #Extension
        #Changes direction of the change in color based on if it reaches the bound
            #for color values
        for item in self.vis:
            if(self.red_val >= 255 or self.red_val <= 0):
                self.red_val_dir *= -1
            if(self.green_val >= 255 or self.green_val <= 0):
                self.green_val_dir *= -1
            if(self.blue_val >= 255 or self.blue_val <= 0):
                self.blue_val_dir *= -1
            
            #Adjusts each color value by 1
            self.red_val = self.red_val + (1 * self.red_val_dir)
            self.green_val = self.green_val + (1 * self.green_val_dir)
            self.blue_val = self.blue_val + (1 * self.blue_val_dir)
            item.setFill(gr.color_rgb(self.red_val,self.green_val,self.blue_val))


    def getPosition(self):
        '''
        (self) -> (list)
        '''
        return(self.position[:])

    def setPosition(self,px,py):
        '''
        Takes self, px, and py as paramters but no return value
        Changes Position of the ball
        '''
        x_old = self.position[0]
        y_old = self.position[1]

        self.position[0] = px
        self.position[1] = py

        #Calculates the change from the old position to the new position
            #and adjust by the scale factor.
        dx = (px-x_old) * self.scale
        dy = (y_old-py) * self.scale

        for item in self.vis:
            item.move(dx,dy)

    def getVelocity(self):
        '''
        (self) -> (list)
        '''
        return(self.velocity[:])

    def setVelocity(self,vx,vy):
        '''
        Takes self, vx, and vy as paramters but no return value
        Changes the velocity of the ball
        '''
        self.velocity = [vx,vy]

    def getAcceleration(self):
        '''
        (self) -> (list)
        '''
        return(self.acceleration[:])
    
    def setAcceleration(self,ax,ay):
        '''
        Takes self, ax, and ay as paramters but no return value
        Changes the acceleration of the ball
        '''
        self.acceleration = [ax,ay]

    def getMass(self):
        '''
        (self) -> (float)
        Returns the mass of the ball
        '''
        return(self.mass)

    def setMass(self,m):
        '''
        Takes self and m as paramters but no return value
        Changes the mass of the ball
        '''
        self.mass = m

    def getRadius(self):
        '''
        (self) -> (int)
        Returns the radius of the ball
        '''
        return(self.radius)

    def update(self,dt):
        '''
        Takes self and dt as paramters but no return value
        Updates the elements related to motion for the ball
        '''
        x_old = self.position[0]
        y_old = self.position[1]

        #Updates the location of the ball
        self.position[0] = x_old + self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt
        self.position[1] = y_old + self.velocity[1]*dt + 0.5*self.acceleration[1]*dt*dt

        dx = (self.position[0] - x_old) * self.scale
        dy = -(self.position[1] - y_old) * self.scale

        for item in self.vis:
            item.move(dx,dy)

        self.velocity[0] += self.acceleration[0] * dt
        self.velocity[1] += self.acceleration[1] * dt

class Block:

    def __init__(self,win,dx,dy):
        '''
        Takes self, win, dx, and dy as paramters but no return value
        Constructs a Block object
        '''
        self.mass = 1
        self.position = [0,0]
        self.velocity = [0,0]
        self.acceleration = [0,0]
        self.win = win

        self.dx = dx
        self.dy = dy

        self.scale = 10
        self.vis = [gr.Rectangle(gr.Point(self.position[0]*self.scale, self.win.getHeight()-(self.position[1]*self.scale)),gr.Point((self.position[0]+self.dx)*self.scale, (self.win.getHeight()-(self.position[1] + self.dy)*self.scale)))]

    def draw(self):
        '''
        Takes self as a paramter but no return value
        Draws colored blocks
        '''
        for item in self.vis:
            item.setFill(gr.color_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            item.draw(self.win)

    def undraw(self):
        '''
        Takes self as a paramter but no return value
        Makes it so that the block can no longer be seen
        '''
        for item in self.vis:
            item.undraw()

    def getPosition(self):
        '''
        (self) -> (tuple)
        Returns the position of the brick
        '''
        return(tuple(self.position))

    def setPosition(self,px,py):
        '''
        Takes self, px, and py as paramters but no return value
        Moves the block to a new location
        '''
        x_old = self.position[0]
        y_old = self.position[1]

        self.position[0] = px
        self.position[1] = py

        #Calculates the change from the old position to the new position
            #and adjust by the scale factor.
        dx = (px-x_old) * self.scale
        dy = (y_old-py) * self.scale

        for item in self.vis:
            item.move(dx,dy)

    def getVelocity(self):
        '''
        (self) -> (tuple)
        Returns the velocity of the block
        '''
        return(tuple(self.velocity))

    def setVelocity(self,vx,vy):
        '''
        Takes self, vx, and vy as paramters but no return value
        Changes the block's velocity
        '''
        self.velocity = [vx,vy]

    def getAcceleration(self):
        '''
        (self) -> (tuple)
        Returns the acceleration of the block
        '''
        return(tuple(self.acceleration))
    
    def setAcceleration(self,ax,ay):
        '''
        Takes self, ax, and ay as paramters but no return value
        Change's the block's acceleration
        '''
        self.acceleration = [ax,ay]

    def getWidth(self):
        '''
        (self) -> (tuple)
        Returns the width of the block
        '''
        return(self.dx)

    def getHeight(self):
        '''
        (self) -> (tuple)
        Returns the height of the block
        '''
        return(self.dy)

    def update(self,dt):
        '''
        Takes self and dt as paramters but no return value
        Updates the elements related to motion for the ball
        '''
        x_old = self.position[0]
        y_old = self.position[1]

        #Updates the location of the brick
        self.position[0] = x_old + self.velocity[0]*dt + 0.5*self.acceleration[0]*dt*dt
        self.position[1] = y_old + self.velocity[1]*dt + 0.5*self.acceleration[1]*dt*dt

        dx = (self.position[0] - x_old) * self.scale
        dy = -(self.position[1] - y_old) * self.scale

        for item in self.vis:
            item.move(dx,dy)

        self.velocity[0] += self.acceleration[0] * dt
        self.velocity[1] += self.acceleration[1] * dt

    def collision(self, ball):
        '''
        (self,ball) -> (boolean)
        Returns whether or not the ball and the block are colliding
        '''
        ball_pos = ball.getPosition()
        ball_radius = ball.getRadius()
        rect_pos = self.getPosition()

        #Checks if any part of the ball touches any part of the block
        if(ball_pos[0] + ball_radius >= rect_pos[0] and ball_pos[0] - ball_radius <= rect_pos[0] + self.dx and ball_pos[1] + ball_radius >= rect_pos[1] and ball_pos[1] - ball_radius <= rect_pos[1] + self.dy):
            return(True)
        else:
            return(False)