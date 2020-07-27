# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:49:01 2020

@author: Todd
"""

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
               (board[r+1][c+1] in ("X","H")) &\
               (board[r+2][c+2] == "-")):
                
                poss_moves.append([[r,c],[r+2,c+2]])
                        
        for c in range(2,8):
            
            if((board[r][c] in ("S")) &\
               (board[r+1][c-1] in ("X","H")) &\
               (board[r+2][c-2] == "-")):
                
                poss_moves.append([[r,c],[r+2,c-2]])
                        
    for r in range(2,8):
        for c in range(6):
            
            if((board[r][c] in ("O","S")) &\
               (board[r-1][c+1] in ("X","H")) &\
               (board[r-2][c+2] == "-")):
                
                poss_moves.append([[r,c],[r-2,c+2]])
                        
        for c in range(2,8):
            
            if((board[r][c] in ("O","S")) &\
               (board[r-1][c-1] in ("X","H")) &\
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


#make a move black
def move_black(a,b,board):
    
    turn_had = False
    attack_again = False
    
    #check for any moves that are captures
    poss_moves = captures_black(board)
    
    #movement of a piece one step
    if(((a[0]-b[0] == -1) & (abs(a[1]-b[1]) == 1) &\
        (board[a[0]][a[1]] in ("X"))) or\
       ((abs(a[0]-b[0]) == 1) & (abs(a[1]-b[1]) == 1) &\
        (board[a[0]][a[1]] in ("H")))):
        
        if(not poss_moves == []):
            return "IM" 
        else:
            board[b[0]][b[1]] = board[a[0]][a[1]]
            board[a[0]][a[1]] = "-"
            
            #promotion to king
            if((board[b[0]][b[1]] == "X") & (b[0] == 7)):
                        
                board[b[0]][b[1]] = "H"
                    
            return(board)
      
    #capturing another piece    
    elif([a,b] in poss_moves): 
        
        c = [int((a[0]+b[0])/2),int((a[1]+b[1])/2)]
        
        if(board[c[0]][c[1]] in ("O","S")):
        
            board[b[0]][b[1]] = board[a[0]][a[1]]
            board[a[0]][a[1]] = "-"
            board[c[0]][c[1]] = "-"
            attack_again = True
            
        else:
            return "IM"
        
    
    else:
        return "IM"
    
    #promotion to king
    if((board[b[0]][b[1]] == "X") & (b[0] == 7)):
                
        board[b[0]][b[1]] = "H"
    
    
    if(attack_again == True):
        new_moves = captures_black(board,b)
        if(not(new_moves == [])):
            turn_had == False
        else:
            attack_again = False
            turn_had = True
            return(board)
        
    if((turn_had == False) & (attack_again == True)):
        print("Black still to play")
        print(np.array(board))
        while True:
            x,y = take_input()
            if(x==b):
                g = move_black(x,y,board)
                if(g=="IM"):
                    print("Invalid Move")
                else:
                    board = g
                    break
            else:
                print("Invalid Move: Must move the piece that has just been moved")
                
        return(board)
            

#----------------------------------------------------------

    
#make a move white
def move_white(a,b,board):
    
    turn_had = False
    attack_again = False
    
    #check for any moves that are captures
    poss_moves = captures_white(board)
    
    #movement of a piece one step
    if(((a[0]-b[0] == 1) & (abs(a[1]-b[1]) == 1) &\
        (board[a[0]][a[1]] in ("O"))) or\
       ((abs(a[0]-b[0]) == 1) & (abs(a[1]-b[1]) == 1) &\
        (board[a[0]][a[1]] in ("S")))):
        
        if(not poss_moves == []):
            return "IM" 
        else:
            board[b[0]][b[1]] = board[a[0]][a[1]]
            board[a[0]][a[1]] = "-"
            
            #promotion to king
            if((board[b[0]][b[1]] == "O") & (b[0] == 0)):
                        
                board[b[0]][b[1]] = "S"
            
            return(board)
      
    #capturing another piece    
    elif([a,b] in poss_moves): 
        
        c = [int((a[0]+b[0])/2),int((a[1]+b[1])/2)]
        
        if(board[c[0]][c[1]] in ("X","H")):
        
            board[b[0]][b[1]] = board[a[0]][a[1]]
            board[a[0]][a[1]] = "-"
            board[c[0]][c[1]] = "-"
            attack_again = True
            
        else:
            return "IM"
        
    
    else:
        return "IM"
    
    #promotion to king
    if((board[b[0]][b[1]] == "O") & (b[0] == 0)):
                
        board[b[0]][b[1]] = "S"
    
    
    if(attack_again == True):
        new_moves = captures_white(board,b)
        if(not(new_moves == [])):
            turn_had == False
        else:
            attack_again = False
            turn_had = True
            return(board)
        
    if((turn_had == False) & (attack_again == True)):
        print(np.array(board))
        print("White still to play")
        while True:
            x,y = take_input()
            if(x==b):
                g = move_white(x,y,board)
                if(g=="IM"):
                    print("Invalid Move")
                else:
                    board = g
                    break
            else:
                print("Invalid Move: Must move the piece that has just been moved")
                
        return(board)
            


#------------------------------------------------------------
#count remaining black pieces      
def count_black(board):
    
    pieces = 0
    
    for r in range(8):
        for c in range(8):
            if board[r][c] in ("X","H"):
                pieces += 1
    
    return pieces

#------------------------------------------------------------
#count remaining white pieces
def count_white(board):
    
    pieces = 0
    
    for r in range(8):
        for c in range(8):
            if board[r][c] in ("O","S"):
                pieces += 1
    
    return pieces

#------------------------------------------------------------
    
def play_draughts():
    
    game = [["X","-","X","-","X","-","X","-",],\
            ["-","X","-","X","-","X","-","X",],\
            ["X","-","X","-","X","-","X","-",],\
            ["-","-","-","-","-","-","-","-",],\
            ["-","-","-","-","-","-","-","-",],\
            ["-","O","-","O","-","O","-","O",],\
            ["O","-","O","-","O","-","O","-",],\
            ["-","O","-","O","-","O","-","O",]]
    
    pieces_black = 12
    pieces_white = 12
    turn = 0
    
    print(np.array(game))
    
    while ((pieces_black > 0) & (pieces_white > 0)):
        
        h = copy.deepcopy(game)
        
        if turn == 0:
        
            while True:
                
                print("White to play")
                a,b = take_input()
                g = move_white(a,b,game)
                
                if(g=="IM"):
                    print("Invalid Move")
                else:
                    break
    
            print(np.array(g))
            
        elif turn == 1:
        
            while True:
                
                print("Black to play")
                a,b = take_input()
                g = move_black(a,b,game)
                
                if(g=="IM"):
                    print("Invalid Move")
                else:
                    break
        
            print(np.array(g))
        
        
        carry_on = input("Confirm Move: ")
        
        if carry_on == "y":
            turn = 1 - turn
        elif carry_on == "n":
            print(np.array(h))
            game = h
        elif carry_on == "exit":
            return "Game Aborted"
            
        pieces_black = count_black(game)
        pieces_white = count_white(game)
            
    if turn == 0:
        print("Black Wins!")
    elif turn == 1:
        print("White Wins!")
        
    return



#-------------Test area--------------------------------------
    


game = [["X","-","X","-","X","-","X","-",],\
            ["-","X","-","X","-","X","-","X",],\
            ["X","-","X","-","X","-","X","-",],\
            ["-","-","-","-","-","-","-","-",],\
            ["-","-","-","-","-","-","-","-",],\
            ["-","O","-","O","-","O","-","O",],\
            ["O","-","O","-","O","-","O","-",],\
            ["-","O","-","O","-","O","-","O",]]

