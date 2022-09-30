from board import Board
from cell import Cell 
from copy import deepcopy

EMPTY_SQUARE = "."

class LeastPossibleSudokuSolver:
    """Class used to solve any sized sudoku through looking at most likely characters.
    """

    def __init__(self) -> None:
        self.iterations = 1
        self.found_solutions = 1

    def solve(self, board: Board) -> None:
        """ Recursively finds all possible solutions for any sized Sudoku board. 
            Chooses a cell that has the lowest number of possible characters. 

        Args:
            board (list): 2d list of strings describing the board, "." are empty squares.
            box_size (int): The size of a box. in 9x9 sudoku this is 3.
        """

        board.calculate_possible_values_for_cells()
        least_option_cell = self.cell_with_least_options(board)

        # Only solved boards should be printed. 
        if board.is_solved():
            print(board, end="\r")
            print("Iterations", self.iterations, "solutions", self.found_solutions, end="\r")
            self.found_solutions = self.found_solutions + 1
        
        if not least_option_cell:
            return

        if least_option_cell.get_value() == EMPTY_SQUARE:
            for char in least_option_cell.get_possible_chars():
                board.set_cell_value(char, least_option_cell.get_row(), least_option_cell.get_col())
                self.iterations += 1                
                
                if len(board) > 20:
                    # It takes an obscene amount of time to solve larger boards. 
                    # So in this case its more fun to see how it solves them in the terminal :) 
                    print(board, end="\r")
                    print("Iterations", self.iterations, "solutions", self.found_solutions, end="\r")

                self.solve(deepcopy(board))
                board.set_cell_value(EMPTY_SQUARE, least_option_cell.get_row(), least_option_cell.get_col())
            return

    def cell_with_least_options(self, board: Board) -> Cell:
        """ Finds the cell in the board with the least possible numbers in it. 

        Args:
            board (Board): The board to look at.

        Returns:
            Cell: The cell with least possible values
        """
        least_options_num = len(board.get_valid_chars()) + 1
        least_option_cell = None
        for cell in board.get_all_cells():
            if len(cell.get_possible_chars()) == 0:
                continue # Meaning, already added a number
            if len(cell.get_possible_chars()) < least_options_num:
                least_option_cell = cell 
                least_options_num = len(cell.get_possible_chars())
        return least_option_cell
        