'''
Jordan Smith
12/10/2021
CS 152B
Final Project
The file simulates a game of roulette.
To run the file type "python3 roulette.py" in the terminal
'''

import graphicsPlus as gr
import new_physics_objects as pho
import line
import random
import math


def makeBackground(win):
    '''
    (win) -> (None)
    Creates a green background
    '''
    background = pho.Block(win,win.getWidth()/20,win.getHeight()/20,win.getWidth()/10,win.getHeight()/10)
    background.setColor((8,116,60))
    background.draw()


def makeDividers(win):
    '''
    (win) -> (None)
    Sets up dividing lines for different parts of the screen
    '''
    horizontal_line = gr.Line(gr.Point(0,win.getHeight()/2),gr.Point(win.getWidth(),win.getHeight()/2))
    horizontal_line.draw(win)
    vertical_line = gr.Line(gr.Point(win.getWidth()/2,0),gr.Point(win.getWidth()/2,win.getHeight()/2))
    vertical_line.draw(win)


class Text:
    '''
    This class provides function to help display text on the screen
    '''
    def __init__(self,win,x,y,str,size = 30,color = "black"):
        '''
        (self,win,float,float,string,float,string) -> (None)
        Constructor for Text
        '''
        self.win = win
        self.x = x
        self.y = y
        self.str = str
        self.size = size
        self.color = color
        self.scale = 10
        self.isDisplayed = False
        self.text = gr.Text(gr.Point(self.x*scale,(self.win.getHeight()-(self.y*scale))),self.str)
    

    def displayText(self):
        '''
        (self) -> (None)
        Shows text on screen
        '''
        self.text.setSize(self.size)
        self.text.draw(self.win)
        self.text.setTextColor(self.color)
        self.isDisplayed = True


    def undrawText(self):
        '''
        (self) -> (None)
        Gets rid of the text on the screen
        '''
        self.text.undraw()


    def getIsDisplaying(self):
        '''
        (self) -> (boolean)
        Returns if the text is being displayed
        '''
        return self.isDisplayed


class RouletteWheel:
    '''
    This class allows one to animate and simulate a roulette wheel
    '''
    def __init__(self,win,radius,wheel_pos):
        '''
        (self,win,int,list) -> (None)
        Constructor for RouletteWheel
        '''
        self.win = win
        self.radius = radius
        self.wheel_pos = wheel_pos
        self.color = (0,0,0)
        self.wheel_lines = []
        self.squares = []


    def makeWheel(self):
        '''
        (self) -> (None)
        Creates and displays roulette wheel
        '''
        #creates main wheel
        outside_wheel = pho.Ball(self.win,self.radius,self.wheel_pos[0],self.wheel_pos[1],(255,255,255))
        outside_wheel.draw()

        #draws lines that seperate numbers on roulette wheel
        self.wheel_lines = self.getWheelLines()

        #Assigns numbers to each section of the wheel
        for i in range(37):
            self.wheel_lines[i].draw()

        #covers lines with a smaller circle
        inside_wheel = pho.Ball(self.win,(3/4) * self.radius,self.wheel_pos[0],self.wheel_pos[1],(76,36,0))
        inside_wheel.draw()
        

    def getWheelLines(self,wheel_lines = []):
        '''
        (self,list) -> (list)
        Returns list of line graphics objects
        '''
        for i in range(37):
            new_line = line.RotatingLine(self.win,self.wheel_pos[0],self.wheel_pos[1],self.radius)
            wheel_lines.append(new_line)
            wheel_lines[i].rotate((360/37)*i) 
        return wheel_lines


    def drawWheelSquares(self):
        '''
        (self) -> (None)
        Creates and displays squares of the roulette wheel
        '''
        for i in range(37):
            self.squares.append(pho.SpecialRotatingBlock(self.win,self.wheel_pos[0] - self.wheel_lines[i].getPoints()[1][0],self.wheel_pos[1] - self.wheel_lines[i].getPoints()[1][1],2,4,self.wheel_pos[0],self.wheel_pos[1]))
            self.squares[i].rotate((360/37)*i)
            #Makes squares red, black, or green appropriately
            if i > 0:
                if i % 2 == 0:
                    self.color = (255,0,0)
                else:
                    self.color = (0,0,0)
            else:
                self.color = (0,255,0)
            self.squares[i].setColor(self.color)
            self.squares[i].draw()


    def assignNumbers(self,black_list = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
                    , red_list = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
                    , final_list = []):
        '''
        (self,list,list) -> (list)
        Creates a list of numbers alternating between black and white
        '''
        #base case
        if len(black_list) == 1 and len(red_list) == 0:
            num = random.choice(black_list)
            final_list.append(num)
            return final_list
        elif len(black_list) <= len(red_list):
            #assigns a random number from red_list to final_list and removes it from red_list
            num = random.choice(red_list)
            red_list.remove(num)
            final_list.append(num)
            #recursively calls assignNumber with a shorter red_list
            return self.assignNumbers(black_list,red_list)
        else:
            #assigns a random number from black_list to final_list and removes it from black_list
            num = random.choice(black_list)
            black_list.remove(num)
            final_list.append(num)
            #recursively calls assignNumber with a shorter black_list
            return self.assignNumbers(black_list,red_list)


    def getNumbers(self):
        '''
        (self) -> (list)
        Returns all the numbers on the wheel
        '''
        numbers = self.assignNumbers()
        return numbers


    def getWinningIndex(self):
        '''
        (self) -> (int)
        Returns the index of the square that the ball is closest to
        '''
        lowest_val = 100
        for i in range(37):
            #Checks which top midpoint of the roulette wheel's squares is closest to the ball
            if math.sqrt(math.pow(rouletteWheel.squares[i].getPointX()-block.getPointX(),2) + math.pow(rouletteWheel.squares[i].getPointY()-block.getPointY(),2)) < lowest_val:

                mid_x = (rouletteWheel.squares[i].getPointX() + rouletteWheel.squares[i].getPointX2()) / 2
                mid_y = (rouletteWheel.squares[i].getPointY() + rouletteWheel.squares[i].getPointY2()) / 2
                
                lowest_val = math.sqrt(math.pow(mid_x-block.getPointX(),2) + math.pow(mid_y-block.getPointY(),2))
                winning_index = i
                return winning_index
    

class RouletteBall(pho.Ball):
    '''
    This class provides functions to display and simulate a roulette Ball
    '''
    def __init__(self,win,radius,x0,y0,rotVel=100,isSpinning=False,color=(100,100,100)):
        '''
        (self,win,int,float,float,float,boolean,tuple) -> (None)
        Constructor for RouletteBall
        '''
        #Call to Ball constructor
        pho.Ball.__init__(self,win,radius,x0,y0,color)
        self.win = win
        self.radius = radius
        self.x0 = x0
        self.y0 = y0
        self.rotVel = rotVel
        self.isSpinning = isSpinning
        self.color = color
        self.vis = [gr.Circle(gr.Point(x0,y0),self.radius)]


    def start_spin(self):
        '''
        (self) -> (None)
        Sets up the initial conditions for the roulette wheel to spin
        '''
        self.isSpinning = True
        #sets ball's intial position to a random location along the wheel
        block.rotate(random.random()*360)
        rouletteBall.setColor(self.color)
        rouletteBall.draw()
        self.rotVel = 100
        block.setRotVelocity(self.rotVel)
        board.assignColors()


    def spin(self):
        '''
        (self) -> (None)
        Makes the ball spin
        '''

        if self.rotVel > 0:
            self.rotVel -= .1
            block.setRotVelocity(self.rotVel)

            block.setColor((0,255,0))

            #This makes it so that the ball constantly moves to the location of the (invisible) block
            rouletteBall.setPosition(block.getPointX()/10.6 + 339.5,((win.getHeight()-block.getPointY())/(1.1*scale)) + 5.75)
        else:
            self.isSpinning = False
            block.setColor((0,255,0))
            rouletteBall.undraw()


    def getIsSpinning(self):
        '''
        (self) -> (boolean)
        Returns whether the ball is spinning
        '''
        return self.isSpinning


    def setIsSpinning(self,isSpinning):
        '''
        (self,boolean) -> (None)
        Sets the boolean value of self.isSpinning
        '''
        self.isSpinning = isSpinning


class PlayerArea:
    '''
    This class controls everything that happens in the player's area (top left of screen)
    '''
    def __init__(self,win):
        '''
        (self,win) -> (None)
        Constructor of PlayerArea
        '''
        self.balance = 1000
        self.win = win
        self.scale = 10
        self.chips = []
        self.chips_x = []
        self.chips_y = []
        self.chip_values = []
        self.board_indeces = []


    def setBalance(self,balance):
        '''
        (self,int) -> (None)
        Sets the value of the player's balance
        '''
        self.balance = balance


    def getBalance(self):
        '''
        (self) -> (int)
        Returns the balance of the player
        '''
        return self.balance
        

    def playerSetup(self):
        '''
        (self) -> (None)
        Displays all the text that will be visible in the player's area at the beginning of the game
        '''
        #Displays the option to spin the wheel and the amount of money the player has
        spin_instructions = Text(self.win,12,47.5,"Press 's' to spin!")
        spin_instructions.displayText()
        betting_instructions1 = Text(self.win,12,44,"Click a chip, then",25)
        betting_instructions2 = Text(self.win,12,40.5,"click a square to bet!",25)
        betting_instructions1.displayText()
        betting_instructions2.displayText()
        self.cur_bal_text = Text(self.win,12.5,37,"Current Balance: $" + str(self.getBalance()),22)
        self.cur_bal_text.displayText()

        #Makes chips of various values for betting
        self.ten_chip = pho.Ball(self.win,3,4.5,30,(255,0,0))
        self.ten_chip.draw()
        self.ten_text = Text(self.win,4.5,30,"10")
        self.ten_text.displayText()
        self.fifty_chip = pho.Ball(self.win,3,12.5,30,(50,50,255))
        self.fifty_chip.draw()
        self.fifty_text = Text(self.win,12.5,30,"50")
        self.fifty_text.displayText()
        self.hundred_chip = pho.Ball(self.win,3,20.5,30,(255,165,0))
        self.hundred_chip.draw()
        self.hundred_text = Text(self.win,20.5,30,"100",30)
        self.hundred_text.displayText()


    def chip_setup(self,board,big_chip_x = [45,125,205],big_chip_val = [10,50,100],big_chip_color = [(255,0,0),(0,0,255),(255,165,0)], little_chip_shift = [1.4,0,-1.4]):
        '''
        (self,board,list,list,list,list) -> (None)
        This function places a minature chip on the square bet on and updates the balance accordingly
        '''
        #assigns mouse_point the point at which the mouse was clicked
        mouse_point = self.win.checkMouse()
        #checks if the mouse was not clicked
        if mouse_point != None:
            #iterates through each of the three types of chips
            for k in range(len(big_chip_x)):
                #Checks to see which big chip was clicked
                if math.sqrt(math.pow(mouse_point.getX()-big_chip_x[k],2)+math.pow(mouse_point.getY()-200,2)) < 30 and playerArea.getBalance() - big_chip_val[k] >= 0:
                    #assigns mouse_point the point at which the mouse was last clicked
                    mouse_point = self.win.getMouse()
                    # iterates through the length of the board (excluding the zero spot)
                    for i in range(board.getNumCols()+3):
                        for j in range(board.getNumRows()):
                            #checks if the main body and far right side of the board was clicked
                            if i*3 + (2-j) < 39:
                                if mouse_point.getX() > (board.getBoardX()[(i*3)+(2-j)] - board.getSquareWidth()/2) * self.scale and mouse_point.getX() < (board.getBoardX()[(i*3)+(2-j)] + board.getSquareWidth()/2) * self.scale and mouse_point.getY() > win.getHeight() - (board.getBoardY()[(i*3)+(2-j)] + board.getSquareHeight()/2) * self.scale and mouse_point.getY() < win.getHeight() - (board.getBoardY()[(i*3)+(2-j)] - board.getSquareHeight()/2) * self.scale:
                                    #places small chip at correct square
                                    small_chip = pho.Ball(self.win,.6,board.getBoardX()[i*3 + (2-j)],board.getBoardY()[i*3 + (2-j)]+little_chip_shift[k],big_chip_color[k])
                                    self.chips.append(small_chip)
                                    self.chips_x.append(board.getBoardX()[i*3 + (2-j)])
                                    self.chips_y.append(board.getBoardY()[i*3 + (2-j)]+little_chip_shift[k])
                                    self.board_indeces.append(i*3 + (2-j))
                            #checks if the top row of the bottom row was clicked
                            elif i*3 + (2-j) < 42:
                                if mouse_point.getX() > (board.getBoardX()[(i*3)+(2-j)] - board.getSquareWidth()*2) * self.scale and mouse_point.getX() < (board.getBoardX()[(i*3)+(2-j)] + board.getSquareWidth()*2) * self.scale and mouse_point.getY() > win.getHeight() - (board.getBoardY()[(i*3)+(2-j)] + board.getSquareHeight()/4) * self.scale and mouse_point.getY() < win.getHeight() - (board.getBoardY()[(i*3)+(2-j)] - board.getSquareHeight()/4) * self.scale:
                                    #places small chip at correct square
                                    small_chip = pho.Ball(self.win,.6,board.getBoardX()[i*3 + (2-j)]-little_chip_shift[k],board.getBoardY()[i*3 + (2-j)],big_chip_color[k])
                                    self.chips.append(small_chip)
                                    self.chips_x.append(board.getBoardX()[i*3 + (2-j)]-little_chip_shift[k])
                                    self.chips_y.append(board.getBoardY()[i*3 + (2-j)])
                                    self.board_indeces.append(i*3 + (2-j))
                            #checks if the very bottom row was clicked
                            elif i*3 + (2-j) < 48:
                                if mouse_point.getX() > (board.getBoardX()[(i*3)+(2-j)] - board.getSquareWidth()) * self.scale and mouse_point.getX() < (board.getBoardX()[(i*3)+(2-j)] + board.getSquareWidth()) * self.scale and mouse_point.getY() > win.getHeight() - (board.getBoardY()[(i*3)+(2-j)] + board.getSquareHeight()/4) * self.scale and mouse_point.getY() < win.getHeight() - (board.getBoardY()[(i*3)+(2-j)] - board.getSquareHeight()/4) * self.scale:
                                    #places small chip at correct square
                                    small_chip = pho.Ball(self.win,.6,board.getBoardX()[i*3 + (2-j)]-little_chip_shift[k],board.getBoardY()[i*3 + (2-j)],big_chip_color[k])
                                    self.chips.append(small_chip)
                                    self.chips_x.append(board.getBoardX()[i*3 + (2-j)]-little_chip_shift[k])
                                    self.chips_y.append(board.getBoardY()[i*3 + (2-j)])
                                    self.board_indeces.append(i*3 + (2-j))
                    #checks if the zero spot was clicked
                    if mouse_point.getX() > (board.getBoardX()[48] - board.getSquareWidth()/2) * self.scale and mouse_point.getX() < (board.getBoardX()[48] + board.getSquareWidth()/2) * self.scale and mouse_point.getY() > win.getHeight() - (board.getBoardY()[48] + board.getSquareHeight()*(3/2)) * self.scale and mouse_point.getY() < win.getHeight() - (board.getBoardY()[48] - board.getSquareHeight()*(3/2)) * self.scale:
                        #places small chip at correct square
                        small_ten_chip = pho.Ball(self.win,.6,board.getBoardX()[48],board.getBoardY()[48]+little_chip_shift[k],big_chip_color[k])
                        self.chips.append(small_ten_chip)
                        self.chips_x.append(board.getBoardX()[48])
                        self.chips_y.append(board.getBoardY()[48]+little_chip_shift[k])
                        self.board_indeces.append(48)
                    #Updates the list of chip values and the balance
                    self.chip_values.append(big_chip_val[k])
                    self.setBalance(self.getBalance() - big_chip_val[k])
                    self.cur_bal_text.undrawText()
                    self.cur_bal_text = Text(self.win,12.5,37,"Current Balance: $" + str(self.getBalance()),22)
                    self.cur_bal_text.displayText()


    def getBoardIndeces(self):
        '''
        (self) -> (list)
        Returns the indices of the squares on the board
        '''
        return self.board_indeces


    def getChipsX(self):
        '''
        (self) -> (list)
        Returns the x positions of the chips on the board
        '''
        return self.chips_x


    def getChipsY(self):
        '''
        (self) -> (list)
        Returns the y positions of the chips on the board
        '''
        return self.chips_y


    def getChipValues(self):
        '''
        (self) -> (list)
        Returns the monetary values of the chips on the board
        '''
        return self.chip_values


    def drawChips(self):
        '''
        (self) -> (None)
        Draws the chips on the board
        '''
        for chip in self.chips:
            if chip.drawn:
                chip.undraw()
            chip.draw()
    

    def undrawChips(self):
        '''
        (self) -> (None)
        Undraws chips and resets related values
        '''
        for chip in self.chips:
            chip.undraw()
        self.chips = []
        self.chips_x = []
        self.chips_y = []
        self.chip_values = []


    def betting(self):
        '''
        (self) -> (None)
        Performs payouts on bets
        '''
        #iterates through every chip on the board
        for i in range(len(self.chips)):
            #payouts for main body of board
            if self.getBoardIndeces()[i] < 36:
                if board.getWinningNumber()-1 == self.getBoardIndeces()[i]:
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 36))
            #payouts for far right side of board
            elif self.getBoardIndeces()[i] == 36:
                if board.getWinningNumber() % 3 == 1:
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 3))
            elif self.getBoardIndeces()[i] == 37:
                if board.getWinningNumber() % 3 == 2:
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 3))
            elif self.getBoardIndeces()[i] == 38:
                if board.getWinningNumber() % 3 == 0:
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 3))
            #payouts for top of bottom row
            elif self.getBoardIndeces()[i] == 39:
                if board.getWinningNumber() <= 12:
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 3))
            elif self.getBoardIndeces()[i] == 40:
                if board.getWinningNumber() > 12 and board.getWinningNumber() <= 24:
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 3))
            elif self.getBoardIndeces()[i] == 41:
                if board.getWinningNumber() >= 25:
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 3))
            #payouts for very bottom row
            elif self.getBoardIndeces()[i] == 42:
                if board.getWinningNumber() <= 18:
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 2))
            elif self.getBoardIndeces()[i] == 43:
                if board.getWinningNumber() % 2 == 0:
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 2))
            elif self.getBoardIndeces()[i] == 44:
                if board.getWinningNumber() in board.getRedList():
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 2))
            elif self.getBoardIndeces()[i] == 45:
                if board.getWinningNumber() in board.getBlackList():
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 2))
            elif self.getBoardIndeces()[i] == 46:
                if board.getWinningNumber() % 2 != 0:
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 2))
            elif self.getBoardIndeces()[i] == 47:
                if board.getWinningNumber() >= 19:
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 2))
            #payout for zero spot
            elif self.getBoardIndeces()[i] == 48:
                if board.getWinningNumber() == 0:
                    self.setBalance(self.getBalance() + (self.getChipValues()[i] * 36))
        #Adjusts balance based on payout
        self.cur_bal_text.undrawText()
        self.cur_bal_text = Text(self.win,12.5,37,"Current Balance: $" + str(self.getBalance()),22)
        self.cur_bal_text.displayText()
                

class Board:
    '''
    This class provides function to simulate and display a roulette board
    '''
    def __init__(self,win):
        '''
        (self,win) -> (None)
        Constructor of Board
        '''
        self.win = win
        self.scale = 10
        self.num_cols = 13
        self.num_rows = 3
        self.square_width = 42.5/(self.num_cols)
        self.square_height = 5
        self.board = []
        self.board_x = []
        self.board_y = []
        #lists of black and red numbers on a roulette board
        self.black_list = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        self.red_list = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]


    def getNumCols(self):
        '''
        (self) -> (int)
        Returns the number of columns in the main body of the board (plus the far right column)
        '''
        return self.num_cols


    def getNumRows(self):
        '''
        (self) -> (int)
        Returns the number of rows in the main body of the board
        '''
        return self.num_rows


    def getSquareWidth(self):
        '''
        (self) -> (float)
        Returns the width of the squares
        '''
        return self.square_width


    def getSquareHeight(self):
        '''
        (self) -> (float)
        Returns the height of the squares
        '''
        return self.square_height
    

    def makeBoard(self):
        '''
        (self) -> (None)
        Makes and animates a roulette board
        '''
        #Makes the main body of the board (plus the extra column on the right side)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                square = pho.Block(self.win,5+(self.square_width/2)+(i*self.square_width),10+(j*self.square_height),self.square_width,self.square_height)
                self.board.append(square)
                self.board_x.append(5+(self.square_width/2)+(i*self.square_width))
                self.board_y.append(10+(j*self.square_height))

        #makes top row of the bottom two
        for i in range(3):
            square = pho.Block(self.win,5+(2*self.square_width)+(i*(4*self.square_width)),6.3,4*self.square_width,self.square_height/2)
            self.board.append(square)
            self.board_x.append(5+(2*self.square_width)+(i*(4*self.square_width)))
            self.board_y.append(6.3)

        #makes very bottom row
        for i in range(6):
            square = pho.Block(self.win,5+self.square_width+(i*(2*self.square_width)),3.8,2*self.square_width,self.square_height/2)
            self.board.append(square)
            self.board_x.append(5+self.square_width+(i*(2*self.square_width)))
            self.board_y.append(3.8)
            
        #draw the whole board except for the space for zero
        for square in self.board:
            square.draw()

        #makes the spot for 0
        zero_spot = gr.Polygon(gr.Point(5*self.scale,self.win.getHeight()-22.5*self.scale),gr.Point(5*self.scale,self.win.getHeight()-7.5*self.scale),gr.Point(3.5*self.scale,self.win.getHeight()-7.5*self.scale),gr.Point(2*self.scale,self.win.getHeight()-15*self.scale),gr.Point(3.5*self.scale,self.win.getHeight()-22.5*self.scale))
        zero_spot.draw(self.win)
        self.board.append(zero_spot)
        self.board_x.append(3.75)
        self.board_y.append(15)


    def makeBoardText(self):
        #Numbers the main body of the board (plus the extra column on the right side)
        for i in range(self.num_cols-1):
            for j in range(self.num_rows):
                if (i)*(j) <= 36:
                    square_number = Text(self.win,5+(self.square_width/2)+(i*self.square_width),10+(j*self.square_height),str((i*3)+(j+1)),15,"white")
                    square_number.displayText()
            
        for i in range(self.num_rows):
            two_to_one_text = Text(self.win,45.85,10+(i*self.square_height),str("2 to 1"),10,"white")
            two_to_one_text.displayText()

        #numbers top row of the bottom two
        for i in range(3):
            if(i == 0):
                first_12_text = Text(self.win,5+(2*self.square_width)+(i*(4*self.square_width)),6.3,"1st 12",15,"white")
                first_12_text.displayText()
            elif(i == 1):
                second_12_text = Text(self.win,5+(2*self.square_width)+(i*(4*self.square_width)),6.3,"2nd 12",15,"white")
                second_12_text.displayText()
            else:
                second_12_text  = Text(self.win,5+(2*self.square_width)+(i*(4*self.square_width)),6.3,"3rd 12",15,"white")
                second_12_text.displayText()

        #numbers very bottom row
        for i in range(6):
            if(i == 0):
                one_to_18_text = Text(self.win,5+self.square_width+(i*(2*self.square_width)),3.8,"1-18",15,"white")
                one_to_18_text.displayText()
            elif(i == 1):
                even_text = Text(self.win,5+self.square_width+(i*(2*self.square_width)),3.8,"EVEN",15,"white")
                even_text.displayText()
            elif(i == 2):
                red_text = Text(self.win,5+self.square_width+(i*(2*self.square_width)),3.8,"RED",15,"red")
                red_text.displayText()
            elif(i == 3):
                block_text = Text(self.win,5+self.square_width+(i*(2*self.square_width)),3.8,"BLACK",15)
                block_text.displayText()
            elif(i == 4):
                odd_text = Text(self.win,5+self.square_width+(i*(2*self.square_width)),3.8,"ODD",15,"white")
                odd_text.displayText()
            else:
                nineteen_to_36_text = Text(self.win,5+self.square_width+(i*(2*self.square_width)),3.8,"19-36",15,"white")
                nineteen_to_36_text.displayText()

        #numbers the spot for 0
        zero_text = Text(self.win,3.5,15,"0",15,"white")
        zero_text.displayText()


    def getBoard(self):
        '''
        (self) -> (list)
        Returns the width of the squares
        '''
        return self.board
    

    def changeSquareColor(self,index,color=(255,215,0)):
        '''
        (self,int,tuple) -> (None)
        Changes the color of the square displaying the value of index
        '''
        self.board[index-1].setColor(color)


    def getWinningNumber(self):
        '''
        (self) -> (int)
        Returns the number that the ball ended on
        '''
        return rouletteWheel.getNumbers()[rouletteWheel.getWinningIndex()]


    def displayWinningNumber(self):
        '''
        (self) -> (None)
        Makes the square displaying the winning number gold
        '''
        self.changeSquareColor(self.getWinningNumber())


    def assignColors(self,black_list = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
                     , red_list = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]):
        '''
        (self,list,list) -> (None)
        Assigns appropriate color to the squares
        '''
        for i in range(1,37):
            if i in black_list:
                color = (0,0,0)
            if i in red_list:
                color = (255,0,0)
            board.changeSquareColor(i,color)
        self.black_list = black_list
        self.red_list = red_list


    def getBlackList(self):
        '''
        (self) -> (list)
        Returns self.black_list
        '''
        return self.black_list


    def getRedList(self):
        '''
        (self) -> (list)
        Returns self.red_list
        '''
        return self.red_list


    def getBoardX(self):
        '''
        (self) -> (list)
        Returns the x values of the board squares
        '''
        return self.board_x


    def getBoardY(self):
        '''
        (self) -> (list)
        Returns the y values of the board squares
        '''
        return self.board_y


if __name__ == "__main__":
    #sets up game objects and visuals
    win = gr.GraphWin('Roulette', 500, 500, False)
    scale = 10
    dt = 0.02
    makeBackground(win)
    makeDividers(win)
    rouletteWheel = RouletteWheel(win,12,[(3*win.getWidth()/4)/scale,(3*win.getHeight()/4)/scale])
    rouletteWheel.makeWheel()
    rouletteWheel.drawWheelSquares()
    rouletteBall = RouletteBall(win,8,37.5*scale,48)
    playerArea = PlayerArea(win)
    playerArea.playerSetup()
    block = pho.RotatingBlock(win,37.5,48,2,2,(3*win.getWidth()/4)/scale,(3*win.getHeight()/4)/scale,(0,255,0))
    board = Board(win)
    board.makeBoard()
    board.assignColors()
    board.makeBoardText()

    #Makes it so that game will run until window is exited
    while True:
        #runs main game
        win.update()
        block.update(dt)
        if win.checkKey() == 's':
            rouletteBall.start_spin()
        if rouletteBall.getIsSpinning():
            rouletteBall.spin()
            if block.getRotVelocity() < 0:
                board.displayWinningNumber()
                playerArea.betting()
                playerArea.undrawChips()
        else:
            playerArea.chip_setup(board)
            playerArea.drawChips()