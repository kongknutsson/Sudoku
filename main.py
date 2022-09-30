from recursive_sudoku_solver import RecursiveSudokuSolver
from least_poss_sudoku_solver import LeastPossibleSudokuSolver
from cell import Cell
from board import Board

board_9x9 = [
    [".", ".", "2", ".", ".", ".", ".", ".", ".",],
    [".", ".", ".", ".", ".", ".", ".", ".", ".",],
    [".", ".", ".", ".", ".", ".", ".", ".", ".",],
    [".", ".", ".", ".", ".", ".", ".", ".", ".",],
    [".", ".", ".", ".", ".", ".", ".", ".", ".",],
    [".", ".", ".", ".", ".", ".", ".", ".", ".",],
    [".", ".", ".", ".", ".", ".", ".", ".", ".",],
    [".", ".", ".", ".", ".", ".", ".", ".", ".",],
    [".", ".", ".", ".", ".", ".", ".", ".", ".",]
]


#### Reads in a 25x25 board from a file #### 
normal_chars = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open("25x25.csv") as file:
    cells_25x25 = []
    for row_index, line in enumerate(file):
        line = line.replace("*", ".").strip()
        line = line.split(",")        
        current_row = []
        for col_index, character in enumerate(line):
            cell = Cell(
                value =  str(normal_chars[int(character)] if character != "." else "."),
                row = row_index,
                col = col_index
            )
            current_row.append(cell)

        cells_25x25.append(current_row)

#### Generates an empty 9x9 board #### 
cells_9 = []
for row in range(0,9):
    cell_row = []
    for col in range(0,9):
        cell_row.append(Cell(board_9x9[row][col], row, col))
    cells_9.append(cell_row)


# Creates the two boards. 
board_25x25 = Board(cells_25x25, 5)
board_9x9 = Board(cells_9, 3)

# Creates the Solver Objects. 
recursive_solver = RecursiveSudokuSolver()
least_poss_solver = LeastPossibleSudokuSolver()

# Uncomment the one you want to run :) 
#least_poss_solver.solve(board_9x9)
#recursive_solver.solve(board_9x9)
least_poss_solver.solve(board_25x25)
#recursive_solver.solve(board_25x25)