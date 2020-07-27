
import numpy as np
import copy



def take_input():

    a,b = [],[]
    
    while True:
        try:
            x = int(input("From row: "))
            if((x>=0) & (x<=7)):
                a.append(x)
                break
            else:
                print("Invalid Input: Must be between 0 or 7")
                ValueError
        except ValueError:
            print("Invalid Input")
            
    while True:
        try:
            x = int(input("From column: "))
            if((x>=0) & (x<=7)):
                a.append(x)
                break
            else:
                print("Invalid Input: Must be between 0 or 7")
                ValueError
        except ValueError:
            print("Invalid Input")
    
    while True:
        try:
            x = int(input("To row: "))
            if((x>=0) & (x<=7)):
                b.append(x)
                break
            else:
                print("Invalid Input: Must be between 0 or 7")
                ValueError
        except ValueError:
            print("Invalid Input")
            
    while True:
        try:
            x = int(input("To column: "))
            if((x>=0) & (x<=7)):
                b.append(x)
                break
            else:
                print("Invalid Input: Must be between 0 or 7")
                ValueError
        except ValueError:
            print("Invalid Input")
    
    return a,b



#---------------------------------------------


#check for possible captues black
def captures_black(board, b="none"):
    
    poss_moves = []
    
    for r in range(6):
        for c in range(6):
            
            if((board[r][c] in ("X","H")) &\
               (board[r+1][c+1] in ("O","S")) &\
               (board[r+2][c+2] == "-")):
                
                poss_moves.append([[r,c],[r+2,c+2]])
                        
        for c in range(2,8):
            
            if((board[r][c] in ("X","H")) &\
               (board[r+1][c-1] in ("O","S")) &\
               (board[r+2][c-2] == "-")):
                
                poss_moves.append([[r,c],[r+2,c-2]])
                        
    for r in range(2,8):
        for c in range(6):
            
            if((board[r][c] in ("H")) &\
               (board[r-1][c+1] in ("O","S")) &\
               (board[r-2][c+2] == "-")):
                
                poss_moves.append([[r,c],[r-2,c+2]])
                        
        for c in range(2,8):
            
            if((board[r][c] in ("H")) &\
               (board[r-1][c-1] in ("O","S")) &\
               (board[r-2][c-2] == "-")):
                
                poss_moves.append([[r,c],[r-2,c-2]])
                        
    if not(b=="none"):
        new_moves = []
        for i in range(len(poss_moves)):
            if b == poss_moves[i][0]:
                new_moves.append(poss_moves[i])
        
        poss_moves = new_moves
                
    return poss_moves



#----------------------------------------------------------

#check for possible captues white
def captures_white(board, b="none"):
    
    poss_moves = []
    
    for r in range(6):
        for c in range(6):
            
            if((board[r][c] in ("S")) &\