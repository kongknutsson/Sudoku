from sudokuMaker import SudokuMaker
from sudokuSolver import SudokuSolver

board =[
    [0, 0, 0, 1, 0, 9, 0, 5, 0],
    [5, 9, 8, 0, 0, 4, 0, 0, 2],
    [0, 3, 0, 0, 6, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 0],
    [4, 0, 7, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 0],
    [0, 7, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [2, 0, 0, 0, 4, 3, 9, 0, 0]
    ]
solver = SudokuSolver()
solver.solve(board)