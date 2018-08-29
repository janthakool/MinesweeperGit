from MineSweeper import *

# Test cases for connect 4
# As a User
# I want to see the current board
# So that i can choose the appropriate cilumn to play

#Scenario 1: Empty board
#Given the initail board
#when show the board
#then the result should be

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

def test_Emty_board_9x9():
    game = minesweeper()
    assert show(game) ==  "8  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "7  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "6  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "5  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "4  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "3  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "2  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "1  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "0  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "   +----------------------------+\n" + \
                          "      0  1  2  3  4  5  6  7  8 \n"

##Scenario : sweepering did't find mine
##given : the board have any mine
##When : user played and input row and col 
##then : did't find any mine the result should be

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
def test_sweepering_does_not_find_mine():
    game = minesweeper()
    Position_mine = [(5,0),(5,1),(5,2),(4,0),(4,2),(3,0),(3,1),(3,2)]
    assert Position_mine == [(5,0),(5,1),(5,2),(4,0),(4,2),(3,0),(3,1),(3,2)]
    game.SWEEPER_position(8,8)
    assert show(game) ==  "8  | XX XX XX XX XX XX XX       |\n" + \
                          "7  | XX XX XX XX XX XX XX       |\n" + \
                          "6  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "5  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "4  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "3  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "2  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "1  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "0  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "   +----------------------------+\n" + \
                          "      0  1  2  3  4  5  6  7  8 \n"

##Scenario : sweepering found mine
##given : mine is row0,column6
##When : user played and input row and col as position's mine (0,6) 
##then : found any mine game is OVER

def test_sweepering_found_mine():
    
    game = minesweeper()
    Position_mine= [(0,6)]
    assert Position_mine == [(0,6)]
    game.SWEEPER_position(5,0)
    assert  game.isOver() == True


##Scenario : check mine around
##Given : mine are 5,0/5,1/5,2/4,0/4,2/3,0/3,1/3,2
##When : user played and input row and column 4,1
##Then : position 4,1 will show '8'
def test_check_mine_arond():
    
    game = minesweeper()
    Position_mine = [(5, 0),(5, 1),(5, 2),(4, 0),(4, 2),(3, 0),(3, 1),(3, 2)]
    game.SWEEPER_position(4,1)
    game.check_mine_AROUND(4,1)
    assert show(game) ==  "8  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "7  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "6  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "5  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "4  | XX *8 XX XX XX XX XX XX XX |\n" + \
                          "3  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "2  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "1  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "0  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "   +----------------------------+\n" + \
                          "      0  1  2  3  4  5  6  7  8 \n"

def test_check_mine_arond_1():
    
    game = minesweeper()
    Position_mine = [(8,1)]
    game.check_mine_AROUND(8,0)
    assert show(game) ==  "8  | *1 XX XX XX XX XX XX XX XX |\n" + \
                          "7  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "6  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "5  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "4  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "3  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "2  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "1  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "0  | XX XX XX XX XX XX XX XX XX |\n" + \
                          "   +----------------------------+\n" + \
                          "      0  1  2  3  4  5  6  7  8 \n"
