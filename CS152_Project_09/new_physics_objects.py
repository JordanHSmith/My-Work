'''
Jordan Smith
11/23/21
CS 152B
This file creates various shapes, including one that can rotate
To run the file type "python3 new_physics_objects.py" in the terminal
'''

import graphicsPlus as gr
import new_collision as coll
import math
import time

#The thing class is a parent for all simulated objects
class Thing:
	def __init__(self,win,the_type):
		self.type = the_type
		self.win = win
		self.mass = 10
		self.scale = 10
		#start in the middle of the screen
		self.position = [win.getWidth()/(2*self.scale),win.getHeight()/(2*self.scale)]
		self.velocity = [0,0]
		self.acceleration = [0,0]
		self.elasticity = 1
		#list of the Zelle graphics that make up an obj
		self.vis = []
		#rgb tuple for color
		self.color  = (0,0,0)
		self.drawn = False

	def getType(self):
		return self.type
	def getMass(self): # Returns the mass of the object as a scalar value
		return self.mass
	def getScale(self):
		return self.scale
	def getPosition(self): # returns a 2-element tuple with the x, y position.
		return (self.position[0],self.position[1])
	def getVelocity(self): # returns a 2-element tuple with the x and y velocities.
		return (self.velocity[0],self.velocity[1])
	def getAcceleration(self): # returns a 2-element tuple with the x and y acceleration values.
		return (self.acceleration[0],self.acceleration[1])
	def getElasticity(self):#returns a scalar value for elasticity
		return self.elasticity
	def getColor(self):#returns a tuple for rgb color
		return self.color		
	
	def draw(self):
		for item in self.vis:
			item.draw(self.win)
		self.drawn = True
	def undraw(self):
		for item in self.vis:
			item.undraw()
		self.drawn = False

	def setMass(self, m): # m is the new mass of the object
		self.mass = m
	def setVelocity(self, vx, vy): # vx and vy are the new x and y velocities
		self.velocity[0] = vx
		self.velocity[1] = vy
	def setAcceleration(self, ax, ay): # ax and ay are new x and y accelerations.
		self.acceleration[0] = ax
		self.acceleration[1] = ay

	def setElasticity(self, elasticity):
		self.elasticity = elasticity

	def setPosition(self,px,py):

		dx = px - self.position[0]
		dy = py - self.position[1]
		self.position[0] = px
		self.position[1] = py
		dx = dx*self.scale
		dy = dy*self.scale*(-1)			
		for item in self.vis:
			item.move(dx,dy)

	def setColor(self,c):  # takes in an (r, g, b) tuple
		self.color  = c 
		if self.color != None:
			for item in self.vis: 
				item.setFill(gr.color_rgb(c[0],c[1],c[2]))

	def update(self,dt):
		oldx = self.position[0]
		oldy = self.position[1]
		# update the x position using x_new = x_old + x_vel*dt + 0.5*x_acc * dt*dt
		self.position[0] = self.position[0]+self.velocity[0]*dt + .5*self.acceleration[0]*dt**2
		# update the y position using y_new = y_old + y_vel*dt + 0.5*y_acc * dt*dt 
		self.position[1] = self.position[1]+self.velocity[1]*dt + .5*self.acceleration[1]*dt**2
		# assign to dx the change in the x position times the scale factor (self.scale)
		dx = (self.position[0] - oldx)*self.scale
		# assign to dy the negative of the change in the y position times the scale factor (self.scale)
		dy = (self.position[1]- oldy)*-self.scale
		# for each item in self.vis
		# call the move method of the graphics object with dx and dy as arguments..
		for item in self.vis:
			item.move(dx,dy)
       # update the x velocity by adding the acceleration times dt to its old value
		self.velocity[0] += self.acceleration[0]*dt
       # update the y velocity by adding the acceleration times dt to its old value
		self.velocity[1] += self.acceleration[1]*dt

#define fuctionality for a ball
class Ball(Thing):
	#construct a ball
	def __init__(self,win,radius = 1, x0 = 0, y0 =0,color = (0,0,0)):
		
		Thing.__init__(self, win, "ball")

		self.radius = radius 
		self.refresh()
		self.setColor(color)
	#update the scene and draw the ball only if appropriate
	def refresh(self):
		if self.drawn:
		# if the object is drawn 
			self.undraw()
		#     undraw the object (use self.undraw())

		# define the self.vis list of graphics objects using the current position, radius, and window
		self.vis = [ gr.Circle( gr.Point(self.position[0]*self.scale, 
                                 self.win.getHeight()-self.position[1]*self.scale), 
                        self.radius * self.scale ) ]

		if self.drawn:
		# if the object is drawn 
			self.draw()
		#     draw the object
	#get the properties of a balle
	def getRadius(self):
		return self.radius	
	#set the property of a ball	
	def setRadius(self,r):
		self.radius = r
		self.refresh()	

#define the functionality of a block
class Block(Thing):
	def __init__(self, win, x0 = 0, y0 = 0, dx=2, dy=1, color=None):
		#use thing's constructor
		Thing.__init__(self,win,"block")
		#set the position of the block 
		self.setPosition(x0,y0)
		#set the demensions of the box
		self.dx = dx
		self.dy = dy
		#set color and then create the vis list w/ reshape
		self.setColor(color)	
		self.reshape()
	
	def reshape(self):
		#undraw the obj if it is drawn
		if self.drawn:
			self.undraw()
		x0 = self.getPosition()[0]
		y0 = self.getPosition()[1]
		upperCorn = gr.Point(x0*self.scale-self.dx*self.scale/2, self.win.getHeight()-y0*self.scale-self.dy*self.scale/2)
		lowerCorn = gr.Point(x0*self.scale+self.dx*self.scale/2, self.win.getHeight()- y0*self.scale+self.dy*self.scale/2)	
		self.vis = [gr.Rectangle(upperCorn,lowerCorn)]

		if self.drawn:
		# if the object is drawn 
			self.draw()
		#     draw the object
	def getWidth(self):
		return self.dx
	def getHeight(self):
		return self.dy
	def setWidth(self,width):
		self.dx = width
		self.reshape()
	def setHeight(self,height):
		self.dy = height
		self.reshape()


############ Task 1 #############

#defines the functionality of a rotating block
class RotatingBlock(Thing):
	"""Rotating block is a rectangular object that spins around a given axis of rotation"""
	def __init__(self,win, x0 = 0, y0 = 0, height = 1, width = 1, Ax = None, Ay = None,color = (100,0,0)):
		#Uses Thing to help initialize a rotating block object
		Thing.__init__(self,win,"rotating block")
		self.width = width
		self.height = height
		self.position = [x0,y0]
		#creates a list of the block's vertices
		self.points = [[-width/2,-height/2],[width/2,-height/2],[width/2,height/2],[-width/2,height/2]]
		self.angle = 0.0
		self.rvel = 0.0
		self.drawn = False
		self.color = color
		#sets the anchor point to the center of the block if no anchor poiint is given
		if(Ax != None and Ay != None):
			self.anchor = [Ax,Ay]
		else:
			self.anchor = [x0,y0]


	############ Task 2 #############

	def refresh(self):
		'''
		(self) -> (None)
		redraws the rotating block
		'''
		drawn = self.drawn
		if(drawn):
			self.undraw()
		self.render()
		if(drawn):
			self.draw()

	"""return the angle"""		
	def getAngle(self):
		'''(self) -> (float)'''
		return self.angle
	
	"""set the angle to a new value and refresh the shapes"""
	def setAngle(self, angle):
		'''(self,float) -> (None)'''
		self.angle = angle

	"""increment angle with a specific value and move the shapes"""
	def rotate(self, angleToMove):
		'''(self,float) -> (None)'''
		self.angle += angleToMove
		self.refresh()

	"""set a new anchor point"""
	def setAnchor(self, Ax, Ay):
		'''(self,int,int) -> (None)'''
		self.anchor = [Ax,Ay]

	"""return the anchor point"""
	def getAnchor(self):
		'''(self) -> (list)'''
		return self.anchor

	'''return the rotational velocity'''
	def getRotVelocity(self):
		'''(self) -> (float)'''
		return self.rvel
	
	'''set the rotational velocity'''
	def setRotVelocity(self,rotVel):
		'''(self,float) -> (None)'''
		self.rvel = rotVel

############ Task 3 #############

#### Provided for you!###########
	def render(self):
		#converts degrees to radians
		theta  = self.angle*math.pi/180.0
		cth = math.cos(theta)
		sth = math.sin(theta)
		pts = []
		
		#Adjusts the position of the vertices of the rotating block
		for vertex in self.points:
		  x = vertex[0]+self.getPosition()[0] - self.anchor[0]
		  y = vertex[1]+self.getPosition()[1] - self.anchor[1]

		  xt = x*cth - y*sth
		  yt = x*sth+ y*cth
		  x = xt + self.anchor[0]
		  y = yt + self.anchor[1]

		  pts.append(gr.Point(self.scale*x,self.win.getHeight()-self.scale*y))
		 
		#defines the block as a polygon wiith four vertices
		self.vis  = [gr.Polygon(pts[0],pts[1], pts[2], pts[3])]

	"""alter the angular velocity"""
	def setRotVelocity(self,value):
		'''(self,float) -> (None)'''
		self.rvel = value
		self.refresh()
		
	"""return the angular velocity"""
	def getRotVelocity(self):
		'''(self) -> (float)'''
		return self.rvel

############ Task 4 #############

	'''rotates block in accordance with the time step'''
	def update(self,dt):
		'''(self,float) -> (None)'''
		da = self.rvel*dt
		if(da != 0):
			self.rotate(da)
			Thing.update(self,dt)

