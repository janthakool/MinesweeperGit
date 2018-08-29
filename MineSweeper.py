from MineSweeper_test import *
#MineSweeper Game
import random

##8  | XX XX XX XX XX XX XX XX XX |
##7  | XX XX XX XX XX XX XX XX XX |
##6  | XX XX XX XX XX XX XX XX XX |
##5  | XX XX XX XX XX XX XX XX XX |
##4  | XX XX XX XX XX XX XX XX XX |
##3  | XX XX XX XX XX XX XX XX XX |
##2  | XX XX XX XX XX XX XX XX XX |
##1  | XX XX XX XX XX XX XX XX XX |
##0  | XX XX XX XX XX XX XX XX XX |
##   +----------------------------+
##      0  1  2  3  4  5  6  7  8

#-------------------------------------------------------------------
#Constants
#-------------------------------------------------------------------
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('                MineSweeper by Nutdanai                ')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
GRID_HEIGHT = 9
GRID_WIDTH = 9
N_MINE = 1

##GRID_HEIGHT = 0
##while True:
##    try:
##        GRID_HEIGHT = int(input("ENTER HEIGHT AND WIDTH : "))       
##    except ValueError:
##        print("Not an integer!")
##        continue
##    else:
##        break 
##
##GRID_WIDTH = GRID_HEIGHT
##    
##N_MINE = 0
##while True:
##    try:
##        N_MINE = int(input("Enter Mine(bomb) : "))       
##    except ValueError:
##        print("Not an integer!")
##        continue
##    else:
##        break 


START_CELL = 'XX'
LAST_CELL = '-'
Position_mine= []
mine = '[]'
No_mine = '  '
#-------------------------------------------------------------------
#Variables
#-------------------------------------------------------------------
board = [[START_CELL for col in range (GRID_WIDTH)]for row in range (GRID_HEIGHT)]
#-------------------------------------------------------------------
#Class
#-------------------------------------------------------------------

class minesweeper(object):
    def __init__(self):
        self.grid = [[START_CELL for col in range (GRID_WIDTH)]for row in range (GRID_HEIGHT)]
        self.mine = mine
        self.isOver_ = False
        self.isOverXX_ = False
    def RANDOM_mine(self,N_MINE):
        #Check range of mine that Was mine out of range ? 
        if N_MINE < GRID_HEIGHT*GRID_WIDTH:
            while N_MINE != 0 :
                row = random.randint(0,GRID_HEIGHT-1)
                col = random.randint(0,GRID_WIDTH-1)
                x = (row,col)
                if x not in Position_mine :
                    Position_mine.append((row,col))
                    #self.grid[row][col] = mine
                    N_MINE -= 1    
                else :
                    continue
        else : return print('Mines was out of range')
        return Position_mine

    def mine_anwser(self):
        for i in range(len(Position_mine)):
            row = (Position_mine[i])[0]
            column = (Position_mine[i])[1]
            self.grid[row][column] = mine
        return self.grid[row][column]
        
        
    def SWEEPER_position(self, row, column):
        ## Check game over    
        if (row,column) in Position_mine:     
            self.isOver_ = True
            self.grid[row][column] = mine
            return (self.grid[row][column],self.isOver_) 
        if row >= GRID_HEIGHT or column >= GRID_WIDTH:
            print("#####Sorry out of range#####")    
        else:
            self.check_mine_AROUND(row, column)
            self.check_gameOver(row, column)
            self.check_gameOver_Won(row, column)
            if self.check_mine_AROUND( row, column) == '*0':
                self.none_mine_around(row, column)
                self.grid[row][column] = No_mine
                
                

            else:
                return (self.grid[row][column])  
        return
        
        
    def check_mine_AROUND(self, row, column):
        index = 0
        for i in range (len(Position_mine)):
            x = (Position_mine[i])[0]
            y = (Position_mine[i])[1]
            ## Corner_top_left
            if row == GRID_HEIGHT-1 and column == 0:
                if row == x and column+1 == y:
                    index  += 1
                if row-1 == x and column == y:
                    index  += 1
                if row-1 == x and column+1 == y:
                    index  += 1
            ## Corner_Down_right
            elif row == 0 and column == GRID_WIDTH -1:
                if row+1 == x and column == y:
                    index  += 1
                if row == x and column-1 == y:
                    index  += 1
                if row+1 == x and column-1 == y:
                    index  += 1
            ## Corner_Down_left
            elif row == 0 and column ==0:
                if row == x and column+1 == y:
                    index  += 1
                if row+1 == x and column == y:
                    index  += 1
                if row+1 == x and column+1 == y:
                    index  += 1
            ## Corner_Top_right
            elif row == GRID_HEIGHT - 1 and column == GRID_WIDTH -1:
                if row-1 == x and column-1 == y:
                    index  += 1
                if row-1 == x and column == y:
                    index  += 1
                if row == x and column-1 == y:
                    index  += 1
            ## TOP
            elif row == GRID_HEIGHT - 1 and GRID_WIDTH-2 >= column >= 1:
                if row == x and column+1 == y:
                    index  += 1
                if row-1 == x and column-1 == y:
                    index  += 1
                if row-1 == x and column == y:
                    index  += 1
                if row-1 == x and column+1 == y:
                    index  += 1
                if row == x and column-1 == y:
                    index  += 1
               
            ## DOWN
            elif row == 0 and GRID_WIDTH-2 >= column >= 1:
                if row == x and column-1 == y:
                    index  += 1
                if row+1 == x and column-1 == y:
                    index  += 1
                if row+1 == x and column == y:
                    index  += 1
                if row+1 == x and column+1 == y:
                    index  += 1
                if row == x and column+1 == y:
                    index  += 1
            ## LEFT
            elif GRID_HEIGHT + 2 >= row >= 1 and column ==0:
                if row == x and column+1 == y:
                    index  += 1
                if row+1 == x and column == y:
                    index  += 1
                if row+1 == x and column+1 == y:
                    index  += 1
                if row-1 == x and column == y:
                    index  += 1
                if row-1 == x and column+1 == y:
                    index  += 1
               

            ## RIGHT
            elif row < GRID_HEIGHT -1 and column == GRID_WIDTH -1:
                if row+1 == x and column == y:
                    index  += 1
                if row-1 == x and column-1 == y:
                    index  += 1
                if row-1 == x and column == y:
                    index  += 1
                if row == x and column-1 == y:
                    index  += 1
                if row+1 == x and column-1 == y:
                    index  += 1

            else:
                if row == x and column+1 == y:
                    index  += 1
                if row+1 == x and column == y:
                    index  += 1
                if row+1 == x and column+1 == y:
                    index  += 1
                if row-1 == x and column-1 == y:
                    index  += 1
                if row-1 == x and column == y:
                    index  += 1
                if row-1 == x and column+1 == y:
                    index  += 1
                if row == x and column-1 == y:
                    index  += 1
                if row+1 == x and column-1 == y:
                    index  += 1
                
        x = index
        x = str(x)
        self.grid[row][column] = '*'+x
        
        return (self.grid[row][column])

    ## Purpose : clear empty cell
    def none_mine_around(self, row, column):
        if self.check_mine_AROUND( row, column) == '*0':
            ## Corner_top_left
            if row == GRID_HEIGHT-1 and column == 0:
                if self.check_mine_AROUND( row, column+1) == '*0':
                    self.grid[row][column+1] = No_mine
                if self.check_mine_AROUND( row-1, column) == '*0':
                    self.grid[row-1][column] = No_mine
                if self.check_mine_AROUND( row-1, column+1) == '*0':
                    self.grid[row-1][column+1] = No_mine
            ## Corner_Down_right
            elif row == 0 and column == GRID_WIDTH -1:
                if self.check_mine_AROUND( row+1, column) == '*0':
                    self.grid[row+1][column] = No_mine
                if self.check_mine_AROUND( row, column-1) == '*0':
                    self.grid[row][column-1] = No_mine
                if self.check_mine_AROUND( row+1, column-1) == '*0':
                    self.grid[row+1][column-1] = No_mine
            ## Corner_Down_left
            elif row == 0 and column ==0:
                if self.check_mine_AROUND( row, column+1) == '*0':
                    self.grid[row][column+1] = No_mine
                if self.check_mine_AROUND( row+1, column) == '*0':
                    self.grid[row+1][column] = No_mine
                if self.check_mine_AROUND( row+1, column+1) == '*0':
                    self.grid[row+1][column+1] = No_mine
            ## Corner_Top_right
            elif row == GRID_HEIGHT - 1 and column == GRID_WIDTH -1:
                if self.check_mine_AROUND( row-1, column-1) == '*0':
                    self.grid[row-1][column-1] = No_mine
                if self.check_mine_AROUND( row-1, column) == '*0':
                    self.grid[row-1][column] = No_mine
                if self.check_mine_AROUND( row, column-1) == '*0':
                    self.grid[row][column-1] = No_mine
            ## TOP
            elif row == GRID_HEIGHT - 1 and GRID_WIDTH-2 >= column >= 1:
                if self.check_mine_AROUND( row, column+1) == '*0':
                    self.grid[row][column+1] = No_mine
                if self.check_mine_AROUND( row-1, column-1) == '*0':
                    self.grid[row-1][column-1] = No_mine
                if self.check_mine_AROUND( row-1, column) == '*0':
                    self.grid[row-1][column] = No_mine
                if self.check_mine_AROUND( row-1, column+1) == '*0':
                    self.grid[row-1][column+1] = No_mine
                if self.check_mine_AROUND( row, column-1) == '*0':
                    self.grid[row][column-1] = No_mine
               
            ## DOWN
            elif row == 0 and GRID_WIDTH-2 >= column >= 1:
                if self.check_mine_AROUND( row, column-1) == '*0':
                    self.grid[row][column-1] = No_mine
                if self.check_mine_AROUND( row+1, column-1) == '*0':
                    self.grid[row+1][column-1] = No_mine
                if self.check_mine_AROUND( row+1, column+1) == '*0':
                    self.grid[row+1][column+1] = No_mine
                if self.check_mine_AROUND( row+1, column) == '*0':
                    self.grid[row+1][column] = No_mine
                if self.check_mine_AROUND( row, column+1) == '*0':
                    self.grid[row][column+1] = No_mine
            ## LEFT
            elif GRID_HEIGHT + 2 >= row >= 1 and column ==0:
                if self.check_mine_AROUND( row, column+1) == '*0':
                    self.grid[row][column+1] = No_mine
                if self.check_mine_AROUND( row+1, column) == '*0':
                    self.grid[row+1][column] = No_mine
                if self.check_mine_AROUND( row+1, column+1) == '*0':
                    self.grid[row+1][column+1] = No_mine
                if self.check_mine_AROUND( row-1, column) == '*0':
                    self.grid[row-1][column] = No_mine
                if self.check_mine_AROUND( row-1, column+1) == '*0':
                    self.grid[row-1][column+1] = No_mine
               

            ## RIGHT
            elif row < GRID_HEIGHT -1 and column == GRID_WIDTH -1:
                if self.check_mine_AROUND( row+1, column) == '*0':
                    self.grid[row+1][column] = No_mine
                if self.check_mine_AROUND( row-1, column-1) == '*0':
                    self.grid[row-1][column-1] = No_mine
                if self.check_mine_AROUND( row-1, column) == '*0':
                    self.grid[row-1][column] = No_mine
                if self.check_mine_AROUND( row, column-1) == '*0':
                    self.grid[row][column-1] = No_mine
                if self.check_mine_AROUND( row+1, column-1) == '*0':
                    self.grid[row+1][column-1] = No_mine
            else:
                if self.check_mine_AROUND( row, column+1) != '*0':
                    return None
                else:
                    self.grid[row][column+1] = No_mine
                    return self.none_mine_around(row, column+1)


                if self.check_mine_AROUND( row+1, column) != '*0':
                    return None
                else:
                    self.grid[row+1][column] = No_mine
                    return self.none_mine_around(row+1, column)


                if self.check_mine_AROUND( row+1, column+1) != '*0':
                    return None
                else:
                    self.grid[row+1][column+1] = No_mine
                    return self.none_mine_around(row+1, column+1)


                if self.check_mine_AROUND( row-1, column-1) != '*0':
                    return None
                else:
                    self.grid[row-1][column-1] = No_mine
                    return self.none_mine_around(row-1, column-1)


                if self.check_mine_AROUND( row-1, column) != '*0':
                    return None
                else:
                    self.grid[row-1][column] = No_mine
                    return self.none_mine_around(row-1, column)


                if self.check_mine_AROUND( row-1, column+1) != '*0':
                    return None
                else:
                    self.grid[row-1][column+1] = No_mine
                    return self.none_mine_around(row-1, column+1)

                if self.check_mine_AROUND( row, column-1) != '*0':
                    return None
                else:
                    self.grid[row][column-1] = No_mine
                    return self.none_mine_around(row, column-1)

                if self.check_mine_AROUND( row+1, column-1) != '*0':
                    return None
                else:
                    self.grid[row+1][column-1] = No_mine
                    return self.none_mine_around(row+1, column-1)
        else:
            return self.grid[row][column]
        return
    
    def check_gameOver(self,row, column):
        for i in range (len(Position_mine)):
            x = (Position_mine[i])[0]
            y = (Position_mine[i])[1]
            if x == row and y == column:
                self.isOver_ = True
        return
                
    def check_gameOver_Won(self, row, column):
        currentXX = 0
        for i in range((GRID_HEIGHT)):
            for j in range ((GRID_WIDTH)):
                if self.grid[i][j] == 'XX':
                    currentXX += 1
        if currentXX == N_MINE :
            self.isOverXX_ = True
                    
    def isOver(self):
        return self.isOver_
    
    def isOverXX(self):
        return self.isOverXX_
#-------------------------------------------------------------------
#Function
#-------------------------------------------------------------------

def show(game):
    string = ''
    collist = []
    for row in range(GRID_HEIGHT-1,-1,-1):
    ## edit row bug space
        if 0 <= row <= 9 :
            string += str(row) + "  | "
        elif 10 <= row <= 99 :
            string += str(row) + " | "
        else : ##more than 99
            string += str(row) + "| "
            
        for col in range(0, GRID_WIDTH):
            string += game.grid[row][col] + " "
        string += "|\n"
    
    
    #The label
    #string += "   +-------------------+\n"
    string += "   +" + "-"*(GRID_WIDTH*3)+'-' + '+' + "\n"

#--------## show col and edit bug space ------------#
    for i in range(GRID_WIDTH):
        collist.append(i)
    ## change type a list to tuple   
    aaa = tuple(collist[0:10])
    bbb = tuple(collist[10:])
    ## convert tuple int to str for use madthod join
    xxx = '  '.join(map(str,aaa))
    yyy = ' '.join(map(str,bbb))
    string += "      "+ str(xxx)+" "+str(yyy)+"\n"
    
    
   
    return string

def showLoseResult(x,y):
        print('\n \n')
        print("Position's",(x,y), 'is Mine BOOOOOMMMM')
        print('Hahahahha!! you lose')


                
game = minesweeper()            

#game = minesweeper()
#game.RANDOM_mine(N_MINE)
#game.SWEEPER_position(5,5)            


#print(Position_mine)
##print((Position_mine[0])[0])
##print((Position_mine[0])[1])
print(show(game))
