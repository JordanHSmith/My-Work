'''
Jordan Smith
12/10/2021
CS 152B
To run the program, type "python3 line.py" into the terminal
'''

import graphicsPlus as gr
import math
import time

class RotatingLine():
    def __init__(self, win, x0, y0, length, Ax = None, Ay = None):
        self.pos = [x0,y0]
        length = length
        if(Ax != None and Ay != None):
            self.anchor = [Ax,Ay]
        else:
            self.anchor = [x0,y0]
        #self.points = [[-length/2.0,0.0],[length/2.0,0.0]]
        self.points = [[0.0,0.0],[length,0.0]]
        self.angle = 0.0
        self.rvel = 0.0
        self.win = win
        self.scale = 10
        self.vis = []
        self.drawn = False

        self.refresh()

    def render(self):
        theta = self.angle*math.pi / 180.0
        cth = math.cos(theta)
        sth = math.sin(theta)
        pts = []
        for vertex in self.points:
            x = self.pos[0] + vertex[0] - self.anchor[0]
            y = self.pos[1] + vertex[1] - self.anchor[1]
            xt = x * cth - y * sth
            yt = x * sth + y * cth
            x = self.anchor[0] + xt
            y = self.anchor[0] + yt
            pts.append(gr.Point(self.scale * x, self.win.getHeight() - self.scale * y))
        
        self.vis = [gr.Line(pts[0],pts[1])]

    def draw(self):
        for shape in self.vis:
            shape.draw(self.win)
            self.drawn = True
    
    def undraw(self):
        for shape in self.vis:
            shape.undraw()
            self.drawn = False

    def refresh(self):
        drawn = self.drawn
        if(drawn):
            self.undraw()
        self.render()
        if(drawn):
            self.draw()

    def getAngle(self):
        return(self.angle)

    def setAngle(self,angle):
        self.angle = angle
        self.refresh()

    def rotate(self,add_angle):
        self.angle += add_angle
        self.refresh()

    def getPoints(self):
        return self.points

    
def test1():
    win = gr.GraphWin('line thingy', 500, 500, False)

    line = RotatingLine(win, 25, 25, 10,20,25)
    line.draw()

    while win.checkMouse() == None:
        line.rotate(3)
        time.sleep(0.08)
        win.update()

    win.getMouse()
    win.close()

if __name__ == "__main__":
    test1()
