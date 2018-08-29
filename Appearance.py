##Play the connect 4 game
##
##1. Desigh Appearance
##      - Show Grid
##      - Burb
##      - show result
##                      -Lose
##                      -Won
##                      -Drawn
##                      -Undecided

def burb():
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('                MineSweeper by Nutdanai                ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("| S = start game | Q = exit | M = show game \
                 \n| R = restart | L = Lost |") 

    
def showLoseResult():
        print('Hahahahha!! you lose')
def showWonResult():
        print('Excellent!! you won')
def showDrawnResult():
        print('Well!! The game is drawn')
def showQuitMessage():
        print('We hope you enjoy the game.')
        print('Please play again next time.')
