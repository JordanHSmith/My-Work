'''
Jordan Smith
11/11/21
CS 152B
This file provides various shapes that can be animated
To run the file type "python3 physics_objects.py" in the terminal
'''

import graphicsPlus as gr
import math

class Thing():
    '''
    No inputs or return
    This is the parent class for the simulated object. It defines various variables as well as getter and setter methods.
    '''

    def __init__(self,win,the_type,x0,y0,color):
        '''
        (self,win,str,int,int,tuple) -> (None)
        Initalizes Thing
        '''
        self.type = the_type
        self.mass = 5
        self.position = [x0,y0]
        self.velocity = [2,2]
        self.acceleration = [1,1]
        self.elasticity = 1
        self.scale = 10
        self.win = win
        self.vis = []
        self.color = color
        self.drawn = False

    def getType(self):
        '''
        (self) -> (str)
        Returns the type of the shape
        '''
        return(self.type)

    def getMass(self):
        '''
        (self) -> (int)
        Returns the mass of the shape
        '''
        return(self.mass)

    def getPosition(self):
        '''
        (self) -> (list)
        Returns the position of the shape
        '''
        return(self.position)

    def getVelocity(self):
        '''
        (self) -> (list)
        Returns the velocity of the shape
        '''
        return(self.velocity)

    def getAcceleration(self):
        '''
        (self) -> (list)
        Returns the acceleration of the shape
        '''
        return(self.acceleration)

    def getElasticity(self):
        '''
        (self) -> (float)
        Returns the elasticity of the shape
        '''
        return(self.elasticity)

    def getScale(self):
        '''
        (self) -> (int)
        Returns the scale used in positioning the shapes
        '''
        return(self.scale)

    def getColor(self):
        '''
        (self) -> (tuple)
        Returns the color of the shape
        '''
        return(self.color)

    def draw(self):
        '''
        Takes self as a paramter but no return value
        Draws a shape
        '''
        for item in self.vis:
            item.draw(self.win)
        self.drawn = True

    def undraw(self):
        '''
        Takes self as a paramter but no return value
        Undraws a shape
        '''
        for item in self.vis:
            item.undraw(self.win)
        self.drawn = False

    def setMass(self,mass):
        '''
        (self,int) -> (None)
        Changes the mass of the shape
        '''
        self.mass = mass

    def setVelocity(self,vx,vy):
        '''
        (self,list) -> (None)
        Changes the velocity of the shape
        '''
        self.velocity = [vx,vy]

    def setAcceleration(self,ax,ay):
        '''
        (self,list) -> (None)
        Changes the acceleration of the shape
        '''
        self.acceleration = [ax,ay]

    def setElasticity(self,elasticity):
        '''
        (self,float) -> (None)
        Changes the elasticity of the shape
        '''
        self.elasticity = elasticity

    def setPosition(self,px,py):
        '''
        (self,int,int) -> (None)
        Changes the position of the shape
        '''
        x_old = self.position[0]
        y_old = self.position[1]

        self.position[0] = px
        self.position[1] = py

        #Calculates the change from the old position to the new position
            #and adjust by the scale factor.
        dx = (px-x_old) * self.scale
        dy = (py-y_old) * -self.scale

        for item in self.vis:
            item.move(dx,dy)

    def setColor(self,c):
        '''
        (self,tuple) -> (None)
        Changes the color of the object
        '''
        self.color = c
        if(self.color != None):
            for item in self.vis:
                item.setFill(gr.color_rgb(self.color[0],self.color[1],self.color[2]))

    def update(self,dt):
        '''
        (self,dt) -> (None)
        Updates the elements related to motion for the object
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

class Ball(Thing):
    '''
    Creates a ball
    '''
    def __init__(self,win,radius=1,x0=25,y0=25,color=(0,0,0)):
        '''
        (self,win,float,int,int,tuple) -> (None)
        Initializes the ball using Thing
        '''
        Thing.__init__(self,win,"ball",x0,y0,color)
        self.radius = radius
        self.refresh()
        self.setColor

    def refresh(self):
        '''
        (self) -> (None)
        Redraws the ball
        '''
        drawn = self.drawn
        if(drawn):
            self.undraw()
        self.vis = [gr.Circle(gr.Point(self.position[0]*self.scale, self.win.getHeight()-(self.position[1]*self.scale)), self.radius * self.scale)]

    def getRadius(self):
        '''
        (self) -> (int)
        Returns the radius of the ball
        '''
        return(self.radius)

    def setRadius(self,r):
        '''
        (self,int) -> (None)
        Changes the radius of the ball
        '''
        self.radius = r
        self.refresh()

class Block(Thing):
    '''
    Creates a block
    '''
    def __init__(self, win,x0=0,y0=0,width=2,height=1, color=(0,0,0)):
        '''
        (self,win,int,int,float,float,tuple) -> (None)
        Initializes the block using Thing
        '''
        Thing.__init__(self,win,"block",x0,y0,color)
        self.width = width
        self.height = height
        
        self.reshape()
        self.setColor(color)

    def reshape(self):
        '''
        (self) -> (None)
        Redraws the block
        '''
        drawn = self.drawn
        for item in self.vis:
            if(drawn):
                item.undraw(self.win)
        # self.vis = [gr.Rectangle(gr.Point((self.position[0]*self.scale)-(self.width/2*self.scale),self.win.getHeight()-(self.position[1]*self.scale)-(self.height/2)*self.scale),gr.Point((self.position[0]*self.scale)+(self.width/2*self.scale),self.win.getHeight()-(self.position[1]*self.scale)+(self.height*self.scale)))]
        self.vis = [gr.Rectangle(gr.Point((self.position[0] - self.width/2) * self.scale, self.win.getHeight() - (self.position[1] - self.height/2) * self.scale), gr.Point((self.position[0] + self.width/2) * self.scale, self.win.getHeight() - (self.position[1] + self.height/2) * self.scale))]
        if(drawn):
            item.draw(self.win)

    def getWidth(self):
        '''
        (self) -> (int)
        Returns the width of the block
        '''
        return(self.width)

    def getHeight(self):
        '''
        (self) -> (int)
        Returns the height of the block
        '''
        return(self.height)

    def setWidth(self,width):
        '''
        (self,int) -> (None)
        Changes the width of the block
        '''
        self.width = width
        self.reshape()

    def setHeight(self,height):
        '''
        (self,int) -> (None)
        Changes the height of the block
        '''
        self.height = height
        self.reshape()

class Triangle(Thing):
    '''
    Creates a triangle
    '''
    def __init__(self, win, radius = 1, x0=25, y0=25, color=None):
        '''
        (self,win,float,int,int,tuple) -> (None)
        Initializes the triangle using Thing
        '''
        Thing.__init__(self,win, "triangle", x0, y0, color)
        self.radius = radius
        self.reshape()
        self.setColor(color)

    def reshape(self):
        '''
        (self) -> (None)
        Redraws the triangle
        '''
        self.vis = [gr.Polygon(gr.Point((self.position[0]*self.scale),self.win.getHeight()-((self.position[1]*self.scale)-(self.radius*self.scale))),gr.Point((self.position[0]*self.scale)+((self.radius/2)*math.sqrt(3)*self.scale),self.win.getHeight()-(self.position[1]*self.scale)-((self.radius/2)*self.scale)),gr.Point((self.position[0]*self.scale)-(((self.radius/2)*math.sqrt(3))*self.scale),self.win.getHeight()-(self.position[1]*self.scale)-((self.radius/2)*self.scale)))]

    def getRadius(self):
        '''
        (self) -> (int)
        Returns the triangle's radius that is used for collision detection
        '''
        return(self.radius)

    def setRadius(self,r):
        '''
        (self,int) -> (None)
        Changes the triangle's radius that is used for collison detection
        '''
        self.radius = r
        self.reshape()

class Bird(Thing):
    '''
    Creates a bird
    '''
    def __init__(self, win, radius = 1, x0=25, y0=25, color=None):
        '''
        (self,win,float,int,int,tuple) -> (None)
        Initializes the bird using Thing
        '''
        Thing.__init__(self,win, "bird", x0, y0, color)
        self.radius = radius
        self.reshape()
        self.setColor(color)

    def reshape(self):
        '''
        (self) -> (None)
        Redraws the bird
        '''
        body = gr.Circle(gr.Point(self.position[0]*self.scale, self.win.getHeight()-(self.position[1]*self.scale)), self.radius * self.scale)
        wing = gr.Polygon(gr.Point((self.position[0]*self.scale+(self.radius*2/3*self.scale)),self.win.getHeight()-((self.position[1]*self.scale)-(self.radius*self.scale)+(self.radius*1/3*self.scale))),gr.Point((self.position[0]*self.scale)+((self.radius/2)*math.sqrt(3)*self.scale)+(self.radius*2/3*self.scale),self.win.getHeight()-(self.position[1]*self.scale)-((self.radius/2)*self.scale)+(self.radius*1/3*self.scale)),gr.Point((self.position[0]*self.scale)-(((self.radius/2)*math.sqrt(3))*self.scale)+(self.radius*2/3*self.scale),self.win.getHeight()-(self.position[1]*self.scale)-((self.radius/2)*self.scale)+(self.radius*1/3*self.scale)))
        self.vis = [body,wing]

    def getRadius(self):
        '''
        (self) -> (int)
        Returns the radius of the bird
        '''
        return(self.radius)

    def setRadius(self,r):
        '''
        (self,int) -> (None)
        Changes the radius of the bird
        '''
        self.radius = r
        self.reshape()


class Spear(Thing):
    '''
    Creates a spear
    '''
    def __init__(self, win, radius=1, x0=0, y0=0, color=(0,0,0)):
        '''
        (self,win,float,int,int,tuple) -> (None)
        Initializes the spear using Thing
        '''
        Thing.__init__(self,win,"spear",x0,y0,color)
        self.radius = radius
        
        self.reshape()
        self.setColor(color)
    
    def reshape(self):
        '''
        (self) -> (None)
        Redraws the block
        '''
        drawn = self.drawn
        for item in self.vis:
            if(drawn):
                item.undraw(self.win)
        handle = gr.Rectangle(gr.Point((self.position[0]*self.scale)-(self.radius/4*self.scale),self.win.getHeight()-(self.position[1]*self.scale)-(self.radius/1.2)*self.scale),gr.Point((self.position[0]*self.scale)+(self.radius/4*self.scale),self.win.getHeight()-(self.position[1]*self.scale)+(self.radius*self.scale)))
        tip = gr.Polygon(gr.Point((self.position[0]*self.scale+(self.radius*2/3*self.scale))-(self.radius*.65*self.scale),self.win.getHeight()-((self.position[1]*self.scale)-(self.radius*self.scale)+(self.radius*1/3*self.scale)+20*self.radius)),gr.Point((self.position[0]*self.scale)+((self.radius/2)*math.sqrt(3)*self.scale)+(self.radius*2/3*self.scale)-(self.radius*.65*self.scale),self.win.getHeight()-(self.position[1]*self.scale)-((self.radius/2)*self.scale)+(self.radius*1/3*self.scale)),gr.Point((self.position[0]*self.scale)-(((self.radius/2)*math.sqrt(3))*self.scale)+(self.radius*2/3*self.scale)-(self.radius*.65*self.scale),self.win.getHeight()-(self.position[1]*self.scale)-((self.radius/2)*self.scale)+(self.radius*1/3*self.scale)))
        self.vis = [handle,tip]
        if(drawn):
            item.draw(self.win)

    def getRadius(self):
        '''
        (self) -> (None)
        Returns the radius used for collision detection for the spear
        '''
        return(self.radius)