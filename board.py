from cell import Cell

EMPTY_SQUARE = "."

class Board: 
    """ A board used for Sudoku
    """

    def __init__(self, board: list[Cell], box_size: int):
        """A board used for Sudoku

        Args:
            board (list[Cell]): A 2d list of cells, used for the board.
            box_size (int): The size of a box. In 9x9 sudoku this is 3. 
        """
        self._board: list[Cell] = board
        self._valid_chars = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:len(self._board)]
        self.box_size = box_size

    def is_solved(self) -> bool:
        """Checks if the board is solved.

        Returns:
            bool: True if the board is solved, else false
        """
        cells = self.get_all_cells()
        for cell in cells: 
            if cell.get_value() == EMPTY_SQUARE:
                return False 
        return True 

    def get_all_cells(self) -> list[Cell]:
        """Gets a 1 dimensional list of all the cells.

        Returns:
            list: The list of cells. 
        """ 
        return [cell for sublist in self._board for cell in sublist]

    def get_valid_chars(self) -> list:
        """Gets the characters that can be used in this board.

        Returns:
            list: The list of chars that can be used in this board. 
        """
        return self._valid_chars[0:len(self._board)]
        
    def get_cell(self, row: int, col: int) -> Cell:
        """Gets a cell from the board. 

        Args:
            row (int): The row of the cell
            col (int): The col of the cell

        Returns:
            Cell: The cell
        """
        return self._board[row][col]

    def set_cell_value(self, value: str, row: int, col: int) -> None:
        """Sets a cell`s value.

        Args:
            value (str): The value to be set
            row (int): The row of the cell
            col (int): The col of the cell
        """
        self.get_cell(row, col).set_value(value)

    def calculate_possible_values_for_cells(self) -> None:
        """Calculates all the possible moves for every cell.
        """
        for cell in self.get_all_cells(): 
            if cell.get_value() != EMPTY_SQUARE:
                cell.set_possible_chars([])
                continue

            possible_chars_for_cell = []
            for char in self.get_valid_chars():
                if self.is_legal_move(char, cell.get_row(), cell.get_col()):
                    possible_chars_for_cell.append(char)
            
            cell.set_possible_chars(possible_chars_for_cell)
            
    def is_legal_move(self, value: str, row: int, col: int) -> bool:
        """ Checks if a move would be legal

        Args:
            value (str): The value to input
            row (int): The row you want to put it in
            col (int): The column you want to put it in 

        Returns:
            bool: True if possible possible move, else false 
        """

        if self.value_is_in_row(value, row):
            return False 

        if self.value_is_in_col(value, col):
            return False 

        if self.value_is_in_box(value, row, col):
            return False 

        return True
        
    def value_is_in_row(self, value: str, row: int) -> bool:        
        """Checks if a value exists in a row. 

        Args:
            value (str): The value to look for.
            row (int): The row to check in

        Returns:
            bool: True if the value is in the row, else false.
        """
        for cell in self._board[row]:
            if cell.get_value() == value: 
                return True 
        return False 
        
    def value_is_in_col(self, value: str, col: int) -> bool:
        """Checks if a value exists in a column

        Args:
            value (str): The value to look for.
            col (int): The col to check in.

        Returns:
            bool: True if the value is in the col, else false. 
        """
        for row in self._board:
            if row[col].get_value() == value:
                return True 
        return False

    def value_is_in_box(self, value: str, row: int, col: int) -> bool:
        """Checks if a value is in a sudoku box.

        Args:
            value (str): The value to look for.
            row (int): The row of the cell.
            col (int): The col of the cell. 

        Returns:
            bool: Ture if the value is in the box, else false. 
        """
        box_row = row // self.box_size * self.box_size
        box_col = col // self.box_size * self.box_size
        # Get only the relevant rows for this grid. 
        rows_in_box = self._board[box_row : box_row + self.box_size]
        for row in rows_in_box:
            # Shorten the row to the relevant grid.
            row = row[box_col : box_col + self.box_size]
            for cell in row: 
                if cell.get_value() == value: 
                    return True 
        return False

    def __repr__(self) -> str:
        res = "\n"
        res += "-"*len(self._board)*3 + "\n"

        for irow, row in enumerate(self._board):
            for icell, cell in enumerate(row):
                icell += 1
                if icell == 1:
                    res += "| "
                res += str(cell) + " "
                if icell % self.box_size == 0:
                    res += "| "
                if icell % len(self._board) == 0:
                    res += "\n"
            irow += 1 
            if irow % self.box_size == 0:
                res += "-"*len(self._board)*3 + "\n"
        # NB Use end="\r" when printing
        return res

    def __len__(self) -> int: 
        return len(self._board)
