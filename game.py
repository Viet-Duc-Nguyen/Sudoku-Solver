import tkinter as tk

# Define the Sudoku board
board = [
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



def solve_sudoku():
    solved = solve(board)
    if solved:
        update_board(board)

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

#9^44 combinations, if super computer calculates 1 billions variations/sec, it would take 240 millions years

def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)  # Find position of empty cell

    return None

def valid(board, num, pos):
    # Check row
    for col in range(len(board[0])):
        if board[pos[0]][col] == num and col != pos[1]:
            return False

    # Check column
    for row in range(len(board)):
        if board[row][pos[1]] == num and row != pos[0]:
            return False

    # Check box
    box_y = pos[0] // 3 #row
    box_x = pos[1] // 3 #col

    for row in range(box_y * 3, box_y * 3 + 3):
        for col in range(box_x * 3, box_x * 3 + 3):
            if board[row][col] == num and (row, col) != pos:
                return False

    return True

def update_board(board):
    for i in range(9):
        for j in range(9):
            entry = entry_grid[i][j]
            entry.config(state=tk.NORMAL)  # Enable the entry widget
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(board[i][j]))
            entry.config(state=tk.DISABLED)  # Disable the entry widget again

# Create the GUI window
window = tk.Tk()
window.title("Sudoku Game")

# Create the grid of Entry widgets
entry_grid = []
for i in range(9):
    row = []
    for j in range(9):
        entry = tk.Entry(window, width=2, font=("Arial", 14))
        entry.grid(row=i, column=j, padx=1, pady=1)
        row.append(entry)
    entry_grid.append(row)


# Set initial values on the grid
for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            entry_grid[i][j].insert(tk.END, str(board[i][j]))
            entry_grid[i][j].config(state=tk.DISABLED) #input board cant be changed

#button
solve_button = tk.Button(window, text="Solve", command=solve_sudoku)
solve_button.grid(row=9, column=0, columnspan=9, pady=10)

# Start the Tkinter event loop
window.mainloop()