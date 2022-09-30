from board import Board

EMPTY_SQUARE = "."

class RecursiveSudokuSolver:
    """Class used to solve any sized sudoku recursively
    """
    def __init__(self) -> None:
        self.iterations = 1
        self.found_solutions = 1

    def solve(self, board: Board) -> None:
        """ Recursively finds all possible solutions for any sized Sudoku board. 

        Args:
            board (list): 2d list of strings describing the board, "." are empty squares.
            box_size (int): The size of a box. in 9x9 sudoku this is 3.
        """
        valid_chars = board.get_valid_chars()
        for row in range(0, len(board)):
            for col in range(0, len(board)):
                cell = board.get_cell(row, col)
                if cell.get_value() == EMPTY_SQUARE:
                    for char in valid_chars:
                        if board.is_legal_move(char, row, col):
                            board.set_cell_value(char, row, col)
                            self.iterations += 1
                            
                            self.solve(board)
                            board.set_cell_value(EMPTY_SQUARE, row, col)
                    return
        print(board, end="\r")
        print(f"Iterations: {self.iterations} Solutions: {self.found_solutions}", end="\r")
        self.found_solutions += 1
