board = [                # pos(0,2) board[0][2]
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    
    for row in range(len(board)):
        if (row) % 3 ==0 and row != 0:
            print("-------------")
        for col in range(len(board[0])):
            if (col) % 3 ==0:
                print("|",end = "")
            print(board[row][col], end = "")
        print()
    
#9^44 combinations
#if super computer can calc 1 billion variations/sec -> 240 million years
            
def find_empty(board):
    for row in range(len(board)): #0-8
        for col in range(len(board[0])): #0-8
            if board[row][col] == 0: #board[0][2]
                return (row,col)  #find position of empty  (0,2)
    
    return False
            
def valid(board, num, pos):
    #pos(0,2)
    #check row
    for col in range(len(board[0])): 
        if board[pos[0]][col] == num and col != pos[1]:  #pos[row] = 
            return False
    #check column
    
    for row in range(len(board)):
        if board[row][pos[1]] == num and row != pos[0]:
            return False
        
    #check box 
    box_y = pos[0] // 3 #0,1,2 (0,2) -> Box 00
    box_x = pos[1] // 3 
    
    
    for row in range(box_y*3, box_y + 3):
        for col in range(box_x * 3, box_x * 3 +3):
            if board[row][col] == num and (row,col) != (pos):
                return False 
    return True         
def solved(board):
    find = find_empty(board) #find pos of empty cell
    if not find:
        return True
    else:
        row,col = find
        
    for num in range(1,10):
        if valid(board, num, (row, col)):
            board[row][col] = num  #add number to board
            
            if solved(board):    #recursively call by input new board
                return True
            
            board[row][col] = 0
            
    return False
               
print("Before: ")
print_board(board)
print()
print("Starting to Solve.")
print("Solved!")
solved(board)

print_board(board)