# Sudoku 

#Backtracking (using recursion) - Systematically checking all the possibilities
# How do we represent a grid - Arrays/lists of lists
# How do we print a solution?
#How do we check we can input a field?
#How do we implement the solver?
# grid = yx y vertical x horizontal 
# challenge write a pretty printer for grids
# possible(y,x,n) = True if we can put n n at position y,x in grid and false otherwise assuming that its empty
import numpy

grid =  [[5, 3, 0, 0 ,7 ,0 ,0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def possible(y,x,n):
    # check all the 9 positions in square
    for i in range(0,SIZE) :
        for j in range(0,SIZE) :
            if grid[i][j]==n :
                return False
                # checked everything, it is possible
                return True



def print_grid(x) :
    for row in range(SIZE) :
        print(x*3*" ",end="")
        for col in range(SIZE) :            
            if grid[row][col]==0 :
                print(".",end=" ")
            else :
                print(grid[row][col],end=" ")
        print()

# to learn it - remake it myself


def solve(x) :
    """
    This version of the solve function contains lots of print statements 
    to help understand backtracking (including indentation based on the value of `x`)
    x: level in the recursion

    """
    print(f"{x*3*' '}solve({x}):")
    print_grid(x)
    input(f"{x*3*' '}----")
    # looking for an empty space
    for i in range(0,SIZE) :
        for j in range(0,SIZE) :
            if grid[i][j] == 0 :
                # we found an empty square, we need to try all digits from 1-9
                for n in range(1,10) :
                    if possible(i,j,n) :
                        # we can put n into that square
                        grid[i][j] = n
                        # recursively solve a smaller instance of the sudoku
                        solve(x+1)                        
                        # add comment
                        grid[i][j] = 0
                        print(f"{x*3*' '}Backtracking!") 
                        print(f"{x*3*' '}solve({x}):")
                        print_grid(x)
                        input(f"{x*3*' '}----")
                # we reached a dead end, backtrack 
                return
    # Problem solved! we got a full grid
    print(f"{x*3*' '}Solution: ")
    print_grid(x)
    # add comment
    input(f"{x*3*' '}More?")
                        
                
    
           
       