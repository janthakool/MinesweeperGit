##
##2. Desigh Event 
##      2.0 Quit
##      2.1 Start game
##      2.2 Play
##      2.3 Resigh (ย้อมแพ้)(yeild)
##      2.4 Restart
##      2.5 Save Game
##      2.6 Load game
##      2.7 Choose level
##
from Appearance import *
from MineSweeper import *
import random,sys

def main():
    global game
    
    game = minesweeper()
    game.RANDOM_mine(N_MINE)
    game.POP_win()
    while True:
        print(show(game))
        print(Position_mine)
        print(POP_win)
        x = 0
        y = 0
        while True:
          try:
             x = int(input("Enter row : "))       
          except ValueError:
             print("Not an integer!")
             continue
          else:
             break
            
        while True:
          try:
             y = int(input("Enter column : "))      
          except ValueError:
             print("Not an integer!")
             continue
          else:
             break 

        if (x and y) > 0 and x <= GRID_HEIGHT or y <= GRID_WIDTH :

            game.SWEEPER_position(x,y)
            
            if game.isOver() == True:
                showLoseResult(x,y)
                game = minesweeper()
                game.mine_anwser()

                ##Clear list of position's mine
                Empty_mine = Position_mine
                del Position_mine[:]
                break
            elif game.win_(x, y) == True:
                print(show(game))
                showWonResult()
                game = minesweeper()
                game.mine_anwser()

                ##Clear list of position's mine
                Empty_mine = Position_mine
                del Position_mine[:]
                break
                
            elif game.isOverXX() == True:
                print(show(game))
                showWonResult()
                game = minesweeper()
                game.mine_anwser()

                ##Clear list of position's mine
                Empty_mine = Position_mine
                del Position_mine[:]
                break
        else:
            print("Row and Column Error")
    
            
game = minesweeper()
#dispatch event
def dispatch(answer):
    Position_mine= []
    global game
    
    if answer == 'Q':
        showQuitMessage()
        sys.exit()
    elif answer == 'M':
        print(show(game))
             
    elif answer == 'S':
        
        main()
        print(show(game))
                        
    elif answer == 'R':       
        main()
        print(show(game))
    elif answer == 'L':
        showLoseResult(x,y)
        game = minesweeper()
        game.mine_anwser()

        ##Clear list of position's mine
        Empty_mine = Position_mine
        del Position_mine[:]
        print(show(game))
                        



















                        
    
