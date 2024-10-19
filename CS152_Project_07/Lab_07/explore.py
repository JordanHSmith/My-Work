'''
Jordan Smith
11/2/21
CS 152B
This file tests basic functions of circles and windows.
To run the file type "python3 explore.py" in the terminal
'''

import graphicsPlus as gr
import random
import time

def test1():
        '''
        No parameters or return
        Tests circle in window
        '''
        window = gr.GraphWin("My First Window",500,500,False)
        point = gr.Point(100,200)
        circle = gr.Circle(point,10)
        circle.draw(window)
        window.update()
        print(window.getMouse())
        window.close()

def test2():
    '''
    No parameters or return
    Tests out multiplication of circles
    '''
    window = gr.GraphWin("My Second Window",500,500,False)
    shapes = []
    while(True):
        pos = window.checkMouse()
        if(pos != None):
            circle = gr.Circle(pos,10)
            circle.setFill("blue")
            shapes.append(circle)
            circle.draw(window)
        key = window.checkKey()
        if(key == "q"):
            break
        window.update()
        time.sleep(.033)
        for shape in shapes:
            x = random.randint(-10,10)
            y = random.randint(-10,10)
            shape.move(x,y)
    window.close()



if __name__ == "__main__":
    #test1()
    test2()
